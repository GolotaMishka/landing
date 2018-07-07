from django.shortcuts import render
from .forms import *


def landing(request):

    return render(request, 'landing/index.html', locals())


def curse1(request):

    form = SubscriberFaceToFaceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data  = form.cleaned_data
        print (data["name"])


        new_form = form.save()
        return render(request, 'landing/modal1.html', locals())
    else:
        return render(request, 'landing/firstCurse.html', locals())

def curse2(request):

    form = SubscriberGroupForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data  = form.cleaned_data
        print (data["name"])

        new_form = form.save()
        return render(request, 'landing/modal2.html', locals())

    else:
        return render(request, 'landing/secondCurse.html', locals())



