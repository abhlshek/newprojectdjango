from django.contrib import admin
from django.shortcuts import HttpResponse,render, redirect
from django.urls import path
from . import views
from quiz.models import QuizModel,cock,Entry,Admission,PhoneBook,collage,Form,Marksheet,company,customer,Hotal,item,showroom,bank


# insert...........



def data(request):
    return HttpResponse("Hello")

def abc(request):
    book=QuizModel()
    book.question="What is the capital of China?"
    book.opta="Hukulganj"
    book.optb="Chetganj"
    book.optc="Beijing"
    book.optd="Nai Basti"
    book.correctanswer=3
    book.save()
    if request.POST:
        hello=request.POST['hello']
        print(hello)
    return render(request,'abc.html') 





    



def que(request):
    result=''
    question=''
    opta=''
    optb=''
    optc=''
    optd=''
    correctanswer=''
    if request.POST:
        q=QuizModel()
        question=request.POST['question']
        opta=request.POST["opta"]
        optb=request.POST["optb"]
        optc=request.POST["optc"]
        optd=request.POST["optd"]
        correctanswer=int(request.POST["correctanswer"])
        q.question=question
        q.opta=opta
        q.optb=optb
        q.optc=optc
        q.optd=optd
        q.correctanswer=correctanswer
        q.save()
        
    return render (request,"xyz.html",)




def test(request):
    print(request)
    return HttpResponse('hi')



def cockwa(request):
    # print("hi")
    coname=''
    price=''
    print(request)
    if request.POST:
        print("hi")
        q=cock()
        
        coname=request.POST['coname']
        price=int(request.POST['price'])
        
        q.coname= coname
        q.price= price
        q.save()
        
        
        
    return render(request,"cock.html",{"coname":coname,"price":price})    




def form(request):
    result=""
    booktitle=''
    authorname=''
    tel=''
    if request.POST:
        q=Entry()
        booktitle=request.POST["booktitle"]
        authorname=request.POST["authorname"]
        tel=int(request.POST["tel"])
        # q.booktitle=booktitle
        q.authorname=authorname
        q.tel=tel
        q.save()
        result="Saved"
    return render(request,"book.html",{"result":result,"booktitle":booktitle,"authorname":authorname,"tel":tel})


def testing(request):
    p=Entry()
    p.booktitle="kauvali"
    p.authorname="raj"
    p.tel="tel"
    p.save()
    return HttpResponse("testing")


def coll(request):
    name=""
    father=""
    mother=""
    dateofbirth=""
    male=""
    female=""
    single=""
    married=""
    presentaddress=""
    permanentaddress=""
    email=""
    sql=""
    java=""
    html=""
    python=""
    css=""
    bootstrap=""
    
    if request.POST:
        q=Admission()
        name=request.POST["name"]
        father=request.POST["father"]
        mother=request.POST["mother"]
        dateofbirth=int(request.POST["dateofbirth"])
        male=request.POST["male"]
        female=request.POST["female"]
        single=request.POST["single"]
        married=request.POST["married"]
        presentaddress=request.POST["presentaddress"]
        permanentaddress=request.POST["permanentaddress"]
        email=request.POST["email"]
        sql=request.POST["sql"]
        java=request.POST["java"]
        html=request.POST["html"]
        python=request.POST["python"]
        css=request.POST["css"]
        bootstrap=request.POST["bootstrap"]
        
        q.name=name
        q.father=father
        q.mother=mother
        q.dateofbirth=dateofbirth
        q.male=male
        q.female=female
        q.single=single
        q.married=married
        q.presentaddress=presentaddress
        q.permanentaddress=permanentaddress
        q.email=email
        q.sql=sql
        q.java=java
        q.html=html
        q.python=python
        q.css=css
        q.bootstrap=bootstrap
        
        q.save()
        return render(request,"from.html",{"name":name,"father":father,"mother":mother,"dateofbirth":dateofbirth,"male":male,"female":female,"single":single,"married":married,"presentaddress":presentaddress,"permanentaddress":permanentaddress,"email":email,"sql":sql,"java":java,"html":html,"python":python,"css":css,"bootstrap":bootstrap})
    
    
def xyz(request):
    name=''
    if request.POST:
        p=PhoneBook()
        name=request.POST["name"]
    
        p.name=name
        p.save()
    return render(request,"name.html",{"name":name})


# search........................ 



def searchbooks(request):
    name="xyz"
    data = "xxx"
    if request.GET:
        name=request.GET["name"]
        data = PhoneBook.objects.filter(name=name)
        print(name)
        print(data)
        
        
    return render(request,"search.html",{"name":name,"data":data})





def searchlist(request):
    booktitle=""
    # authorname=""
    # tel=""
    data=""
    if request.GET:
        booktitle=request.GET["booktitle"]
        # authorname=request.GET["authorname"]
        # tel=request.GET["tel"]
        
        # data=Entry.objects.filter(booktitle="python")
        data=Entry.objects.filter(booktitle=booktitle)

        
        print(booktitle)
        # print(authorname)
        # print(tel)
        print(data)
    return render(request,"mno.html",{"booktitle":booktitle,"data":data}) 




def searchdic(request):
       coname=""
       price=""
    
       data=""
       if request.GET:
           coname=request.GET["coname"]
           price=request.GET["price"]
        
        #    data=cock.objects.filter(coname="sprite")
           data=cock.objects.filter(coname=coname,price=price)

           print(coname)
           print(price)
           
           print(data)
       return render(request,"xxx.html",{"coname":coname,"price":price,"data":data})


# insert......................


def school(request):
    name=""
    cla=""
    if request.POST:
      q=collage()
      name=request.POST["name"]
      cla=request.POST["cla"]
      print(name,cla)
      q.name=name
      q.cla=cla
      q.save()
    # return HttpResponse("h")
    return render(request,"coll.html",{"name":name,"cla":cla})


# search....................


def coll(request):
    name=""
    data=""
    cla=""
    if request.GET:
        name=request.GET["name"]
        cla=request.GET["cla"]
        data=collage.objects.filter(name=name,cla=cla)
        
        print(name)
        print(data)
        print(cla)
    return render(request,"www.html",{"name":name,"data":data,"cla":cla})



#  insert..................
def vvv(request):
    name=""
    middlename=""
    lastname=""
    if request.POST:
      q=Form()
      name=request.POST["name"]
      middlename=request.POST["middlename"]
      lastname=request.POST["lastname"]
      q.name= name
      q.middlename= middlename
      q.lastname= lastname
      q.save()
    return render(request,"yyy.html",{"name":name,"middlename":middlename,"lastname":lastname})

#  search ..............
def jjj(request):
    name=""
    middlename=""
    lastname=""
    data=""
    if request.GET:
        name=request.GET["name"]
        middlename=request.GET["middlename"]
        lastname=request.GET["lastname"]
        data=Form.objects.filter(name=name,middlename=middlename,lastname=lastname)
    return render(request,"ccc.html",{"name":name,"middlename":middlename,"lastname":lastname,"data":data})

# insert ....................
def results(request):
    roll=""
    name=""
    java=""
    python=""
    c=""
    if request.POST:
       q=Marksheet()
       roll=request.POST["roll"]
       name= request.POST["name"]
       java= request.POST["java"]
       python=request.POST["python"]
       c=request.POST["c"]
       print(name,roll,java,python,c)
       q.roll=roll
       q.name=name
       q.java=java
       q.python=python
       q.c=c
    
       q.save()
    # return HttpResponse("hi")
    return render(request,"hhh.html",{"roll":roll,"name":name,"java":java,"python":python,"c":c})

def intro(request):
    name=""
    comapnyname=""
    place=""
    if request.POST:
      q=company()
      name=request.POST["name"]
      comapnyname=request.POST["comapnyname"]
      place=request.POST["place"]
      print(name,comapnyname,place)
      q.name=name
      q.comapnyname=comapnyname
      q.place=place
      q.save()
    # return HttpResponse("di")
    return render(request,"sss.html",{"name":name,"comapnyname":comapnyname,"place":place})



def cust(request):
    customername=""
    country=""
    age=""
    phone=""
    if request.POST:
        p=customer()
        customername=request.POST["customername"]
        country=request.POST["country"]
        age= request.POST["age"]
        phone=request.POST["phone"]
        print(customername,country,age,phone)
        p.customername=customername
        p.country=country
        p.age=age
        p.phone=phone
        p.save()
    # return HttpResponse("hi")
    return render(request,"customer.html",{"customername":customername,"country":country,"age":age,"phone":phone})


def res(request):
    name=""
    address=""
    city=""
    state=""
    phone=""
    email=""
    if request.POST:
      q=Hotal()
      name=request.POST["name"]
      address=request.POST["address"]
      city=request.POST["city"]
      state=request.POST["state"]
      phone=request.POST["phone"]
      email=request.POST["email"]
      q.name=name
      q.address=address
      q.city=city
      q.state=state
      q.phone=phone
      q.email=email
      q.save()
    # return HttpResponse("morning")
    return render(request,"hotal.html",{"name":name,"address":address,"city":city,"state":state,"phone":phone,"email":email})


def shop(request):
    shopname=""
    itemno=""
    itemname=""
    price=""
    place=""
    dist=""
    if request.POST:
        q=item()

        shopname=request.POST["shopname"]
        itemno=request.POST["itemno"]
        itemname=request.POST["itemname"]
        price= request.POST["price"]
        place=request.POST["place"]
        dist=request.POST["dist"]
        print(shopname,itemno,itemname,price,place,dist)
        q.shopname=shopname
        q.itemno=itemno
        q.itemname=itemname
        q.price=price
        q.place=place
        q.dist=dist
        q.save()
    return render(request,"shop.html",{"shopname":shopname,"itemno":itemno,"itemname":itemname,"price":price,"place":place,"dist":dist})



# search .....................................
def searchresult(request):
    roll=""
    name=""
    java=""
    python=""
    c=""
    data=""
    if request.GET:
        roll=request.GET["roll"]
        name=request.GET["name"]
        java=request.GET["java"]
        python=request.GET["python"]
        c=request.GET["c"]
        data=Marksheet.objects.filter(roll=roll,name=name,java=java,python=python,c=c)
    return render(request,"qqq.html",{"roll":roll,"name":name,"java":java,"python":python,"c":c,"data":data})


def searchintro(request):
    name=""
    comapnyname=""
    place=""
    data=""
    if request.GET:
        name=request.GET["name"]
        comapnyname=request.GET["comapnyname"]
        place=request.GET["place"]
        data=company.objects.filter(name=name,comapnyname=comapnyname,place=place)
        print(name,comapnyname,place)
    return render(request,"sushil.html",{"name":name,"comapnyname":comapnyname,"place":place,"data":data})



def searchcust(request):
    customername=""
    country=""
    age=""
    phone=""
    data=""
    if request.GET:
        customername=request.GET["customername"]
        country=request.GET["country"]
        age=request.GET["age"]
        phone=request.GET["phone"]
        data=customer.objects.filter(customername=customername,country=country,age=age,phone=phone)
        print(customername,country,age,phone)
    return render(request,"abhi.html",{"customername":customername,"country":country,"age":age,"phone":phone,"data":data})


def searchres(request):
    name=""
    address=""
    city=""
    state=""
    phone=""
    email=""
    data=""
    if request.GET:
        name=request.GET["name"]
        address=request.GET["address"]
        city=request.GET["city"]
        state=request.GET["state"]
        phone=request.GET["phone"]
        email=request.GET["email"]
        data=Hotal.objects.filter(name=name,address=address,city=city,state=state,phone=phone,email=email)
    return render(request,"deep.html",{"name":name,"address":address,"city":city,"state":state,"email":email,"phone":phone,"data":data})


def searchshop(request):
    shopname=""
    itemno=""
    itemname=""
    price=""
    place=""
    dist=""
    data=""
    if request.GET:
        shopname=request.GET["shopname"]
        itemno=request.GET["itemno"]
        itemname=request.GET["itemname"]
        price=request.GET["price"]
        place=request.GET["place"]
        dist=request.GET["dist"]
        data=item.objects.filter(shopname=shopname,itemno=itemno,itemname=itemname,price=price,dist=dist,place=place)
    return render(request,"raj.html",{"shopname":shopname,"itemno":itemno,"price":price,"place":place,"dist":dist,"data":data})



def bike(request):
    name=""
    brand=""
    model=""
    price=""
    email=""
    q=showroom()
    q.name="hero"
    q.brand="splender"
    q.model="2024"
    q.price="100000"
    q.email="xy@gmail.com"
    q.save()
    return HttpResponse("go")


def index(request):
    return render(request,"web.html")


def banks(request):
    account=""
    name=""
    branch=""
    balance=""
    if request.POST:
       q=bank()
       account=request.POST["account"]
       name=request.POST["name"]
       branch=request.POST["branch"]
       balance=request.POST["balance"]
       q.account=account
       q.name=name
       q.branch=branch
       q.balance=balance
       q.save()
    return render(request,"bank.html",{"account":account,"name":name,"branch":branch,"balance":balance})


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
    return render(request,"text.html")


















