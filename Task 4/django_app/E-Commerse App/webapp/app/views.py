from django.shortcuts import render, reverse, redirect, HttpResponse

from django.contrib.auth.decorators import login_required

from model.diabetes_model import make_prediction

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from .forms import CreateUserForm, LoginForm, User
from .models import DiabetesPrediction

import io

from django.contrib import messages

import joblib

user_profile = None

def index(request):

    return render(request, "index.html")

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Registed Successfully! Please login again to continued.")

            return redirect('login')
    
    context = {'form':form}

    return render(request, "account/register.html", context=context)

def login(request):

    form = LoginForm()

    error = None

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        print("Checking for vlaidaion........")

        if form.is_valid():

            print("Form is valid")

            username = request.POST['username']
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                user_profile = user

                auth.login(request, user)

                messages.success(request, "Loged In successfully!")

                return redirect("index")
            
        else:

            print("Form is not valid")

            error = "Password doesn't match with username!"

    context = {'form':form, 'error':error}

    return render(request, "account/login.html", context=context)

@login_required
def profile(request):

    current_user = request.user

    user_data = User.objects.get(username=current_user.username)

    flag = 0

    context = {'user': user_data, 'flag': flag}

    return render(request, "account/profile.html", context= context)

@login_required
def update_profile(request):

    current_user = request.user

    user_data = User.objects.get(username=current_user.username)

    flag = 1

    context = {'user': user_data, 'flag': flag}

    return render(request, "account/profile.html", context= context)


@login_required
def logout(request):

    auth.logout(request)

    messages.success(request, "Loged Out successfully!")

    return render(request, "index.html")  

@login_required
def diabetes_prediction(request):

    # make_prediction() # train the model

    if request.method == "POST":

        gender              = float(request.POST.get("gender"))
        age                 = float(request.POST.get("age"))
        hypertension        = float(request.POST.get("hypertension"))
        heart_disease       = float(request.POST.get("heart_disease"))
        smoking_history     = float(request.POST.get("smoking_history"))
        bmi                 = float(request.POST.get("bmi"))
        HbA1c_level         = float(request.POST.get("HbA1c_level"))
        blood_glucose_level = float(request.POST.get("blood_glucose_level"))
        user                = request.user

        diabetes_model = joblib.load('model/diabetes_model.pkl')    #  Read the model

        result = diabetes_model.predict([[gender, age, hypertension, heart_disease, smoking_history, 
                                          bmi, HbA1c_level, blood_glucose_level]])

        if result == 1:

            result = "Presence of Diabetes"

        else:

            result = "No Diabetes"

        prediction = DiabetesPrediction(
            gender=gender,
            age=age,
            hypertension=hypertension,
            heart_disease=heart_disease,
            smoking_history=smoking_history,
            bmi=bmi,
            HbA1c_level=HbA1c_level,
            blood_glucose_level=blood_glucose_level,
            result=result,
            user=user)
        
        prediction.save()

        return redirect('diabetes_result')
    
    return render(request, "prediction/diabetes.html")


def diabetes_result(request):

    prediction = DiabetesPrediction.objects.all().order_by("-created_at")

    user = request.user
    prediction = prediction.filter(user=user)
    return render(request,
                  "prediction/result.html",
                  {"prediction": prediction})

def download(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    prediction = DiabetesPrediction.objects.all()
    user = request.user
    prediction = prediction.filter(user=user)

    lines = []

    for predict in prediction:
        lines.append("age " + str(predict.age))
        lines.append("sex " + str(predict.sex))
        lines.append("bmi " + str(predict.bmi))
        lines.append("bp " + str(predict.bp))
        lines.append("tc " + str(predict.tc))
        lines.append("ldl " + str(predict.ldl))
        lines.append("hdl " + str(predict.hdl))
        lines.append("tch " + str(predict.tch))
        lines.append("ltg " + str(predict.ltg))
        lines.append("glucose " + str(predict.glucose))
        lines.append("date " + str(predict.created_at))
        lines.append("result " + str(predict.result))

        lines.append(" ")
        lines.append(" ")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='diabetesresult.pdf')



