from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class Customer(models.Model):
    class Meta:
        verbose_name_plural = "Customers"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)


    def validate_fields(self):
        if not self.first_name:
            raise ValidationError("First name is required.")
        if not self.last_name:
            raise ValidationError("Last name is required.")
        if not self.phone:
            raise ValidationError("Phone number is required.")
        if not self.email:
            raise ValidationError("Email address is required.")
        if not self.password:
            raise ValidationError("Password is required.")
        if len(self.phone) != 10:
            raise ValidationError("Phone number must be 10 digits.")
        try:
            validate_email(self.email)
        except ValidationError:
            raise ValidationError("Invalid email address.")
    

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return None

    def isExists(self):
        return Customer.objects.filter(email=self.email).exists()
    
