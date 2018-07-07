from django.contrib import admin
from .models import *


class SubscriberFaceToFaceAdmin (admin.ModelAdmin):

    list_display = [field.name for field in FaceToFace._meta.fields]
    list_filter = ['name','place']
    search_fields = ['name']

    fields = ["name","phone_number","place"]



    class Meta:
        model = FaceToFace

admin.site.register(FaceToFace, SubscriberFaceToFaceAdmin)



class SubscriberGroupAdmin (admin.ModelAdmin):

    list_display = [field.name for field in Group._meta.fields]
    list_filter = ['name','level']
    search_fields = ['name']

    fields = ["name","phone_number","level"]


    class Meta:
        model = Group

admin.site.register(Group, SubscriberGroupAdmin)