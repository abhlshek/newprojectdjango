from django.http import HttpResponse
from django.shortcuts import render


def index1(request):
    return render(request, "hello.html")


def add(request):
    result = ""
    a = 0
    b = 0
    if request.GET:
        a = int(request.GET["a1"])
        b = int(request.GET["a2"])

        result = a + b
        print(result)
    return render(request, "form.html", {"result": result, "a": a, "b": b})


def sub(request):
    result = ""
    a = 0
    b = 0
    if request.GET:
        a = int(request.GET["a1"])
        b = int(request.GET["a2"])
        result = a - b
        print(result)
    return render(request, "form.html", {"result": result, "a": a, "b": b})


def mul(request):
    result = ""
    a = 0
    b = 0
    if request.GET:
        a = int(request.GET["a1"])
        b = int(request.GET["a2"])
        result = a * b
        print(result)
    return render(request, "form.html", {"result": result, "a": a, "b": b})


def index(request):
    result = ""
    a = 0
    b = 0
    if request.GET:
        a = int(request.GET["a1"])
        b = int(request.GET["a2"])
        result = a / b
        print(result)
        return render(request, "form.html", {"result": result, "a": a, "b": b})

        return render(request, "form.html", {"result": result, "a": a, "b": b})

    return render(request, "form.html")
