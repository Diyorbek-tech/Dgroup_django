from django.shortcuts import render
from .forms import homeform

def homeview(request):
    form=homeform()

    if request.method=="POST":
        name=request.POST.get('username')
        email=request.POST.get('email')

        print(name,email)
    context={
        "form":form
    }
    return render(request,'home.html',context)


