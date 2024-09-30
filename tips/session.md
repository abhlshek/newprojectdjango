
<img width="960" alt="image" src="https://github.com/user-attachments/assets/d3b8dd15-3076-4409-944c-f751b4c866c3">

# session...............

def sessionset(request):
    session=request.session
    session["current"]=str(datetime.now())
    print(session["current"])
    return HttpResponse("Session Set")

def sessionremove(request):
    session=request.session
    session.pop("current")
    return HttpResponse("remove")

def sessionviews(request):
    session=request.session
    current=session.get("current")
    if current is None:
        current="none"
    return HttpResponse("session view" + current)

    <img width="960" alt="image" src="https://github.com/user-attachments/assets/271356db-9059-422e-b7ca-3d8cfaea14a8">
