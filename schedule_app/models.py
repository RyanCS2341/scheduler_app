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
