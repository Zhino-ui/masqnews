from django.contrib import admin
from .models import Subscriber, ContactMessage

# Register your models here.
admin.site.register(Subscriber)
admin.site.register(ContactMessage)