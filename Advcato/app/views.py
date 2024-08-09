from django.shortcuts import render,redirect
from .models import *
import bcrypt
from django.contrib import messages
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
            messages.success(request, "Account created successfully pls login to continue !")
            return redirect(login)
        else:
            messages.add_message(request,messages.INFO, "Password Doesn't match Pls Register again!!" ,extra_tags="danger")
    return redirect(login)

def Ulog(request):
    if request.method=="POST":
        epho=request.POST['epho']
        password=request.POST['password']   
        psw=password.encode('utf-8')
        print(psw,password,epho)
        try:
            data=User.objects.get(uphone=epho)
            ps2=data.upassword.encode('utf-8')
            print(data,ps2)
            if bcrypt.checkpw(psw,data.upassword.encode('utf-8')):
                request.session['user']=data.uname
                # messages.success(request, "Login successfully completed!") 
                return redirect(index)
            else:
                messages.add_message(request,messages.INFO, "Incorrect Password" ,extra_tags="danger")
                return redirect(login)  

        except:
            try:
                data=User.objects.get(uemail=epho)
                # print(data)
                if bcrypt.checkpw(psw,data.upassword.encode('utf-8')):
                    request.session['user']=data.uname
                    # messages.success(request, "Login successfully completed!") 
                    return redirect(index)
                else:
                    messages.add_message(request,messages.INFO, "Incorrect Password" ,extra_tags="danger")
                    return redirect(login)
            except:
                messages.add_message(request,messages.INFO, "Incorrect Email or Phonenumber!!" ,extra_tags="danger")
                return redirect(login)
            
            
