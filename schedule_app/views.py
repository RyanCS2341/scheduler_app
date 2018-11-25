from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
import os
import json
from .models import Courses
dataFile = 'schedule_app/templates/schedule_app/text_files/data.txt'

def home(request):
    return render(request, 'schedule_app/search.html')

@login_required
def schedule(request):
    return render(request, 'schedule_app/schedule.html')


def getQueryParam(request, name, pattern = False):
    value = request.GET[name]
    #if pattern:
        # check value matches pattern
        # if violates ... error ...
    return value

def addCourse(request):
    # dataFile = 'schedule_app/templates/schedule_app/text_files/data.txt'
    idFile = 'schedule_app/templates/schedule_app/text_files/nextid.txt'
    semester = request.GET['semester']
    #year = request.GET['year']
    year = getQueryParam(request, 'year', '\\d{2}|\\d{4}')
    prefix = request.GET['prefix']
    number = str(request.GET['num'])

    ## regular expressions

    with open(dataFile, 'r') as data, open(idFile, 'r') as num:
        id = int(num.readline()) + 1
        stuff = json.load(data)
        stuff.append( { "id" : id, "prefix" : prefix, "number" : number, "sem" : semester, "year" : year } )
    with open(dataFile, 'w') as data, open(idFile, 'w') as num:
         json.dump(stuff, data)
         num.write(str(id))
    return render(request, 'schedule_app/text_files/data.txt')

def removeCourse(request):
    # dataFile = 'schedule_app/templates/schedule_app/text_files/data.txt'
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

def viewCourses(request):
    all_courses = Courses.objects.all()
    return render(request, 'schedule_app/courses.html',
            {'all_courses': all_courses})

def add(request):
    if (request.method == "POST"):
        semester = request.POST['semester'].lower();
        year = request.POST['year']
        prefix = request.POST['prefix'].lower();
        course_num = request.POST['course_num']
        hours = request.POST['hours']
        professor = request.POST['professor'].lower();

        new_course = Courses.objects.create(semester=semester,year=year,prefix=prefix,course_num=course_num,
                            hours=hours, professor=professor)
        return HttpResponseRedirect('/courses/')
    else:
        return HttpResponseRedirect('/')

def courseList(request):
    courses = Courses.objects.all()
    course_json = [{"semester":c.semester, "year":c.year, "prefix":c.prefix, "number":c.course_num, "hours":c.hours, "professor":c.professor} for c in courses]
    # print(json.dumps(course_json))
    return HttpResponse(json.dumps(course_json), content_type='application/json')

def search(request):
    if (request.method == "POST"):
        prefix = request.POST['prefix']
        relevant = []
        all_courses = Courses.objects.all()
        for course in all_courses:
            if (course.prefix == prefix):
                relevant.append(course)
        return render(request, 'schedule_app/home.html', {'relevant': relevant})
    else:
        return HttpResponseRedirect('/')
