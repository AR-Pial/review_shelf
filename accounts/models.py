import uuid
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models
from django_countries.fields import CountryField

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Automatically set the username to the email if not provided
        if 'username' not in extra_fields:
            extra_fields['username'] = email  # Set username as email

        return self.create_user(email, password, **extra_fields)




class CustomUserModel(AbstractUser):
    """
    Custom user model that extends the default AbstractUser model.
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, db_index=True) 

    username = models.CharField(max_length=200, unique=True, null=True, blank=True) 
    country = CountryField(blank_label='(select country)', null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []  

    def __str__(self):
        """
        Return the string representation of the user.
        """
        return self.username if self.username else ""
    
    def save(self, *args, **kwargs):
        """
        Automatically set the username to the email if not set.
        """
        if self.is_superuser and not self.username:
            self.username = self.email  # Set the username to email if not set
        super().save(*args, **kwargs) 
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"  
      
    class Meta:
        ordering = ('username', 'first_name', 'email',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'custom_user_model'

