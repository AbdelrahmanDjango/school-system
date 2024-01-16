from django.contrib import admin
from .models import Student, FirstClassRoom, SecondClassRoom, LastClassRoom

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'email', 'National_ID', 'approval_status']
    list_filter = ['approval_status']

admin.site.register(FirstClassRoom)
admin.site.register(SecondClassRoom)
admin.site.register(LastClassRoom)

