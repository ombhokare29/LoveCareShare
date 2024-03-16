from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # context = {
    #     "variable" : "made by om"
    # }
    # return HttpResponse("this is homepage")
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def joinus(request):
    return render(request, "joinus.html")
def contact(request):
    return render(request, "contact.html")
def donate(request):
    return render(request, "donate.html")
