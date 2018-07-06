from django.contrib import admin
from .models import *


class SubscriberAdmin (admin.ModelAdmin):

    list_display = [field.name for field in Subscriber._meta.fields]
    list_filter = ['name','level','place']
    search_fields = ['name']

    fields = ["name","phone_number","level","place"]

    #exclude = ["email"]
	# inlines = [FieldMappingInline]
	# fields = []
    # #exclude = ["type"]
	# #list_filter = ('report_data',)
	# search_fields = ['category', 'subCategory', 'suggestKeyword']

    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)