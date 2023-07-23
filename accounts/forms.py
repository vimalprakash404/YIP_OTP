from django import forms
from .models import Data
DISTRICT_CHOICES = [
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
    # Add more choices as needed
]

class MyForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    mobile = forms.CharField(label='Mobile',widget=forms.TextInput(attrs={"pattern":"[7-9]{1}[0-9]{9}" ,"title":"Phone number with 7-9 and remaing 9 digit with 0-9"}))
    district = forms.ChoiceField(label='District', choices=DISTRICT_CHOICES)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'
class OtpForm(forms.Form):
    otp = forms.CharField(label='Name', max_length=100)


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = '__all__'
        widgets = {
            'ideator_dob': forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['districtd'].label = 'District'
        self.fields['ideator_mobile'].label = 'Mobile'
        self.fields['combinedInstitution'].label = 'Institution'
        self.fields['ideator_dob'].label = 'Date of Birth'
        self.fields['ideator_cat'].label = 'Ideator category'
        self.fields['ideator_year'].label = 'Year'
        self.fields['ideator_dep'].label = 'Department'
        self.fields['type_identity_no'].label = 'Identity No'
        self.fields['btnval'].label = 'Btn  Value'
        self.fields['bank_acno'].label = 'Bank Account Number'
        self.fields['bank_name'].label = 'Bank Name'
        self.fields['bank_ifsc'].label = 'Bank IFSC'

from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'