from django.forms import ModelForm
from Home.models import UserModel


class UserForm(ModelForm):
    class Meta:
        model = UserModel
        exclude = ('ver_type', 'ver_done_by', 'is_approved', 'date',)
