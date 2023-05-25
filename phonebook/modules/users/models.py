from django.db import models
from django.urls import reverse
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserMannager(BaseUserManager):

    def create_user(self, firstname, lastname, email, phone, password=None):
        """
        Creates and saves a User with the given fullname, email, phone and password.
        """
        if not email:
            raise ValueError('User should have an email')
        if not phone:
            raise ValueError('User should have phone start with code country ex +966')
        
        user = self.model(
            firstname   = firstname,
            lastname    = lastname,
            email       = self.normalize_email(email),
            phone       = phone
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, firstname, lastname, email, phone, password=None):
        """
        Creates and saves a SuperUser with the given fullname, email, phone and password.
        """
        user = self.create_user(firstname=firstname, lastname=lastname, email=email, phone=phone, password=password)
        user.is_superuser           = True
        user.is_active              = True
        user.is_staff               = True
        user.save(using=self._db)

        return user

class UserModel(AbstractBaseUser, PermissionsMixin):
    id              = models.BigAutoField(primary_key=True, auto_created=True, blank=False, unique=True, null=False, verbose_name='User ID', editable=False)
    firstname       = models.CharField(verbose_name='User First name', max_length=100, blank=False, null=False)
    lastname        = models.CharField(verbose_name='User Last name', max_length=100, blank=False, null=False)
    email           = models.EmailField(max_length=254, unique=True, null=False, blank=False, verbose_name='User Email')
    phone           = models.CharField(max_length=20, unique=True, blank=False, null=False, verbose_name='User Phone')
    password        = models.CharField(max_length=150, blank=False, null=False, verbose_name='User Pass')
    is_active       = models.BooleanField(default=True, verbose_name='User Active')
    is_staff        = models.BooleanField(default=False, verbose_name='User Staff')
    is_superuser    = models.BooleanField(default=False, verbose_name='User SuperUSer')
    is_driver       = models.BooleanField(default=False, verbose_name='User Driver')
    is_client       = models.BooleanField(default=False, verbose_name='User Client')
    date_join       = models.DateTimeField(auto_now_add=True, verbose_name='User Create')
    last_login      = models.DateTimeField(auto_now=True, verbose_name='User Last login')

    USERNAME_FIELD  = 'phone'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'email']
    objects         = UserMannager()

    class Meta:
        app_label           = 'users'
        db_table            = 'Users'
        managed             = True
        verbose_name        = 'User Model'
        verbose_name_plural = 'Users Model'
        indexes             = [ models.Index(fields=['id'], name='id_user'), models.Index(fields=['phone'], name='phone_user'), 
                               models.Index(fields=['email'], name='email_user')]

    def get_full_name(self):
        '''Override `get_full_name()` method'''
        return ' '.join([elm.strip() for elm in [self.firstname, self.lastname]])
    
    def get_short_name(self):
        '''Override `get_short_name()` method'''
        return self.lastname
    
    def get_absolute_url(self):
        return reverse("users:user_details", kwargs={"id": self.id, 'email':self.email, 'phone':self.phone})
    