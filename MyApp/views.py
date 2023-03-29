from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib import messages
import pandas as pd
from sklearn.linear_model import LinearRegression
from MyApp.models import userinput

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def predict(request):
    return render(request,'predict.html')

def landing(request):
    return render(request,'landing.html')

def login(request):
    if request.method == "POST":
        uname=request.POST['loguser']
        pass1=request.POST['lpass'].lower()
        user = authenticate(username=uname, password=pass1)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Invalid Credentials")
            return render(request, "login.html")
    return render(request,'login.html')

def register(request):
    if request.method=="POST":
        username = (request.POST['user']).lower()
        fname = request.POST['fname'].lower()
        lname = request.POST['lname'].lower()
        email = request.POST['email']
        passwd = request.POST['pass']
        con_passwd = request.POST['confirm_pass']
            
        if passwd==con_passwd:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists!")
                return render(request, "register.html")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists!")
                return render(request, "register.html")
            else:
                user = User.objects.create_user(username=username, first_name=fname,
                last_name=lname, email=email, password=passwd)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Password's do not match!")
            return render(request,"register.html")
    else:
        return render(request, "register.html")
    
    # return render(request,'register.html')

def predictsales(request):
    if request.method == 'POST':
        retailer=int(request.POST.get('retailer'))
        region=int(request.POST.get('region'))
        state=int(request.POST.get('state'))
        city=int(request.POST.get('city'))
        product=int(request.POST.get('product'))
        method=int(request.POST.get('method'))
        priceperunit=int(request.POST['priceperunit'])
        unitssold=int(request.POST['unitssold'])
        operatingprofit=int(request.POST['operatingprofit'])
        operatingmargin=float(request.POST['operatingmargin'])

        data = pd.read_csv(r"static/dataset/sample.csv")
        
        X_train = data[['Retailer',	'Region',	'State',	'City',	'Product'	,'Price per Unit',	'Units Sold',	'Operating Profit',	'Operating Margin',	'Method']]
        Y_train = data[['Total Sales']]

        lr = LinearRegression()
        lr.fit(X_train, Y_train)
        
        prediction_result = lr.predict([[retailer,region,state,city,product,priceperunit,unitssold,operatingprofit,operatingmargin,method]])

        predict = userinput.objects.create(retailer = retailer, region = region, state = state, city = city, product = product, method = method, priceperunit = priceperunit, unitssold = unitssold, operatingprofit = operatingprofit, operatingmargin = operatingmargin)
        predict.save()
        return render(request, "inputs.html", {"Prediction":prediction_result, "retailer" : retailer, "region" : region, "state" : state, "city" : city, "product" : product, "method" : method, "priceperunit" : priceperunit, "unitssold" : unitssold, "operatingprofit" : operatingprofit, "operatingmargin" : operatingmargin})