from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from Home.models import UserModel
from django import forms


class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ('location', 'contactno', 'organization',
                  'facility_type', 'avail_type', 'remarks')
        labels = {
            'location': _('Enter the location '),
            'contactno': _('Contact No '),
            'organization': _('Organization/Contact Person Name '),
            'facility_type': _('Select the Facility Type '),
            'avail_type': _('Select the Availability Type '),
            'remarks': _('Remarks '),
        }
        # widgets = {
        #     'location': forms.TextInput(attrs={
        #         'class': 'form-control',
        #     }),
        #     'contactno': forms.NumberInput(attrs={
        #         'class': 'form-control',
        #     }),
        # }
