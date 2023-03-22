from django.http import HttpResponse

def aboutus(request):
    return HttpResponse("Hello Anurag")

def course(request):
    return HttpResponse("<b>Contact-Us :- anurag.itmatters@gmail.com</b>")

def mobile(request):
    return HttpResponse("<u><b>My mobile number is : 8595848097</b></u>")

