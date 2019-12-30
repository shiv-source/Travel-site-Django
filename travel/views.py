from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):


    dest1= Destination()
    dest1.name='Mumbai'
    dest1.price=500
    dest1.desc='Mumbai is the Biggest Financial Hub in India.'
    dest1.img= 'destination_1.jpg'
    dest1.offer= True


    dest2= Destination()
    dest2.name='Chandigrh'
    dest2.price=600
    dest2.desc='Place of Peace and Entertenment.'
    dest2.offer= False
    dest2.img='destination_2.jpg'

    
    dest3= Destination()
    dest3.name='Mohali'
    dest3.price=700
    dest3.desc='Mohali is the place where i live'
    dest3.img= 'destination_3.jpg'
    dest3.offer= True

    
    dest4= Destination()
    dest4.name='Gunupur'
    dest4.price=800
    dest4.desc='GIET UNIVERSITY'
    dest4.img= 'destination_4.jpg'
    dest4.offer= True

    
    dest5= Destination()
    dest5.name='Bhagalpur'
    dest5.price=900
    dest5.desc='My home town'
    dest5.img= 'destination_5.jpg'
    dest5.offer= True

    dests=[dest1,dest2,dest3,dest4,dest5]

    return render(request,'index.html',{'dests':dests})
