from django.contrib import admin
from .models import Course, Term, Offering, TermPermission

# Register your models here.
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "course_num", "date", "previous_version"]
    list_filter = ["prefix"]
    search_fields = ["prefix"]
    class Meta:
        model = Course

class TermModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "year"]
    list_filter = ["semester"]
    search_fields = ["semester", "year"]
    class Meta:
        model = Term

class OfferingModelAdmin(admin.ModelAdmin):

    def term_semester(self, obj):
        return obj.term.semester

    list_display = ["__str__"]
    list_filter = ["term__year", "term__semester"]
    search_fields = ["term__year"]
    class Meta:
        model = Offering

admin.site.register(Course, CourseModelAdmin)
admin.site.register(Term, TermModelAdmin)
admin.site.register(Offering, OfferingModelAdmin)
admin.site.register(TermPermission)
