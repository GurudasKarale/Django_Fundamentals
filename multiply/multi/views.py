from django.shortcuts import render

def home(request):
    return render(request,"index.html",{'multiplier':'Multiplier'})


def calculate(request):

    val1= request.GET['num1']
    val2= request.GET['num2']

    res=int(val1) * int(val2)
    return render(request,"index.html",{'multiplier':'Multiplier','result':res})

