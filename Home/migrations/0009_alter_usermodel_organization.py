# Generated by Django 3.2 on 2021-05-11 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_usermodel_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='organization',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
