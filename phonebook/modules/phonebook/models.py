from django.db import models
from django.urls import reverse



class ContactModel(models.Model):
    id              = models.BigAutoField(primary_key=True, auto_created=True, blank=False, unique=True, null=False, verbose_name='Contact ID', editable=False)
    contact         = models.CharField(verbose_name='Fullname', max_length=100, blank=False, null=False)


    class Meta:
        app_label           = 'phonebook'
        db_table            = 'CONTACT'
        verbose_name        = 'CONTACT'
        verbose_name_plural = 'CONTACTS'
        indexes             = [ models.Index(fields=['id'], name='contact_id')]

class PhoneNumbers(models.Model):
    id              = models.BigAutoField(primary_key=True, auto_created=True, blank=False, unique=True, null=False, verbose_name='Phone ID', editable=False)
    contact_id      = models.ForeignKey(ContactModel, on_delete=models.CASCADE, related_name='phone_numbers')
    phone           = models.CharField(max_length=255, unique=True, blank=False, null=False, verbose_name='Contact Phone')
    class Meta:
        app_label           = 'phonebook'
        db_table            = 'PHONENUMBERS'
        verbose_name        = 'PHONENUMBER'
        verbose_name_plural = 'PHONENUMBERS'
        indexes             = [ models.Index(fields=['id'], name='phone_id'), models.Index(fields=['phone'], name='contact_phone')]

    def get_absolute_url(self):
        return reverse("contact:contact_details", kwargs={"id": self.id})