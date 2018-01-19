from django.shortcuts import (
    render,
    redirect,
)

from django.contrib.auth.models import User
from .models import (
    Karta,
    Measurement,
    Doctor,
    Patient,
    MyUser,
)
def index(request):
    return render(request, 'aplikacja/index.html')
# Create your views here.
def patient_list(request):
    ekarty = Karta.objects.all()
    lekarze = Doctor.objects.all()
    return render(request, 'aplikacja/patient_list.html', {'ekarty': ekarty, 'lekarze':lekarze})

def patient_details(request, card_id):
    card = Karta.objects.get(id=card_id)
    measurements = Measurement.objects.filter(patient = card.patient)
    return render(
        request,
        'aplikacja/patient_details.html',
        {'card': card, 'measurements': measurements}
    )

def patient_add(request):
    name = request.POST.get("name")
    surname = request.POST.get("surname")
    PESEL = request.POST.get("PESEL")
    desc = request.POST.get("desc")
    doctor_id = int(request.POST.get("doctor_id"))
    doctor = Doctor.objects.get(id = doctor_id)
    patient = Patient(
        name=name,
        surname=surname,
        pesel=PESEL,
        doctor=doctor,
    )
    patient.save()

    karta = Karta(
        patient=patient,
        description=desc,
    )
    karta.save()
    return redirect("patient_list")

def measurement_add(request):
    value = request.POST.get("value")
    card_id = int(request.POST.get("card_id"))
    card = Karta.objects.get(id=card_id)

    measurement=Measurement(
    value=value,
    patient=card.patient,
    )
    measurement.save()
    return redirect("patient_details", card_id)

def user_add(request):
    role=request.POST.get("role")
    name=request.POST.get("name")
    surname=request.POST.get("surname")
    password=request.POST.get("password")
    username="{}_{}".format(name.lower(), surname.lower())
    user = User.objects.create_user(
        username=username,
        password=password,
        first_name=name,
        last_name=surname,
    )
    user.save()

    myuser=MyUser(
    user=user,
    role=role
    )
    myuser.save()

#    if myuser.role="Nurse":
#        nurse=Nurse(
#            name=name,
#            surname=surname,
#            myuser=myuser,
#        )
##
#    elif myuser.role="Doctor":
#        doctor=Doctor(
#            name=name,
#            surname=surname,
#            myuser=myuser,
#        )
#        doctor.save()
#    return redirect("user_list")

#    def user_list(request):
#        user = MyUser.objects.all()
#        return render(request, 'aplikacja/user_list.html', {'user': user})
