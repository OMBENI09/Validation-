from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from simple_history.models import HistoricalRecords

class Participant(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]

    date_of_birth = models.DateField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(validators=[RegexValidator(regex=r'@ur\.ac\.rw$', message='Email should be from University of Rwanda.')])
    phone_number = models.CharField(max_length=20, validators=[RegexValidator(regex=r'^\+\d{1,}', message='Phone number should start with +(country code).')])
    reference_number = models.IntegerField(validators=[MinValueValidator(99), MaxValueValidator(999)])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    car_plate_number = models.CharField(max_length=20, validators=[RegexValidator(regex=r'^(IT|RDF|RNP|GR|GP)\d{2,}$', message='Invalid car plate number.')])
    has_driving_license = models.BooleanField(default=False)
    history = HistoricalRecords()

    class Meta:
        app_label = 'validation_app'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Vehicle(models.Model):
    car_plate_number = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    speed = models.IntegerField()
    weight = models.IntegerField()
    color = models.CharField(max_length=50)
    volume = models.IntegerField()
    area = models.IntegerField()
    mass = models.IntegerField()
    additional_field = models.IntegerField(default=0)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.car_plate_number}'s Vehicle"
