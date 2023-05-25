from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from .forms import AddContactForm
from .models import ContactModel


class AddContactView(CreateView):
    template_name   = 'phonebook/home.html'
    form_class      = AddContactForm
    success_url     = reverse_lazy('phonebook:contact-list')


    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)


class ContactList(ListView):
    template_name       = 'phonebook/contact_list.html'
    context_object_name = 'contacts'
    model               = ContactModel

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["contacts"] = self.model.objects.values('contact').distinct()
    #     return context
    

    def get_queryset(self):
        obj = self.model.objects.values('contact').distinct()
        print(obj)
        return super().get_queryset()
    