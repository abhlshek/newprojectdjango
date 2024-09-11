"""
URL configuration for quizsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('data/',views.data),
    path('abc/',views.abc),
    path('que/',views.que),
    path('cock/',views.cockwa),
    path('test/',views.test),
    path('form/',views.form),
    path('coll/',views.coll),
    path('xyz/',views.xyz),
    path('searchbooks/',views.searchbooks),
    path('searchlist/',views.searchlist),
    path('searchdic/',views.searchdic),
    path('school/',views.school),
    path("coll/",views.coll),
    path('vvv/',views.vvv),
    path('jjj/',views.jjj),
    path('results/',views.results),
    path('intro/',views.intro),
    path('cust/',views.cust),
    path('res/',views.res),
    path('shop/',views.shop),
    path('searchresult/',views.searchresult),
    path('searchintro/',views.searchintro),
    path('searchcust/',views.searchcust),
    path('searchres/',views.searchres),
    path('searchshop/',views.searchshop),
    path('bike/',views.bike),
    path('banks/',views.banks),
    path('searchbanks/',views.searchbanks),
    path('deposite/',views.deposite),
    path('deposit2/',views.deposit2),
    path('withdraw/',views.withdraw),
    path('withdraw1/',views.withdraw1)
]
