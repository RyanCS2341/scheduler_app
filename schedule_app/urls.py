from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='base-view'),
    url(r'^add/', views.add, name='schedule-add-post'),
    url(r'^list/', views.courseList, name='course-list'), # returns JSON for all courses
    url(r'^addcourse/', views.addCourse, name='schedule-add'),
    url(r'^logout/', views.log, name='log-out'),
    url(r'^term/(?P<id>\d+)/$', views.term_detail, name='term-detail'),
]

# CREATE
# READ
# UPDATE
# DELETE
