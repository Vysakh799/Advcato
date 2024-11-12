from django.shortcuts import render,redirect
from .models import *
import bcrypt
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from itertools import zip_longest
from django.http import JsonResponse

# Create your views here.

def getuser(request):
    user=False

    if 'user' in request.session:
            user=True
    return user
def getadv(request):
    adv=False
    if 'adv' in request.session:
        adv=True
    return adv

def index(request):
    return render(request,'index.html',{'user':getuser(request),'adv':getadv(request)}) 
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
        # print(psw,password,epho)
        try:
            data=User.objects.get(uphone=epho)
            # ps2=data.upassword.encode('utf-8')
            # print(data,ps2)
            if bcrypt.checkpw(psw,data.upassword.encode('utf-8')):
                request.session['user']=data.uname
                # messages.success(request, "Login successfully completed!") 
                return redirect(User_index)
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
                    return redirect(User_index)
                else:
                    messages.add_message(request,messages.INFO, "Incorrect Password" ,extra_tags="danger")
                    return redirect(login)
            except:
                messages.add_message(request,messages.INFO, "Incorrect Email or Phonenumber!!" ,extra_tags="danger")
                return redirect(login)
    else:
        return redirect(login)

def User_logout(request):
    if getuser(request):
        del request.session['user']
        return redirect(index)
    else:
        return redirect(login)


def User_index(request):
    if getuser(request):
        user1=request.session['user']
        # print(user1)
        return render(request,'user/user_index.html',{"user":user1})
    else:
        return redirect(login)

def Advocates(request):
    if getuser(request):
        data=Advocate.objects.filter(p_status=True).order_by('aname')
        return render(request,'user/advocates.html',{'Advocates':data})
    else:
        return redirect(login)
    

def advuser_profile(request,pk):
    if getuser(request):
        adv=Advocate.objects.get(pk=pk)
        return render(request,"user/advuser_profile.html",{"adv":adv})
    else:
        return redirect(login)
def user_msg(request):
    if getuser(request):
        user=User.objects.get(uname=request.session['user'])
        advs=Chat.objects.filter(uname=user)
        anames1=[]
        for i in advs:
            anames1.append(i.aname)
        d_anames=set(anames1)
        advs=list(d_anames)
        count=[]
        for i in advs:
            data=Chat.objects.filter(aname=i,userread_status=False)
            count.append(len(data))
        advchatcount=zip_longest(advs,count)
        return render(request,'user/user_msg.html',{'advchatcount':advchatcount})
    else:
        return redirect(login)

def useradv_chat(request,pk):
    if getuser(request):
        adv=Advocate.objects.get(pk=pk)
        user=User.objects.get(uname=request.session['user'])
        msgs=Chat.objects.filter(uname=user,aname=adv)
        Chat.objects.filter(uname=user,aname=adv,advs=True).update(userread_status=True)
        if request.method=='POST':
            msg=request.POST['msg_box']
            data=Chat.objects.create(uname=user,aname=adv,messege=msg,userread_status=True)
            return redirect(reverse('useradv_chat',args=[pk]))
            # return HttpResponseRedirect(reverse('useradv_chat', args=[pk]))

        return render(request,"user/useradv_chat.html",{"adv":adv,"msgs":msgs})
    else:
        return redirect(login)
# def user_sendmsg(request,pk):
#     adv=Advocate.objects.get(pk=pk)
   
#     return redirect(useradv_chat)

#Advocates
def Adv_reg(request):
    if request.method=='POST':
        aname=request.POST['name']
        aphone=request.POST['phno']
        agender=request.POST['gender']
        aemail=request.POST['email']
        aaddress=request.POST['address'] 
        apassword=request.POST['password']
        cnf_password=request.POST['cnf_password']
        if apassword==cnf_password: 
            psw=apassword.encode('utf-8')
            salt=bcrypt.gensalt()               #Password Hashing
            psw_hashed=bcrypt.hashpw(psw,salt)
            data=Advocate.objects.create(aname=aname,aphone=aphone,agender=agender,aemail=aemail,aaddress=aaddress,apassword=psw_hashed.decode('utf-8'))
            data.save()
            messages.success(request, "Account created successfully pls login to continue !")
            return redirect(login)
        else:
            messages.add_message(request,messages.INFO, "Password Doesn't match Pls Register again!!" ,extra_tags="danger")
    return redirect(login)

def Adv_log(request):
    if request.method=='POST':
        epho=request.POST['epho']
        password=request.POST['password']   
        psw=password.encode('utf-8')
        print(psw,password,epho)
        try:
            data=Advocate.objects.get(aphone=epho)
            # print(data)
            # ps2=data.upassword.encode('utf-8')
            # print(data,ps2)
            if bcrypt.checkpw(psw,data.apassword.encode('utf-8')):
                request.session['adv']=data.aname
                print("logged in")
                if data.status:
                    return redirect(Adv_index)
                # messages.success(request, "Login successfully completed!") 
                else:
                    return redirect(Adv_reg_form)
            else:
                messages.add_message(request,messages.INFO, "Incorrect Password" ,extra_tags="danger")
                return redirect(login)  

        except:
            try:
                data=Advocate.objects.get(aemail=epho)
                if bcrypt.checkpw(psw,data.apassword.encode('utf-8')):
                    request.session['adv']=data.aname
                    print("logged in")
                    if data.status:
                        return redirect(Adv_index)
                        # messages.success(request, "Login successfully completed!") 
                    else:
                        return redirect(Adv_reg_form)
                else:
                    messages.add_message(request,messages.INFO, "Incorrect Password" ,extra_tags="danger")
                    return redirect(login) 
            except:
                messages.add_message(request,messages.INFO, "Incorrect Email or Phonenumber!!" ,extra_tags="danger")
                return redirect(login)
    else:
        return redirect(login)

def Adv_logout(request):
    if "adv" in request.session:
        del request.session['adv']
        return redirect(index)
    else:
        return redirect(login)

def Adv_index(request):
    if 'adv' in request.session:
        aname=request.session['adv']
        adv=Advocate.objects.get(aname=aname)
        if adv.status:
            return render(request,'adv/adv_index.html',{'adv':adv})
        else:
            return redirect(Adv_reg_form)
    else:
        return redirect(login)
    
def Adv_reg_form(request):
    if 'adv' in request.session:
        lang=Langauges.objects.all()
        parea=Practice_areas.objects.all()
        adv=Advocate.objects.get(aname=request.session['adv'])
        if request.method=='POST':
            bcr_no=request.POST['bcr_no']
            aheighest_qual=request.POST['aheighest_qual']
            amjtown=request.POST['amjtown']
            start_time=request.POST['start_time']
            endtime=request.POST['endtime']
            offday=request.POST['offday']
            idproof=request.FILES['idproof']
            bc_certificate=request.FILES['bc_certificate']
            exp_certificate=request.FILES['exp_certificate']
            pareas=request.POST.getlist('pareas')
            langs=request.POST.getlist('langs')
            if langs and pareas:
                for i in pareas:
                    p_area=Practice_areas.objects.get(p_area=i)
                    data=Selected_parea.objects.create(p_area_name=p_area,aname=adv)
                    data.save()
                for i in langs:
                    language=Langauges.objects.get(language=i)
                    data=Selected_lang.objects.create(aname=adv,alang=language)
                    data.save()
                data=Advocate.objects.filter(aname=request.session['adv']).update(bcr_no=bcr_no,aheighest_qual=aheighest_qual,amjtown=amjtown,start_time=start_time,end_time=endtime,off_day=offday,idproof=idproof,bc_certificate=bc_certificate,exp_certificate=exp_certificate,status=True)
                return redirect(Adv_index)
            else:
                messages.add_message(request,messages.INFO, "You missed something !!" ,extra_tags="danger")

            
        return render(request,'adv/adv_reg_form.html',{'data':parea,'lang':lang})
    else:
        return redirect(login)

def Adv_profile(request):
    if 'adv' in request.session:
        advocate=Advocate.objects.get(aname=request.session['adv'])
        return render(request,'adv/adv_profile.html',{'adv':advocate})
    else:
        return redirect(login)


def advprof_Activate(request):
    if 'adv' in request.session:
        adv=Advocate.objects.get(aname=request.session['adv'])
        advocate=Advocate.objects.filter(aname=request.session['adv']).update(p_status=True)
        return redirect(Adv_profile)
    else:
        return redirect(login)
def advprof_Deactivate(request):
    if 'adv' in request.session:
        advocate=Advocate.objects.filter(aname=request.session['adv']).update(p_status=False)
        return redirect(Adv_profile)
    else:
        return redirect(login)

def Update_prof(request):
    if 'adv' in request.session:
            advocate=Advocate.objects.get(aname=request.session['adv'])
            lang=Langauges.objects.all()
            parea=Practice_areas.objects.all()
            sparea=Selected_parea.objects.filter(aname=advocate)
            slang=Selected_lang.objects.filter(aname=advocate)
            return render(request,'adv/update_prof.html',{'adv':advocate,'data':parea,'lang':lang,'sparea':sparea,'slang':slang})
    else:
        return redirect(login)

def adv_clients(request):
    if 'adv' in request.session:
        adv=Advocate.objects.get(aname=request.session['adv'])
        users1=Chat.objects.filter(aname=adv)
        usernames=[]
        for i in users1:
            usernames.append(i.uname)
        d_usernames=set(usernames)
        users=list(d_usernames)
        return render(request,'adv/adv_clients.html',{'users':users})


def adv_msg(request):
        if 'adv' in request.session:
            adv=Advocate.objects.get(aname=request.session['adv'])
            users1=Chat.objects.filter(aname=adv)
            usernames=[]
            for i in users1:
                usernames.append(i.uname)
            d_usernames=set(usernames)
            users=list(d_usernames)
            # print(users)
            count=[]
            counts=0
            for i in users:
                data=Chat.objects.filter(uname=i,advread_status=False)
                # print(data)
                count.append(len(data))
            # print(count)    
            userchatcount=zip_longest(users,count)
            # print(userchatcount)

            return render(request,'adv/adv_msg.html',{'user_chatcount':userchatcount})

def advuser_chat(request,pk):
    if 'adv' in request.session:
        user=User.objects.get(pk=pk)
        adv=Advocate.objects.get(aname=request.session['adv'])
        msgs=Chat.objects.filter(uname=user,aname=adv)
        Chat.objects.filter(uname=user,aname=adv,advs=False).update(advread_status=True)
        if request.method=='POST':
            msg=request.POST['msg_box']
            data=Chat.objects.create(uname=user,aname=adv,messege=msg,advread_status=True,advs=True)
            return redirect(reverse('advuser_chat',args=[pk]))
        return render(request,"adv/advuser_chat.html",{'user':user,'msgs':msgs})

def user_and_caseview(request,pk):
    if 'adv' in request.session:
        user=User.objects.get(pk=pk)
        return render(request,'adv/user_and_caseview.html',{"user":user})
