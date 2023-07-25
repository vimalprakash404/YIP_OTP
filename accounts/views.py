import string
import random
import requests
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import MyForm,UpdateForm,LoginForm
from .models import Data, PreRegister
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib import messages

def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def make_api_request(form_data,API_URL):
    try:
        response = requests.post(API_URL, data=form_data)
        print(response.text)
        response_json = response.json()
        return response_json
    except requests.exceptions.RequestException as e:
        # Handle any exception that might occur during the API call
        print(f"Error: {e}")
        return None

def pre_register(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the form data if it's valid
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            district = form.cleaned_data['district']

            # Make API request with form data
            api_data = {
                'prereg_name': name,
                'prereg_email': email,
                'prereg_mob': mobile,
                'districtd': district,
              #  'combinedInstitution':1,
            }
            api_response = make_api_request(api_data,'https://dev.yip.kerala.gov.in/yipapp/index.php/Idea2021/add_pre_reg/')

            if api_response:
                # If the API request is successful, display the response on the success page
                print(api_response.get("Success"))
                if api_response.get("Success") == "1":
                    context={
                        'name': name,
                        'email': email,
                        'mobile': mobile,
                        'district': district,
                    }
                    return render(request, 'otp_verification.html',context)
                return render(request, 'success.html', {'response': api_response})
            else:
                return render(request, 'error.html')
    else:
        form = MyForm()

    return render(request, 'pre_reg.html', {'form': form})



def api_check_otp_view(request):
    if request.method == 'POST':
        otp_received = request.POST["otp"]
        # Retrieve data from sessions
        prereg_name = request.POST['name']
        prereg_email = request.POST['email']
        prereg_mob = request.POST['mobile']
        districtd = request.POST['districtd']
        # Make API request with form data
        print(prereg_name)
        print(prereg_email)
        print(prereg_mob)
        print(districtd)
        api_data = {
            'otp_received': otp_received,
            'user_id': prereg_email,  # Assuming prereg_email is the user_id
            'prereg_name': prereg_name,
            'prereg_email': prereg_email,
            'prereg_mob': prereg_mob,
            'districtd': 1,
        }

        api_response = make_api_request(api_data,'https://dev.yip.kerala.gov.in/yipapp/index.php/Com_mobile_otp/checkotp/')
        if api_response:
                context={}
                if api_response["Success"]== "1":
                    
                    if create_user_with_random_password(prereg_email):
                        if PreRegister.objects.filter(prereg_email=prereg_email).exists():
                            ob=PreRegister.objects.get(prereg_email=prereg_email)
                        else:
                            ob=PreRegister()
                            ob.prereg_mob=prereg_mob
                            ob.districtd=districtd
                            ob.prereg_name=prereg_name
                            ob.prereg_email=prereg_email
                            ob.save()
                        context["message"] = "Registration Details Successfully Saved.Login Credentials shaerd to your registered email id .Now you can continue to complete the registeration. "
                    else :
                        context["wrong"]="user already exist"

                else :
                     context["wrong"]=api_response["msg"]
                return render(request, 'otp_verification.html',context)
        else:
                return render(request, 'error.html')
    else:
        return render(request, 'otp_verification.html')


def update_data_view(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'update_form.html', {'form': form,"message":"updated successfully"})
    else:
        try:
            userob=User.objects.get(id=request.user.id)
            prereg_data = PreRegister.objects.get(prereg_email=request.user.username)  # Change 'user_id' to the appropriate field for user identification
            print(request.user.username+"___________")        
        except PreRegister.DoesNotExist:
            prereg_data = None

        # Initialize the form with initial values from the PreRegister model
        initial_data = {}
        if prereg_data:
            print("good")
            initial_data = {
                'user': request.user.id,
                'Ideator_name': prereg_data.prereg_name,
                'ideator_mobile': prereg_data.prereg_mob,
                'districtd': prereg_data.districtd,
            }
        
        form = UpdateForm(initial=initial_data)

    return render(request, 'update_form.html', {'form': form})

def create_user_with_random_password(email):
    password = generate_random_password()
    if User.objects.filter(email=email).exists():
        return False
    user = User.objects.create_user(username=email, email=email, password=password)
    print("user created")
    # Send the generated password to the user's email
    subject = 'YIP Password'
    message = f'Username: {email} <br> Password : {password}'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
    return True

def login_view(request):
    form=LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')  # Replace 'username' with the name of the username input field in your login form
        password = request.POST.get('password')  # Replace 'password' with the name of the password input field in your login form

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page or any other desired page after successful login
            return redirect('update_data')
        else:
            # Display an error message for invalid login
            return render(request, 'login.html',{"message":'Invalid login credentials. Please try again.'})  # Redirect back to the login page for reattempt
    else:
        # Render the login page when accessing it via GET request
        return render(request, 'login.html',{"form":form})
