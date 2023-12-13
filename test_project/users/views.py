from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User

def index(request):
    template = loader.get_template("index.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))

#  Python Course
def python(request):
    template = loader.get_template("python.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))

#  Fresher Jobs
def freshersjob(request):
    template = loader.get_template("news-single.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))

#  Experience Jobs
def experience(request):
    template = loader.get_template("experence.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))

#Fresher Placement
def Fplacement(request):
    template = loader.get_template("fplace.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))   

#Experience Placement
def Eplacement(request):
    template = loader.get_template("eplace.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))

#Testimonials  
                    
def Testimonial(request):
    template = loader.get_template("tens.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))

#Driver Cyber Success
def DCS(request):
    template = loader.get_template("campus.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))

# Careers       
def Careers(request):
    template = loader.get_template("about.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))

# Clients   
def Clients(request):
    template = loader.get_template("clients.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))

# Blogs
def Blogs(request):
    template = loader.get_template("blog.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))


#  Contact
def contact(request):
    template = loader.get_template("contact.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))