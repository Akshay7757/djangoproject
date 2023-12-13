from django.urls import path
from . import views 

urlpatterns = [


    path('', views.index, name='index'),
    # contact 
    path('contact', views.contact, name='contact'),
     # Python 
    path('python', views.python, name='python'),
    # FreshersJob 
    path('freshersjob', views.freshersjob, name='freshersjob'),
    # Experience Job 
    path('experience', views.experience, name='experience'),
    # Freshers Placement 
    path('Fplacement', views.Fplacement, name='Fplacement'),
    # Experience Placement
    path('Eplacement', views.Eplacement, name='Eplacement'),
    # Testimonial
    path('Testimonial', views.Testimonial, name='Testimonial'),
    # Drives Cyber Success
    path('DCS', views.DCS, name='DCS'),
    # Careers
    path('Careers', views.Careers, name='Careers'),
    # Clients
    path('Clients', views.Clients, name='Clients'),
    # Blogs
    path('Blogs', views.Blogs, name='Blogs'),

   

    
    
    



    
    

    

    


]