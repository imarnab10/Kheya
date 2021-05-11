from django.db import models
from django.utils.timezone import now

# Create your models here.


class UserModel(models.Model):
    facility_choices = [
        ('Oxygen', 'OXYGEN'),
        ('CovidBed', 'COVID BED'),
        ('CovidTest', 'COVID TESTING'),
        ('DoctorOnCall', 'DOCTOR ON CALL'),
        ('Ambulance', 'AMBULANCE'),
        ('Food', 'FOOD'),
        ('Medicine', 'MEDICINE'),
    ]
    avail_choices = [
        ('Available', 'AVAILABLE'),
        ('NotAvailable', 'NOT AVAILABLE'),
        ('CurrentlyNotAvailable', 'CURRENTLY NOT AVAILABLE'),
        ('AvailableSoon', 'AVAILABLE SOON'),
        ('Depends', 'DEPENDS')
    ]
    ver_choices = [
        ('Verified', 'VERIFIED'),
        ('NotVerified', 'NOT VERIFIED'),
        ('CallNotAnswered', 'CALL NOT ANSWERED'),
        ('PhoneUnreachable', 'PHONE UNREACHABLE')
    ]
    ver_done_by_choices = [
        ('Asif', 'ASIF'),
        ('Abanti', 'ABANTI'),
        ('Anusuya', 'ANUSUYA'),
        ('Debartha', 'DEBARTHA'),
        ('Nirmendu', 'NIRMENDU'),
        ('Rajsekhar', 'RAJSEKHAR'),
        ('Sharma', 'SHARMA'),
        ('Tuhin', 'TUHIN'),
        ('Rahi', 'RAHI'),
        ('Trishani', 'TRISHANI'),
        ('Risita', 'RISITA')
    ]
    location = models.CharField(max_length=50)
    contactno = models.BigIntegerField()
    organization = models.CharField(max_length=50, default=None)
    facility_type = models.CharField(
        max_length=15, choices=facility_choices, default=None)
    avail_type = models.CharField(
        max_length=21, choices=avail_choices, default='SELECT')
    ver_type = models.CharField(
        max_length=20, choices=ver_choices, default='SELECT')
    remarks = models.TextField(max_length=200, blank=True, null=True)
    ver_done_by = models.CharField(
        max_length=15, choices=ver_done_by_choices, default='SELECT')
    is_approved = models.BooleanField(default=False)
    date = models.DateTimeField(default=now)

    def __str__(self):
        return self.facility_type

    @staticmethod
    def get_all_oxygen():
        return UserModel.objects.filter(is_approved=True).filter(facility_type='Oxygen')

    @staticmethod
    def get_all_doconcall():
        return UserModel.objects.filter(is_approved=True).filter(facility_type='DoctorOnCall')

    @staticmethod
    def get_all_covidbed():
        return UserModel.objects.filter(is_approved=True).filter(facility_type='CovidBed')

    @staticmethod
    def get_all_covidtest():
        return UserModel.objects.filter(is_approved=True).filter(facility_type='CovidTest')

    @staticmethod
    def get_all_ambulance():
        return UserModel.objects.filter(is_approved=True).filter(facility_type='Ambulance')

    @staticmethod
    def get_all_food():
        return UserModel.objects.filter(is_approved=True).filter(facility_type='Food')

    @staticmethod
    def get_all_medicine():
        return UserModel.objects.filter(is_approved=True).filter(facility_type='Medicine')
