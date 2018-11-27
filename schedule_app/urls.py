from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="schedule-home"),
    path('add/', views.add, name='schedule-add'),
    path('list/', views.courseList, name='course-list'),
    path('addcourse/', views.viewCourses, name='schedule-test'),
    path('logout/', views.log, name='log-out'),

    # USELESS
    # path('search/', views.search, name='schedule-add'),


    path('addcourse/', views.addCourse, name='schedule-add'),
    path('removecourse/', views.removeCourse, name='schedule-remove'),
    path('courselist/', views.listCourses, name='schedule-courseList'),
]
