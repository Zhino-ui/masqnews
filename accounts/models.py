from django.db import models
from newsletter_subscription.models import SubscriptionBase


# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    is_active =  models.BooleanField(default=False)
    subcribed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"