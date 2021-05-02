# Generated by Django 3.2 on 2021-05-01 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_rename_userinput_usermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='avail_type',
            field=models.CharField(choices=[('Available', 'AVAILABLE'), ('NotAvailable', 'NOT AVAILABLE'), ('CurrentlyNotAvailable', 'CURRENTLY NOT AVAILABLE'), ('AvailableSoon', 'AVAILABLE SOON'), ('Depends', 'DEPENDS')], default='SELECT', max_length=21),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='remarks',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='ver_done_by',
            field=models.CharField(choices=[('Asif', 'ASIF'), ('Abanti', 'ABANTI'), ('Anusuya', 'ANUSUYA'), ('Debartha', 'DEBARTHA'), ('Nirmendu', 'NIRMENDU'), ('Rajsekhar', 'RAJSEKHAR'), ('Sharma', 'SHARMA'), ('Tuhin', 'TUHIN'), ('Rahi', 'RAHI'), ('Trishani', 'TRISHANI'), ('Risita', 'RISITA')], default='SELECT', max_length=15),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='ver_type',
            field=models.CharField(choices=[('Verified', 'VERIFIED'), ('NotVerified', 'NOT VERIFIED'), ('CallNotAnswered', 'CALL NOT ANSWERED'), ('PhoneUnreachable', 'PHONE UNREACHABLE')], default='SELECT', max_length=20),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='facility_type',
            field=models.CharField(choices=[('Oxygen', 'OXYGEN'), ('CovidBed', 'COVID BED'), ('CovidTest', 'COVID TESTING'), ('DoctorOnCall', 'DOCTOR ON CALL'), ('Ambulance', 'AMBULANCE'), ('Food', 'FOOD'), ('Medicine', 'MEDICINE')], default='SELECT', max_length=15),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='location',
            field=models.CharField(max_length=50),
        ),
    ]
