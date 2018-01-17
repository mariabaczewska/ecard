from django.db import models
from django.utils import timezone
# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=40)

    def __str__(self):
        return '{0} {1}'.format(self.name, self.surname)

class Nurse(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=40)

    def __str__(self):
        return '{0} {1}'.format(self.name, self.surname)

class Patient(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=40)
    pesel = models.CharField(max_length=9)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} {1}'.format(self.name, self.surname)

class Karta(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    description = models.TextField()

    def __str__(self):
        if self.patient:
            return 'Karta: {0} {1}'.format(self.patient.name, self.patient.surname)
        else:
            return 'unknown'

class Measurement(models.Model):
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    value = models.FloatField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True, null=True)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
