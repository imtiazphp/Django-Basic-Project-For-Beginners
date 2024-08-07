from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    if(request.method=="POST"):        
      name = request.POST.get("name")
      email = request.POST.get("email")
      mobile = request.POST.get("mobile")
      subject = request.POST.get("subject")
      message = request.POST.get("message")
      contact = Contact(name=name,email=email,mobile=mobile,subject=subject,message=message,created_at=datetime.today())
      contact.save();
    messages.add_message(request, messages.SUCCESS, "Contact information has been sent successfully")

    return render(request,'contact.html')