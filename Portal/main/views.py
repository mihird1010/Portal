from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from Portal.main.models import *
import json

def schemelist(request):
	no=request.GET.get('category')
	resp={}
	t=[]	
	schemeList=Scheme.objects.all()
	for i in schemeList:
		if no in i.categories.split(','):
			temp={}			
			temp['no']=(i.number)
			temp['name']=(i.name)
			t.append(temp)
			print("ccccccc")
	resp['schemes']=t
	data=json.dumps(resp,indent=4)
	return HttpResponse(data,content_type='json')

def getscheme(request):
	no=request.GET.get('scheme_number')
	scheme=Scheme.objects.get(number=no)
	response={}
	resp={}
	resp['name']=scheme.name
	resp['state']=scheme.state
	resp['duration']=scheme.duration
	resp['qualification']=scheme.qualification
	resp['income_per_annum']=scheme.income_per_annum
	resp['caste']=scheme.caste
	resp['physically_handicapped']=scheme.physically_handicapped
	resp['gender']=scheme.gender
	resp['age']=scheme.age
	resp['occupation']=scheme.occupation
	response['schemes']=resp
	data=json.dumps(response,indent=4)
	return HttpResponse(data,content_type='json')

def getcategories(request):
	allschemes=Scheme.objects.all()
	categories=[]
	resp={}
	for i in allschemes:
		schemcats=i.categories.split(',')
		for j in schemcats:
			if j not in categories:
				categories.append(j)
	resp['all_categories']=categories
	data=json.dumps(resp,indent=4)
	return HttpResponse(data,content_type='json')
