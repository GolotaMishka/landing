from django.shortcuts import render
from .forms import SubscriberForm


def landing(request):

    form = SubscriberForm(request.POST or None)


    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data  = form.cleaned_data
        print (data["name"])

        new_form = form.save()


    return render(request, 'landing/index.html', locals())

def curse1(request):

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data  = form.cleaned_data
        print (data["name"])

        new_form = form.save()


    return render(request, 'landing/firstCurse.html', locals())

def curse2(request):

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data  = form.cleaned_data
        print (data["name"])

        new_form = form.save()


    return render(request, 'landing/secondCurse.html', locals())



