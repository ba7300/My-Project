from django.db import models

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=50)
    provinceing = models.ForeignKey(State, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Registration(models.Model):
    First_name = models.CharField(max_length=500)
    Last_name = models.CharField(max_length=500)
    pan_number = models.CharField(max_length=500)
    gst_number =models.CharField(max_length=500)
    register_number =models.CharField(max_length=500)
    licence_number =models.CharField(max_length=500)
    address =models.TextField()
    state_name = models.CharField(max_length=500)
    branch_name = models.CharField(max_length=500)
    person_name =models.CharField(max_length=500)
    contact_number1 =models.CharField(max_length=500)
    email1 =models.EmailField()
    email2 =models.EmailField()
    contact_number2 =models.CharField(max_length=500)
    location =models.TextField()
    postal_code =models.CharField(max_length=500)
    password =models.CharField(max_length=500)

    def __str__(self):
        return self.First_name
