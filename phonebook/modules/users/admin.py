from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseAdmin

from .forms import UserCreateForm, UserUpdateForm
from .models import UserModel
# Register your models here.


class UserAdmin(BaseAdmin):
    form        = UserCreateForm
    add_form    = UserUpdateForm

    readonly_fields = ['last_login']
    list_display    = ['firstname', 'lastname', 'phone', 'email', 'date_join']
    list_filter     = ['is_superuser']
    ordering        = ['email']
    search_fields   = ["email", "phone"]
    fieldsets = (
        (
            'Fields',
            {
                'fields': (
                    'firstname',
                    'lastname',
                    'email',
                    'phone',
                    'last_login',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'is_driver',
                    'is_client',
                )
            },
        ),
    )
    


admin.site.register(UserModel, UserAdmin)
admin.site.unregister(Group)