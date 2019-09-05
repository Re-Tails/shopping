from django.shortcuts import render
from django.http import HttpResponseRedirect
from direct.forms import RegistrationForm
from django.views.generic import TemplateView


def register(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/admin/')
        #For now after the user hits submit, they will be redirected to the admin page.
        #We should make some sort of confirmation page, or maybe redirect them to the login page.
        #extra comment ignore

    context={'form': form}
    return render(request, 'registration.html', {'form':form})
