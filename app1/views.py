from django.shortcuts import render

# Create your views here.
def if_condition (request):
    d={'a':1000}
    return render (request,'if_condition.html',d)

def if_else (request):
    d={'a':1000,'b':150}
    return render (request,'if_else.html'd)


def if_elif_else (request):
    d={'a':1000,'b':150,'c':200}
    return render (request,'if_elif_else.html'd)