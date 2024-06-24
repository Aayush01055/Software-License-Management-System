from multiprocessing import AuthenticationError
from profile import Profile
from urllib import request
from django.shortcuts import render, redirect  
from Oper.forms import Oper_forms,Oper1_forms 
from Oper.models import brillentsec,feedcalcusers
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm


login_required = False
u=""
# Create your views here.  
def create(request):
    if request.method == "POST":
        form = Oper_forms(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home.html')
            except:
                pass
    else:
        form = Oper_forms()
    return render(request, 'home.html', {'form':form,'user':''})



#retrive data
def retrieve(request):  
        ret = brillentsec.objects.all()
        return render(request,'search.html',{'ret':ret} ) 

def retrieve_users(request):  
        ret1 = feedcalcusers.objects.all()
        return render(request,'search_user.html',{'ret1':ret1} ) 
#---------------------------------------------------------------------------

#update user and customer
def update(request,pk):
    up = brillentsec.objects.get(SrNo=pk)
    form = Oper_forms(instance=up)

    if request.method == 'POST':
        form = Oper_forms(request.POST, instance=up)
        if form.is_valid():
            form.save()
            return redirect('/search')

    context = {
        'opert': up,
        'form': form,
    }
    return render(request,'update.html',context)

def update_user(request,pk):
    up1 = feedcalcusers.objects.get(Id=pk)
    form1 = Oper1_forms(instance=up1)

    if request.method == 'POST':
        form1 = Oper1_forms(request.POST, instance=up1)
        if form1.is_valid():
            form1.save()
            return redirect('/search_user')

    context = {
        'opert': up1,
        'form': form1,
    }
    return render(request,'update_users.html',context)

#-------------------------------------------------------

#delete user and customer
def delete(request, pk):
    dele = brillentsec.objects.get(SrNo=pk)

    if request.method == 'POST':
        dele.delete()
        return redirect('/search')

    context = {
        'opert': dele,
    }
    return render(request, 'remove.html', context)

def delete_user(request, pk):
    dele1 = feedcalcusers.objects.get(Id=pk)

    if request.method == 'POST':
        dele1.delete()
        return redirect('/search_user')

    context = {
        'opert1': dele1,
    }
    return render(request, 'remove_user.html', context)
#---------------------------------------------------------------------------

#register user and customer
def register_customer(request):
        if request.method == 'POST':
            SerialNumber = request.POST['SerialNumber']
            CompName = request.POST['CompName']
            ActivationCode = request.POST['ActivationCode']
            ExpiryDate = request.POST['ExpiryDate']
            StartDate = request.POST['StartDate']
            CheckedOn=request.POST['CheckedOn']
            MacAddress=request.POST['MacAddress']
            Activated=request.POST['Activated']
            CheckedDt=request.POST['CheckedDt']

            if SerialNumber==SerialNumber:
                if brillentsec.objects.filter(MacAddress=MacAddress).exists():
                    messages.info(request, 'MACADDRESS ALREADY EXISTSs')
                    return redirect(register_customer)
                else:
                   user = brillentsec.objects.create(SerialNumber=SerialNumber, CompName=CompName,ActivationCode=ActivationCode,ExpiryDate=ExpiryDate,StartDate=StartDate,CheckedOn=CheckedOn,MacAddress=MacAddress,Activated=Activated,CheckedDt=CheckedDt)
                user.save()
                return render(request,'home.html',{'user':user})
            else:
                messages.info(request, 'SERIAL NUMBER ALREADY EXISTS')
                return redirect(register_customer)
        else:
            return render(request, 'create_customer.html')

def register_user(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password==confirm_password:
            if feedcalcusers.objects.filter(username=username).exists():
                    messages.info(request, 'USERNAME ALREADY EXISTS')
                    return redirect(register_user)
            else:
                user = feedcalcusers.objects.create(username=username,password=password,confirm_password=confirm_password )
                user.save()
                return render(request,'home.html',{'user':user})
        else:
                messages.info(request, 'PLEASE CHECK PASsWORD AND CONFIRM PASSWORD')
                return redirect(register_user)
    else:
        return render(request,'create_user.html')

#-----------------------------------------------------------------------------------------------------------
def home(request):
    return render(request, 'home.html',{'user':''})



#------------------------------------------------------------------------------------------------------------

def signin(request):
#usw mysql database
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']

        if feedcalcusers.objects.filter(username=username).exists():
            user = feedcalcusers.objects.get(username=username)
            u=user
            if user.password == password:
                return render(request,'home.html',{'user':user})
                
            else:
                messages.info(request, 'PASSWORD IS INCORRECT')
                return redirect(signin)
        else:
            messages.info(request, 'USERNAME IS INCORRECT')
            return redirect(signin)
    return render(request, 'login.html')

def signout(request):
    return render(request, 'home.html',{'user':''})
