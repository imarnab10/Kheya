from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from Home.forms import UserForm
from .models import UserModel
# Create your views here.


# class UserInput(View):
#     def get(self, request):
#         form = UserForm()
#         return render(request, 'index.html', {'form': form})
#
#     def post(self, request):
#         form = UserForm(request.POST)
#         if form.is_valid():
#             location = form.cleaned_data['location']
#             contactno = form.cleaned_data['contactno']
#             facility_type = form.cleaned_data['facility_type']
#             avail_type = form.cleaned_data['avail_type']
#             ver_type = form.cleaned_data['ver_type']
#             remarks = form.cleaned_data['remarks']
#             ver_done_by = form.cleaned_data['ver_done_by']
#             print(location)
#             p = UserModel(location=location,
#                           contactno=contactno,
#                           facility_type=facility_type,
#                           avail_type=avail_type,
#                           ver_type=ver_type,
#                           remarks=remarks,
#                           ver_done_by=ver_done_by,
#                           )
#             p.save()
#         return HttpResponseRedirect('/thanks/')
def product_detail_view(request):
    oxygens = UserModel.get_all_oxygen()
    doconcalls = UserModel.get_all_doconcall()
    covidbeds = UserModel.get_all_covidbed()
    covidtests = UserModel.get_all_covidtest()
    foods = UserModel.get_all_food()
    ambulances = UserModel.get_all_ambulance()
    medicines = UserModel.get_all_medicine()
    data = {
        'oxygens': oxygens,
        'doconcalls': doconcalls,
        'covidbeds': covidbeds,
        'covidtests': covidtests,
        'foods': foods,
        'ambulances': ambulances,
        'medicines': medicines,
    }
    return render(request, "products.html", data)


def user_input(request):
    context = {}

    # create object of form
    form = UserForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return HttpResponseRedirect('/product_view/')

    context['form'] = form
    return render(request, "index.html", context)