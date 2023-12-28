from django.shortcuts import render, redirect
from .forms import ParticipantForm, VehicleForm

def participant_form(request):
    if request.method == 'POST':
        participant_form = ParticipantForm(request.POST, prefix='participant')
        vehicle_form = VehicleForm(request.POST, prefix='vehicle')

        if participant_form.is_valid() and vehicle_form.is_valid():
            # Save the forms to the database (optional, based on your requirement)
            participant = participant_form.save()
            vehicle = vehicle_form.save(commit=False)
            vehicle.participant = participant
            vehicle.save()

            # Redirect to the success page
            return redirect('submission_success')
    else:
        participant_form = ParticipantForm(prefix='participant')
        vehicle_form = VehicleForm(prefix='vehicle')

    return render(request, 'validation_app/participant_form.html', {'participant_form': participant_form, 'vehicle_form': vehicle_form})

def submission_success(request):
    return render(request, 'validation_app/submission_success.html')
