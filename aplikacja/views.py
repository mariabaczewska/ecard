from django.shortcuts import render
from .models import (
    Karta,
    Measurement,
)

# Create your views here.
def patients_list(request):
    ekarty = Karta.objects.all()
    return render(request, 'aplikacja/patient_list.html', {'ekarty': ekarty})

def patient_details(request, card_id):
    card = Karta.objects.get(id=card_id)
    measurements = Measurement.objects.filter(patient = card.patient)
    return render(
        request,
        'aplikacja/patient_details.html',
        {'card': card, 'measurements': measurements}
    )
