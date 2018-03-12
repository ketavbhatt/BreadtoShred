# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout


from django.http import JsonResponse
import requests

from email.MIMEMultipart import MIMEMultipart
from .safe import usermail,upassword
from email.MIMEText import MIMEText
import smtplib



# Create your views here.


def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		weight = float(request.POST['weight'])
		height = float(request.POST['height'])

		bmi = float(weight/(height*height))

		

		
		
		user = User.objects.create(username=username,email=email)
		user.set_password(password)
		
		user.save()

		if(bmi<18.5):
			user_cal = user_calorie.objects.create(user=user,food_cal=0,exe_cal=0,rem_cal=3020,goal_cal=3020)
			user_cal.save()
		elif(bmi>=18.5 and bmi<24.9):
			user_cal = user_calorie.objects.create(user=user,food_cal=0,exe_cal=0,rem_cal=2600,goal_cal=2600)
			user_cal.save()
		elif(bmi>=24.9 and bmi<29.9):
			user_cal = user_calorie.objects.create(user=user,food_cal=0,exe_cal=0,rem_cal=2190,goal_cal=2190)
			user_cal.save()
		elif(bmi>=29.9 and bmi<34.9):
			user_cal = user_calorie.objects.create(user=user,food_cal=0,exe_cal=0,rem_cal=1950,goal_cal=1950)
			user_cal.save()
		
		return render(request,"login.html")
	else:

		return render(request,"login.html")




def login_site(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		print("asdasd")
		print(username)
		print(password)
		print(user)
		if user:
			print("asas")
			login(request, user)
			return render(request,'index.html')
		else:
			return HttpResponse('invalid')

	else:	
		return render(request, 'login.html')

def logout(request):
    if request.user.is_authenticated():
        auth_logout(request)
    else:
        return HttpResponse("invalid")
   
    return render(request, 'login.html')



def about(request):

	return render(request,'about.html')

def gallery(request):
	return render(request,'gallery.html')

def calorie(request):
	if request.method == 'POST':
		calorie = json.loads(request.body.decode('utf-8'))
		goal = calorie['goal']
		food = calorie['food']
		exercise = calorie['exercise']
		remaining = calorie['remaining']
		
		user_calorie.objects.filter(user=request.user).update(food_cal=food,exe_cal=exercise,rem_cal=remaining,goal_cal=goal)
		user_cal = user_calorie.objects.get(user=request.user)
		food = Food.objects.all()
		exercise = Exercise.objects.all()
		return JsonResponse({'success' : 'true'})
		


	else:
		food = Food.objects.all()
		exercise = Exercise.objects.all()
		user_cal = user_calorie.objects.get(user=request.user)
		return render(request,"calorie.html",{'food' : food, 'exercise' : exercise, 'user_cal' : user_cal})


def home(request):
	return render(request,"index.html")
	

def blog(request):
	if request.method != 'POST':
		return render(request,"codes.html")
	if request.method == 'POST':
		name = request.POST['Name']
		email = request.POST['Email']
		message = request.POST['Message']
		fromaddr=usermail
        toaddr=usermail
        print fromaddr
        print toaddr
        msg=MIMEMultipart()
        msg['From']=fromaddr
        msg['To']=toaddr
        msg['Subject']='Feedback Email'
        domain = request.get_host()
        scheme = request.is_secure() and "https" or "http"
        body = "Name: {0} \n Email: {1} \n Message: {2}".format(name,email,message) 
        part1 = MIMEText(body, 'plain')
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, upassword)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        return render(request,'codes.html')






		

    


