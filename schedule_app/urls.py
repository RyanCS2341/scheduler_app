from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="schedule-home"),
    path('schedule/', views.schedule, name="schedule-schedule"),
    path('addcourse/', views.addCourse, name='schedule-add'),
    path('removecourse/', views.removeCourse, name='schedule-remove'),
    path('courselist/', views.listCourses, name='schedule-courseList'),
    path('courses/', views.viewCourses, name='schedule-test'),
    path('add/', views.add, name='schedule-add'),
    path('search/', views.search, name='schedule-add'),
    path('list/', views.courseList, name='course-list'),
]
