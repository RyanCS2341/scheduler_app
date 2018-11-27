from django.db import models

class Courses(models.Model):
    semester = models.TextField()
    year = models.TextField()
    prefix = models.TextField()
    course_num = models.TextField()
    hours = models.TextField()
    professor = models.TextField()

    def __str__(self):
        return self.prefix.upper() + " " + self.course_num


class Term(models.Model):
    semester = models.TextField()
    year = models.TextField()
    name = models.TextField()
    courses = models.ManyToManyField(Courses, through='Offering')

    def __str__(self):
        return self.name



class Offering(models.Model):
    term = models.ForeignKey(Term, on_delete = models.CASCADE)
    course = models.ForeignKey(Courses, on_delete = models.CASCADE)

    def __str__(self):
        return "Offerings: " + self.term.name
