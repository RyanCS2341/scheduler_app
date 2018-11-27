from django.contrib import admin
from .models import Courses, Term, Offering

# Register your models here.
admin.site.register(Courses)
admin.site.register(Term)
admin.site.register(Offering)
