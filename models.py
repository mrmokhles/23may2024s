from django.db import models

# Create your models here.
class contactEnquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)




class CountryGDP(models.Model):
    name=models.CharField(max_length=50)
    code=models.CharField(max_length=4)
    year=models.CharField(max_length=5)
    value=models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
     return self.name
    


class Image(models.Model):
    name = models.CharField(max_length=50, default=None)
    img = models.ImageField(upload_to='images/', default=None)
    
#cascading dropdown
class Country(models.Model):
   name=models.CharField(max_length=50)
   def __str__(self):
      return self.name
class City(models.Model):
   country=models.ForeignKey(Country,on_delete=models.CASCADE)
   name=models.CharField(max_length=50)
   def __str__(self):
      return self.name
   
class Person(models.Model):
   name=models.CharField(max_length=50)
   country=models.ForeignKey(Country,on_delete=models.SET_NULL,blank=True,null=True)
   city=models.ForeignKey(City,on_delete=models.SET_NULL,blank=True,null=True)
   def __str__(self):
      return self.name


class InputInfo(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
      return self.name
    
class Profile(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    bio=models.CharField(max_length=50)
    def __str__(self):
      return self.name
    
class Item(models.Model):
    name=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
      return self.name
    
class Admin_add_employee(models.Model):

    emp_id=models.CharField(max_length=50)

    emp_name=models.CharField(max_length=50)
    emp_post_name=models.CharField(max_length=50)

    emp_grade=models.CharField(max_length=50)
    emp_salary=models.CharField(max_length=50)
    emp_bonus=models.CharField(max_length=50)

    emp_increment=models.CharField(max_length=50)
    emp_joining_date=models.DateTimeField(auto_now_add=True)

    emp_joining_month=models.CharField(max_length=50)
    emp_joining_year=models.CharField(max_length=50)
   
    def __str__(self):
      return self.emp_name
    

class Admin_add_overtime(models.Model):

    emp_id=models.CharField(max_length=50)

    emp_name=models.CharField(max_length=50)
    emp_month=models.CharField(max_length=50)

    overtime_hours=models.CharField(max_length=50)

    overtime_money=models.CharField(max_length=50)
    year=models.CharField(max_length=50)

    date=models.DateTimeField(auto_now_add=True)
   
   
    def __str__(self):
      return self.emp_name
    
class EmployeeLogin(models.Model):

    user_name=models.CharField(max_length=50)

    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)

    def __str__(self):
      return self.user_name