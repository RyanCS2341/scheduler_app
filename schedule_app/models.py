from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    prefix = models.CharField(max_length=100)
    course_num = models.CharField(max_length=100)
    lecture_hours = models.CharField(max_length=20)
    lab_hours = models.CharField(max_length=20)
    credit_hours = models.CharField(max_length=20)
    date = models.DateField(auto_now=False, auto_now_add=False) # change to auto-generate date

    previous_version = models.ForeignKey('self', on_delete=models.DO_NOTHING, blank=True, null=True) # change this?

    def __str__(self):
        return self.prefix.upper() + " " + self.course_num


class Term(models.Model):
    semester = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    courses = models.ManyToManyField(Course, through='Offering')

    def __str__(self):
        return self.name

    def termCourses(self):
        term_courses = self.courses.all()
        return term_courses

class Offering(models.Model):
    term = models.ForeignKey(Term, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    instructor = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.term.semester + " " + self.term.year + " - " + self.course.__str__()

class TermPermission(models.Model):
    creator = models.ForeignKey(User, on_delete = models.CASCADE)
    term = models.ForeignKey(Term, on_delete = models.CASCADE)
    # owner = boolean
