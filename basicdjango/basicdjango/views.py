from django.http import HttpResponse
from django.shortcuts import render


def twobutton(request):
    result = ""
    a = 0
    b = 0
    if request.GET:
        a = int(request.GET["a1"])
        b = int(request.GET["a2"])
        x = request.GET["x"]
        if x == "add":
            result = a + b
        if x == "sub":
            result = a - b
        if x == 'mul':
            result = a * b

    # print(a, b, x, result)
    return render(request, "button.html", {"result": result, "a": a, "b": b})


def add(request):
    result = ""
    a = 0
    b = 0
    if request.GET:
        a = int(request.GET["a1"])
        b = int(request.GET["a2"])

        result = a + b
        print(result)
    return render(request, "button.html", {"result": result, "a": a, "b": b})


def sub(request):
    result = ""
    a = 0
    b = 0
    if request.GET:
        a = int(request.GET["a1"])
        b = int(request.GET["a2"])
        result = a - b
        print(result)
    return render(request, "button.html", {"result": result, "a": a, "b": b})


def index(request):
    return render(request, 'hello.html')


def mul(request):
    result = ""
    a = 0
    b = 0
    if request.GET:
        a = int(request.GET["a1"])
        b = int(request.GET["a2"])
        result = a * b
        print(result)
    return render(request, "button.html", {"result": result, "a": a, "b": b})


def radio(request):
    result = ""
    a = 0
    b = 0
    if request.GET:
        a = int(request.GET["a1"])
        b = int(request.GET["a2"])
        x = request.GET["radio"]
        if x == "add":
            result = a + b
        if x == "sub":
            result = a - b

    return render(request, "radio.html", {"result": result, "a": a, "b": b})


def select(request):
    result = ""
    a = 0
    b = 0
    if request.GET:
        a = int(request.GET["a1"])
        b = int(request.GET["a2"])
        x = request.GET["select"]
        if x == "add":
            result = a + b
        if x == "sub":
            result = a - b

    return render(request, "select.html", {"result": result, "a": a, "b": b})


def checkbox(request):
    result = ""
    a = 0
    b = 0
    if request.GET:
        a = int(request.GET["a1"])
        b = int(request.GET["a2"])
        x = request.GET["checkbox"]
        if x == "add":
            result = a + b
        if x == "sub":
            result = a - b

    return render(request, "checkbox.html", {"result": result, "a": a, "b": b})


def facebook(request):
    result = ""
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    if request.GET:
        a = int(request.GET["fname"])
        b = int(request.GET["lname"])
        c = int(request.GET["phone email"])
        d = int(request.GET["password"])
        e = int(request.GET["date of birth"])
        f = int(request.GET["mail"])
        g = int(request.GET["femail"])
        h = int(request.GET["checkbox"])
        i = int(request.GET["custom"])
        j = int(request.GET["checkbox"])
        x = request.GET["facebook"]

    return render(request, "facebook.html",
                  {"result": result, "a": a, "b": b, "c": c, "d": d, "e": e, "f": f, "g": g, "h": h, "i": i, "j": j})


def collage(request):
    firstname = ""
    middlename = ""
    lastname = ""
    day = ""
    checkbox = ""
    tel = ""
    email = ""
    address = ""
    city = ""
    state = ""
    a = ""
    radio = ""

    if request.GET:
        firstname = request.GET["fname"]
        middlename = request.GET["mname"]
        lastname = request.GET["lname"]

        day = request.GET["day"]
        checkbox = request.GET["checkbox"]
        tel = request.GET["tel"]
        email = request.GET["email"]
        address = request.GET["address"]
        city = request.GET["city"]
        state = request.GET["state"]
        a = int(request.GET["a1"])
        radio = request.GET["radio"]

    print(firstname)
    print(middlename)
    print(lastname)
    print(day)
    print(tel)
    print(email)
    print(address)
    print(city)
    print(state)

    return render(request, "collage.html",
                  {"firstname": firstname, "middlename": middlename, "lastname": lastname, "day": day,
                   "checkbox": checkbox, "tel": tel, "email": email, "address": address, "city": city, "state": state,
                   "a": a, "radio": radio})


def post(request):
    result = ""
    a = 0
    b = 0
    if request.POST:
        a = int(request.POST["a1"])
        b = int(request.POST["a2"])
        x = request.POST["post"]
        if x == "add":
            result = a + b
            print(result)

    return render(request, "post.html", {"result": result, "a": a, "b": b})


def book(request):
    booktitle = ""
    publishplace = ""
    fname = ""
    lname = ""
    pageno = ""
    address = ""
    city = ""
    region = ""
    phone = ""
    bookname = ""
    subject = ""
    price = ""
    if request.POST:
        booktitle = request.POST["booktitle"]
        publishplace = request.POST["publishplace"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        pageno = int(request.POST["pageno"])
        address = request.POST["address"]
        city = request.POST["city"]
        region = request.POST["region"]
        phone = int(request.POST["phone"])
        bookname = request.POST["bookname"]
        subject = request.POST["subject"]
        price = request.POST["price"]

    print(booktitle)
    print(publishplace)
    print(fname)
    print(lname)
    print(pageno)
    print(address)
    print(city)
    print(region)
    print(phone)
    print(bookname)
    print(subject)
    print(price)
    return render(request, "book.html", )


def laptop(request):
    hp = ""
    lenovo = ""
    ibm = ""
    if request.POST:
        hp = request.POST["hp"]
        lenovo = request.POST["lenovo"]
        ibm = request.POST["ibm"]
    print(hp)
    print(lenovo)
    print(ibm)

    return render(request, "laptop.html", {"hp": hp, "lenovo": lenovo, "ibm": ibm})


def roll(request):
    result = 'even'
    if request.POST:
        num = int(request.POST['num'])

        if num % 2 == 0:
            print("pass")
        else:
            print("fail")
    return render(request, "roll.html", {"result": result})
