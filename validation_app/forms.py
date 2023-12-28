# validation_app/forms.py

from django import forms
from django.core.validators import MinValueValidator, RegexValidator
from datetime import date, timedelta
from .models import Participant, Vehicle

class ParticipantForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]

    VEHICLE_TYPE_CHOICES = [
        ('V8', 'V8'),
        ('Van', 'Van'),
        ('Convertible', 'Convertible'),
        ('Bicycle', 'Bicycle'),
        ('Bus', 'Bus'),
        ('Ambulance', 'Ambulance'),
        ('Coupe', 'Coupe'),
        ('Caravan', 'Caravan'),
    ]

    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Choose the date of birth."
    )

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        help_text="Choose the gender."
    )

    car_plate_number = forms.CharField(
        max_length=20,
        validators=[RegexValidator(regex=r'^(IT|RDF|RNP|GR|GP)\d{2,}$', message='Invalid car plate number.')]
    )

    has_driving_license = forms.BooleanField(
        initial=False,
        required=False,
        help_text="Check if the participant has a driving license."
    )

    vehicle_type = forms.ChoiceField(
        choices=VEHICLE_TYPE_CHOICES,
        help_text="Choose the type of vehicle."
    )

    class Meta:
        model = Participant
        fields = '__all__'


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

    def clean_car_plate_number(self):
        car_plate_number = self.cleaned_data['car_plate_number']

        government_prefixes = ['RDF', 'RNP', 'GR', 'GP', 'IT']
        if any(car_plate_number.startswith(prefix) for prefix in government_prefixes):
            return car_plate_number

        if not car_plate_number[:3].isalpha() or not ('RAA' <= car_plate_number[:3] <= 'RAH'):
            raise forms.ValidationError("Car plate number should start with alphabets between 'RAA' and 'RAH'.")

        if not car_plate_number[3:].isdigit() or not (0 <= int(car_plate_number[3:]) <= 999):
            raise forms.ValidationError("Car plate number should be followed by three digits between 0 and 9.")

        return car_plate_number
