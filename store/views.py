from django.shortcuts import render, redirect
from store.models import Product, Category, Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    c_di = request.GET.get('category')
    if c_di:
        products = Product.objects.filter(category=c_di)
        return render(request, 'store/index.html', {'products':products,'categories':categories})
    else:
        return render(request, 'store/index.html', {'products':products,'categories':categories})


class Login(View):
    def get(self, request):
        return render(request, 'store/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        error_message = None
        customer = None
        try:
            customer = Customer.objects.get(email=email)
        except:
            error_message = 'User does not exists!!'

        if customer:
            flag = check_password(password, customer.password)
            if flag:
                return redirect('home')
            else:
                error_message = 'Incorrect email or password!! '
        else:
            pass

        return render(request, 'store/login.html', {'error': error_message})


class Signup(View):
    def get(self, request):
        if request.method == 'GET':
            return render(request, 'store/signup.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer()
        data = {
            'first_name':first_name,
            'last_name':last_name,
            'phone':phone,
            'email':email,
        }

        if customer.isExists():
            return render(request, 'store/signup.html',{'error':'Email Already exists !!','data':data})
        password = make_password(password)

        customer = Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password)
        customer.save()
        return redirect('home')



