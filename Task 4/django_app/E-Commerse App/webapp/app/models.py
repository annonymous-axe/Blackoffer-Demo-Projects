from django.db import models
from django.conf import settings
from django.utils import timezone


class DiabetesPrediction(models.Model):
    gender = models.FloatField()
    age = models.IntegerField()    
    hypertension = models.IntegerField()
    heart_disease = models.IntegerField()
    smoking_history = models.IntegerField()
    bmi = models.FloatField()
    HbA1c_level = models.FloatField()
    blood_glucose_level = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    result = models.CharField(max_length=50)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Diabetes result for {self.user}"