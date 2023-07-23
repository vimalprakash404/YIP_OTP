from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Data(models.Model):
    DISTRICT_CHOICES = (
         (1, 'Thiruvananthapuram'),
        (2, 'Kollam'),
        (3, 'Pathanamthitta'),
        (4, 'Alappuzha'),
        (5, 'Kottayam'),
        (6, 'Idukki'),
        (7, 'Ernakulam'),
        (8, 'Thrissur'),
        (9, 'Palakkad'),
        (10, 'Malappuram'),
        (11, 'Kozhikode'),
        (12, 'Wayanad'),
        (13, 'Kannur'),
        (14, 'Kasaragod'),
        # Add other district choices as needed
    )

    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Other'),
    )

    CATEGORY_CHOICES = (
        (4, 'Category 4'),
        (5, 'Category 5'),
        # Add other category choices as needed
    )

    YEAR_CHOICES = (
        (year, str(year)) for year in range(1999, 2024)
        # Add other year choices as needed
    )
    IDEATOR_DEP_CHOICES = (
        (1, 'Computer Science and Engineering'),
        (2, 'Electrical '),
        (3, 'Mechanical '),
        (4, 'Civil '),
        (5, 'Chemical '),
        (6, 'Biomedical '),
        # Add more engineering departments as needed
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    districtd = models.PositiveIntegerField(choices=DISTRICT_CHOICES)
    ideator_mobile = models.CharField(max_length=15)
    ideator_gender = models.PositiveIntegerField(choices=GENDER_CHOICES)
    ideator_dob = models.DateField()
    combinedInstitution = models.CharField(max_length=100)
    ideator_cat = models.PositiveIntegerField(choices=CATEGORY_CHOICES)
    ideator_year = models.PositiveIntegerField(choices=YEAR_CHOICES)
    ideator_dep = models.PositiveIntegerField(choices=IDEATOR_DEP_CHOICES)
    type_identity_no = models.CharField(max_length=100)
    btnval = models.IntegerField()
    Ideator_name = models.CharField(max_length=100,null=True)
    # cas_cat = models.CharField(max_length=50)
    bank_acno = models.CharField(max_length=100, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    bank_ifsc = models.CharField(max_length=100, blank=True, null=True)

class PreRegister(models.Model):
    PREREG_CHOICES = (
         (1, 'Thiruvananthapuram'),
        (2, 'Kollam'),
        (3, 'Pathanamthitta'),
        (4, 'Alappuzha'),
        (5, 'Kottayam'),
        (6, 'Idukki'),
        (7, 'Ernakulam'),
        (8, 'Thrissur'),
        (9, 'Palakkad'),
        (10, 'Malappuram'),
        (11, 'Kozhikode'),
        (12, 'Wayanad'),
        (13, 'Kannur'),
        (14, 'Kasaragod'),
        # Add other choices as needed
    )

    prereg_name = models.CharField(max_length=100)
    prereg_email = models.EmailField()
    prereg_mob = models.CharField(max_length=15)
    districtd = models.PositiveIntegerField(choices=PREREG_CHOICES)

    def __str__(self):
        return self.prereg_name