from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import pyautogui as pu


# Create your views here.

def signup(request):
    if request.method == "POST":
        firstname = request.POST['Cname']
        lastname = request.POST['Cname2']
        pan_number = request.POST['pan']
        gst_number = request.POST['gst']
        register_number = request.POST['register']
        licence_number = request.POST['licence']
        state = request.POST.get('province')
        branch = request.POST.get('branches')
        address = request.POST['address']
        person_name = request.POST['person']
        contact1 = request.POST['contact1']
        email1 = request.POST['email1']
        email2 = request.POST['email2']
        contact2 = request.POST['contact2']
        location = request.POST['location']
        postalcode = request.POST['postalcode']
        # user_name = request.POST.get('userid', "default value")
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            # user = User.objects.create_user(username=user_name)
            # user.save()
            Registration(First_name=firstname,Last_name=lastname,pan_number=pan_number,gst_number=gst_number,
                         register_number=register_number,licence_number=licence_number,address=address,state_name=state,branch_name=branch,
                         person_name=person_name,contact_number1=contact1,email1=email1,email2=email2,contact_number2=contact2,
                         location=location,postal_code=postalcode,password=password1).save()
            pu.confirm("Account is Created Succsessfully")
            return redirect('/')

        else:
            messages.error(request,'Password is not matching')
            return redirect('signup')

    else:
        province = State.objects.all()
        d = {'province': province}
        return render(request, 'signup.html',d)

def load_branches(request):
    provinceing_id = request.GET.get('provinceing')
    branches =Branch.objects.filter(provinceing_id=provinceing_id).order_by('name')
    return render(request, 'courses_dropdown_list_options.html', {'branches': branches})

def forgot(request):
    return render(request,'forgot.html')

def forgot1(request):
    return render(request,'forgot-1.html')

def dashboard(request):
    return render(request,'dashboard.html')

def attendance(request):
    return render(request,'attendance.html')

def emp_details(request):
    return render(request,'emp-details.html')

def loans(request):
    return render(request,'loans.html')

def payslip(request):
    return render(request,'payslip.html')

def privacy(request):
    return render(request,'privacy.html')

def terms(request):
    return render(request,'terms.html')