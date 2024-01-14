from django.contrib import admin
from .models import Student, FirstClassRoom, SecondClassRoom, LastClassRoom

admin.site.register(Student)
admin.site.register(FirstClassRoom)
admin.site.register(SecondClassRoom)
admin.site.register(LastClassRoom)

