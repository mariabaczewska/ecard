from django.contrib import admin
from .models import (
    Karta,
    Doctor,
    Patient,
    Measurement,
    Nurse,
) 

admin.site.register(Karta)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Measurement)
admin.site.register(Nurse)
# Register your models here.
