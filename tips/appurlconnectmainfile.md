
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('medical/',include('medicalshop.urls')),
     

]

mainfile screenshort
<img width="960" alt="image" src="https://github.com/user-attachments/assets/bcd37358-f35e-4f05-b330-5f2f47f4198e">
appfile screenshort
<img width="960" alt="image" src="https://github.com/user-attachments/assets/cb8c07a6-848a-400e-ac36-68e6cc332fde">

notescreenshort
<img width="960" alt="image" src="https://github.com/user-attachments/assets/fe37c9d6-a46a-42ee-b721-10c96296df03">


