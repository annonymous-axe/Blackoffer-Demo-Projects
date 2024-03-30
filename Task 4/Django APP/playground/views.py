from django.shortcuts import render, redirect

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from .models import Record

from django.contrib import messages

# Create your views here.
# Takes a request -> Reqturn Response
# So it is request handler

def index(request):
    return render(request, 'index.html')

# - Register a user

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Registed Successfully! Please login again to continued.")

            return redirect('my-login')

    
    context = {'form':form}

    return render(request, 'register.html', context=context)

# - Login a user

def login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                messages.success(request, "Loged In successfully!")

                return redirect("dashboard")

    context = {'form':form}

    return render(request, 'my-login.html', context=context)



# Dashboard view

@login_required(login_url="my-login")
def dashboard(request):

    my_records = Record.objects.all()

    context = {"records": my_records}

    return render(request, "dashboard.html", context=context)



# - User Logout

def logout(request):

    auth.logout(request)

    messages.success(request, "Loged Out successfully!")

    return render(request, "index.html")  


# - Create a record

@login_required(login_url="my-login")
def create_record(request):

    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Record Added!")

            return redirect("dashboard")
        
    context = {"form": form}

    return render(request, 'create-record.html', context=context)
        
# - Update a record

@login_required(login_url="my-login")
def update_record(request, pk):

    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == "POST":

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, "Record Updated!")

            return redirect("dashboard")
        
    context = {"form": form}

    return render(request, "update-record.html", context=context)

# - View single record

@login_required(login_url='my-login')
def singular_record(request, pk):

    record = Record.objects.get(id=pk)

    context = {'record':record}

    return render(request, 'view-record.html', context=context)


# - Delete Recrod

@login_required(login_url="my-login")
def delete_record(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Record Removed!")

    return redirect('dashboard')