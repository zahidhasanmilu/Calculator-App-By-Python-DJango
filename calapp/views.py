from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def calculator(request):
    # try:
    #     c = ''
    #     num1 = ''
    #     num2 = ''
    #     operator = ''
    #     if request.method == 'POST':
    #         num1 =eval(request.POST.get('number1'))
    #         num2 = eval(request.POST.get('number2'))
    #         operator = request.POST.get('operator')
            
            
    #         if operator == '+':
    #             c = num1 + num2
    #         if operator == '-':
    #             c = num1 - num2
    #         if operator ==  '*':
    #             c = num1 * num2
    #         if operator ==  '/':
    #             c = num1 / num2
           
    # except:
    #     c = 'invalid Operator'
    # return render(request,'index.html', context={'c': c, 'num1':num1, 'num2':num2, 'operator':operator})
    if request.method =='POST':
        num1 = eval(request.POST.get('number1'))
        num2 = eval(request.POST.get('number2'))
        operator = request.POST.get('operator')
        if operator == '+':
            c = num1+num2
        elif operator == '-':
            c = num1-num2
        elif operator == '*':
            c = num1*num2
        elif operator == '/':
            c = num1/num2
        else:
            c = 'invalid Operator'
        return render(request,'index.html', context={'c': c, 'num1':num1, 'num2':num2, 'operator':operator})
    return render(request,'index.html')


def intslug(request, a, b):
    return HttpResponse("Hello Int slug ", a+b)

def strslug(request, x, y):
    return HttpResponse(x+y)

def justslug(request,x,y,z):
    return HttpResponse(x+y+z)