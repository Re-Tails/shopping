from django.shortcuts import render
from django.http import HttpResponse
from direct.forms import RegistrationForm
from django.views.generic import TemplateView


def register(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        form.save()

    context={'form': form}
    #if request.method == 'POST':
    #    if form.is_valid():
    #        obj = Customer
    #        obj.password = form.cleaned_data['Name']

    #        obj.save()
    #        return HttpResponseRedirect('/admin/')

    return render(request, 'registration.html', {'form':form})
