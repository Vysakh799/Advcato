from django.shortcuts import render,redirect
from .models import *
import bcrypt
# Create your views here.

def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

#user
def Ureg(request):
    if request.method=='POST':
        uname=request.POST['name']
        uphone=request.POST['phno']
        uemail=request.POST['email']
        uaddress=request.POST['address']
        upassword=request.POST['password']
        ucnfpassword=request.POST['cnf_password']
        if upassword==ucnfpassword:
            psw=upassword.encode('utf-8')
            salt=bcrypt.gensalt()               #Password Hashing
            psw_hashed=bcrypt.hashpw(psw,salt)
            data=User.objects.create(uname=uname,uphone=uphone,uemail=uemail,uaddress=uaddress,upassword=psw_hashed.decode('utf-8'))
            data.save()
            return redirect(index)
        else:
            print("Password dosen't match")
    return redirect(login)