# from django.db import models
# from django.core.validators import MaxValueValidator

# class Student(models.Model):
#     school_year_choices = [
#         ('First_class', 'First_class'),
#         ('Second_class', 'Second_class'),
#         ('Last_class', 'Last_class')
#     ]

#     name = models.CharField(max_length=250)
#     school_year = models.CharField(max_length=50, choices=school_year_choices, default='First_class')
#     address = models.CharField(max_length=250)
#     email = models.EmailField(default=None, unique=True)
#     National_ID = models.IntegerField(
#         validators=[MaxValueValidator(99999999999999)],
#         help_text='Enter a 14-digit National ID.',
#         unique=True
#     )

#     def __str__(self) -> str:
#         return f'{self.name} - {self.school_year}'

# class FirstClassRoom(models.Model):
#     class_room_options = [
#         ('OOP', 'OOP'),
#         ('Data Structures', 'Data Structures'),
#         ('Python', 'Python'), 
#         ('Design Patterns', 'Design Patterns')
#     ] 
#     students = models.ManyToManyField(Student, related_name='first_class_rooms')
#     room = models.CharField(max_length=50, choices=class_room_options)
#     school_year = models.CharField(max_length=50, choices=Student.school_year_choices)

#     def save(self, *args, **kwargs):
#         # Check if all associated students belong to the "First_class" school year
#         if all(student.school_year == 'First_class' for student in self.students.all()):
#             super().save(*args, **kwargs)
#         else:
#             raise ValueError("All students must belong to the 'First_class' school year.")

#     def __str__(self) -> str:
#         return f'{self.room} - {self.school_year}'