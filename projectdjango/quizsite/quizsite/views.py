from django.contrib import admin
from django.shortcuts import HttpResponse,render, redirect
from django.urls import path
from . import views
from quiz.models import QuizModel,cock,Entry,Admission,PhoneBook,collage,Form,Marksheet,company,customer,Hotal,item,showroom,bank


# insert...........



def index(request):
    return render(request,"base.html")


def banks(request):
    account=""
    name=""
    branch=""
    balance=""
    if request.POST:
        account=request.POST["account"]
        name=request.POST["name"]
        branch=request.POST["branch"]
        balance=request.POST["balance"]
        q=bank()
        print(account)
        print(name)
        print(branch)
        print(balance)
        q.name= name
        q.account= account
        q.branch=branch
        q.balance=balance
        q.save()
    # return HttpResponse("he")
    return render(request,"bank.html",{"account":account,"name":name,"branch":branch,"balance":balance})

    
    # return HttpResponse("Banks")
    # if request.POST:
       
    #    account=int(request.POST["account"])
    #    name=request.POST["name"]
    #    branch=request.POST["branch"]
    #    balance=int(request.POST["balance"])
    #    q.account=account
    #    q.name=name
    #    q.branch=branch
    #    q.balance=balance
    #    q.save()


def searchbanks(request):
    account=""
    data=""
    result=""
    acc=""
    display="none"

    if request.GET:
        account=request.GET["account"]
        data=bank.objects.filter(account=account)
        # print(data)
        # print(data.count)
        print(data.count())
        x=data.count()
        if x==0:
            result="Not Found"
        else:
            result="Found"
            display="block"
            acc=data.get()
            print(acc)
            print(acc.name)
            print(acc.balance)
            print(acc.branch)
            
        

    return render(request,"searchbank.html",{"account":account,"data":acc,"result":result,"display":display})


def deposite(request):
    account=""
    # balance=""
    result=""
    
    acc=""
    display="none"
    if request.GET:
        
        account=int(request.GET["account"])
        # balance=int(request.GET["balance"])
        print(account)
        data=bank.objects.filter(account=account)
        print(data.count())
        x=data.count()
        if x==0:
            result="Not Found"
        else:
            result="Found"
            display="block"
            acc=data.get()
            print(acc)
            print(acc.name)
            print(acc.balance)
            print(acc.branch)
            
    return render(request,"depo.html",{"account":account,"data":acc,"result":result,"display":display})


def deposit2(request):
    account=""
    result=""
    if request.GET:
        account=request.GET["account"]
        balance=int(request.GET["balance"])
        data=bank.objects.filter(account=account)
        print(account)
        print(data)
        x=data.count()
        if x>0:
            acc=data.get()
            if balance<=0:
                result="not "
            else:
                acc.balance+=balance
                acc.save()
                result="success"
    
    return HttpResponse(result)


def withdraw(request):
    account=""
    balance=""
    result=""
    
    acc=""
    display="none"
    if request.GET:
        
        account=int(request.GET["account"])
        print(account,balance)
        data=bank.objects.filter(account=account)
        print(data.count())
        x=data.count()
        if x==0:
            result="Not Found"
        else:
            result="Found"
            display="block"
            acc=data.get()
            print(acc)
            print(acc.name)
            print(acc.balance)
            print(acc.branch)
            
    return render(request,"withdraw.html",{"account":account,"data":acc,"result":result,"display":display})

    


def withdraw1(request):
    account=""
    result=""
    if request .GET:
        account=request.GET["account"]
        balance=int(request.GET["balance"])
        data=bank.objects.filter(account=account)
        print(data)
        print(account)
        x=data.count()
        if x>0:
            acc=data.get()
            if acc.balance<balance or balance<=0:
                result="Insufficient amount"
            else:
                
                acc.balance-=balance
                acc.save()
                result="Success"

    return HttpResponse(result)





# .................
def base(request):
    return render(request,"inherit.html")


















