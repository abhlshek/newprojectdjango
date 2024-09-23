from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index)

]

screenshort
<img width="960" alt="image" src="https://github.com/user-attachments/assets/1ef47c99-40d1-411d-9273-5b2426f3f1be">
