from django.urls import path
from .views import AddContactView, ContactList
app_name = 'phonebook'


urlpatterns = [
    path('create/', AddContactView.as_view(), name='home'),
    path('list/', ContactList.as_view(), name='contact-list'),
]