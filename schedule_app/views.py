from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
import os
import json
from .models import Course, Term
from django.contrib.auth import logout
dataFile = 'schedule_app/templates/schedule_app/text_files/data.txt'

def home(request):
    terms = Term.objects.all()
    context = {
        "terms" : terms
    }
    return render(request, 'schedule_app/base.html', context)

def term_detail(request, id=None):
    terms = Term.objects.all()
    instance = get_object_or_404(Term, id=id)
    context = {
        "name" : instance.courses.all(),
        "terms" : terms
    }
    return render(request, 'schedule_app/term.html', context)


def addCourse(request):
    return render(request, 'schedule_app/courses.html') #,{'all_courses': all_courses})

def add(request):
    if (request.method == "POST"):
        semester = request.POST['semester'].lower();
        year = request.POST['year']
        prefix = request.POST['prefix'].lower();
        course_num = request.POST['course_num']
        hours = request.POST['hours']
        professor = request.POST['professor'].lower();

        new_course = Course.objects.create(semester=semester,year=year,prefix=prefix,course_num=course_num,
                            hours=hours, professor=professor)
        return HttpResponseRedirect('/courses/')
    else:
        return HttpResponseRedirect('/')

# returns JSON for Course objects
def courseList(request):
    courses = Course.objects.all()
    course_json = [{"prefix":c.prefix, "number":c.course_num, "lecture":c.lecture_hours, "lab":c.lab_hours, "credit":c.credit_hours} for c in courses]
    # print(json.dumps(course_json))
    return HttpResponse(json.dumps(course_json), content_type='application/json')

def log(request):
    logout(request)
    return HttpResponseRedirect('/')

    # def search(request):
    #     if (request.method == "POST"):
    #         prefix = request.POST['prefix']
    #         relevant = []
    #         all_courses = Courses.objects.all()
    #         for course in all_courses:
    #             if (course.prefix == prefix):
    #                 relevant.append(course)
    #         return render(request, 'schedule_app/home.html', {'relevant': relevant})
    #     else:
    #         return HttpResponseRedirect('/')
