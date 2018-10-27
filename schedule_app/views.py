from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import os
import json

def home(request):
    return render(request, 'schedule_app/home.html')

@login_required
def schedule(request):
    return render(request, 'schedule_app/schedule.html')

def addCourse(request):
    dataFile = 'schedule_app/templates/schedule_app/text_files/data.txt'
    idFile = 'schedule_app/templates/schedule_app/text_files/nextid.txt'
    semester = request.GET['semester']
    year = request.GET['year']
    prefix = request.GET['prefix']
    number = str(request.GET['num'])

    with open(dataFile, 'r') as data, open(idFile, 'r') as num:
        id = int(num.readline()) + 1
        stuff = json.load(data)
        stuff.append( { "id" : id, "prefix" : prefix, "number" : number, "sem" : semester, "year" : year } )
    with open(dataFile, 'w') as data, open(idFile, 'w') as num:
         json.dump(stuff, data)
         num.write(str(id))
    return render(request, 'schedule_app/text_files/data.txt')

def removeCourse(request):
    dataFile = 'schedule_app/templates/schedule_app/text_files/data.txt'
    idFile = 'schedule_app/templates/schedule_app/text_files/nextid.txt'
    semester = request.GET['semester']
    year = request.GET['year']
    prefix = request.GET['prefix']
    number = str(request.GET['num'])

    with open(dataFile, 'r') as data:
        information = json.load(data)
        for i in reversed(information):
            if (i["prefix"] == prefix and i["number"] == number):
                information.remove(i)
    with open(dataFile, 'w') as data:
        json.dump(information, data)

    return render(request, 'schedule_app/text_files/data.txt')


def listCourses(request):
    return render(request, 'schedule_app/text_files/data.txt')
