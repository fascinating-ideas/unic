from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect,request
from application.forms import UserForm
from project import settings  
from django.core.mail import send_mail  
import random
import email as em
# Create your views here.

def first(request):
    return render(request,"firstpage.html")
def second(request):
    return render(request,"loginpage.html")
def home(request):
    a=request.get["Username"]
    b=request.get["pass"]
    if a=="admin" and b=="admin.123":
        msg="Welcome admin"
        return render(request,"adminpage.html",{'message':msg}) 
    else:    
        use=UserForm()
        return render(request,"/home1",{'form':use})   
def third(request):
    return render(request,"singuppage.html")
def mail(request):
    a=print(random.randrange(1,10000))
    em.open("compose=new") 
    subject = "confrimation code from Train books"  
    msg     = a 
    to      = "sujithsn1570@gmail.com"  
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
    if(res == 1):  
        msg = "Mail Sent Successfuly"  
    else:  
        msg = "Mail could not sent"  
    return HttpResponse(msg) 
    return render(request,"forgetpassword.html")  
def book(request):
    return render(request,"ticketbooking.html")
def contact(request):
    return render(request,"contact.html")
def admin(request):
    return render(request,"adminpage.html")    
def home1(request):
    return render(request,"homepage.html")
def train(request):
    url="http://indianrailapi.com/api/v2/TrainSchedule/apikey/<apikey>/TrainNumber/<TrainNumber>/"      
    resoponse = request.GET(url)
    data = response.json()["data"]
    print(data)
    return render(request,"traintabel.html")
