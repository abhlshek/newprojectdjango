from django.contrib import admin
from django.shortcuts import HttpResponse,render, redirect
from django.urls import path
from . import views
from quiz.models import QuizModel,cock,Entry,Admission,PhoneBook


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

def index(request):
    return HttpResponse("Home")


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
    authorname=""
    tel=""
    data=""
    if request.GET:
        booktitle=request.GET["booktitle"]
        authorname=request.GET["authorname"]
        tel=request.GET["tel"]
        
        data=Entry.objects.filter(booktitle=booktitle,authorname=authorname,tel=tel)
        
        print(booktitle)
        print(authorname)
        print(tel)
        print(data)
    return render(request,"mno.html",{"booktitle":booktitle,"authorname":authorname,"data":data,"tel":tel}) 




def searchdic(request):
       coname=""
       price=""
       data=""
       if request.GET:
           coname=request.GET["coname"]
           price=request.GET["price"]
           data=cock.objects.filter(coname=coname,price=price)
           print(coname)
           print(price)
           print(data)
       return render(request,"xxx.html",{"coname":coname,"price":price,"data":data})   

