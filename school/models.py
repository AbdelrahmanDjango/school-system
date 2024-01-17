from django.db import models
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
# from taggit.managers import TaggableManager
from django.db.models.query import QuerySet

class ApprovedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(approved_status=Student.Status.APPROVED)
class ApprovedManagerFirst(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(approved_status=FirstClassRoom.Status.APPROVED)
class ApprovedManagerSecond(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(approved_status=SecondClassRoom.Status.APPROVED)
class ApprovedManagerLast(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(approved_status=LastClassRoom.Status.APPROVED)

class Student(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PD', 'Pending'
        REJECTED = 'RJ', 'Rejected'
        APPROVED = 'AP', 'Approved'


    SCHOOL_YEAR_CHOICES = [
        ('First_class', 'First_class'),
        ('Second_class', 'Second_class'),
        ('Last_class', 'Last_class')
    ]

    name = models.CharField(max_length=250)
    school_year = models.CharField(max_length=50, choices=SCHOOL_YEAR_CHOICES, default='First_class')
    address = models.CharField(max_length=250)
    email = models.EmailField(default=None, unique=True)
    approval_status = models.CharField(max_length=50, choices= Status.choices, default=Status.PENDING)
    National_ID = models.IntegerField(
        validators=[MaxValueValidator(99999999999999)],
        help_text='Enter a 14-digit National ID.',
        unique=True
    )
    objects = models.Manager()
    approved_students = ApprovedManager()
    
    def __str__(self) -> str:
        return f'{self.name} - {self.school_year}'


class FirstClassRoom(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PD', 'Pending'
        REJECTED = 'RJ', 'Rejected'
        APPROVED = 'AP', 'Approved'

    class_room_options = [
        ('Operating System', 'Operating System'),
        ('Data Structures', 'Data Structures'),
        ('Design Patterns', 'Design Patterns'),
        ('C++', 'C++'), 
    ] 
    students = models.ManyToManyField(Student, related_name='first_class_rooms')
    room = models.CharField(max_length=50, choices=class_room_options)
    school_year = models.CharField(max_length=50, choices=Student.SCHOOL_YEAR_CHOICES)
    approval_status = models.CharField(max_length=50, choices= Status.choices, default=Status.PENDING)

    objects = models.Manager()
    approved_students = ApprovedManagerFirst()
    def __str__(self):
        return "%s (%s)" % (
            self.room,
            ", ".join(student.name for student in self.students.all()),
        )

@receiver(m2m_changed, sender=FirstClassRoom.students.through)
def limit_students_to_first_class(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == 'pre_add' and not reverse:
        # Check if any student in the pk_set is not from the 'First_class'
        students_not_in_first_class = Student.objects.filter(pk__in=pk_set, school_year='First_class')
        if students_not_in_first_class.count() != len(pk_set):
            raise ValidationError(f"All students must belong to the 'First_class' school year. Students not in 'First_class': {students_not_in_first_class}.")

class SecondClassRoom(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PD', 'Pending'
        REJECTED = 'RJ', 'Rejected'
        APPROVED = 'AP', 'Approved'

    class_room_options = [
        ('OOP', 'OOP'),
        ('Data Structures', 'Data Structures'),
        ('Python', 'Python'), 
        ('Network', 'Network')
    ] 
    students = models.ManyToManyField(Student, related_name='second_class_rooms')
    room = models.CharField(max_length=50, choices=class_room_options)
    school_year = models.CharField(max_length=50, choices=Student.SCHOOL_YEAR_CHOICES)
    approval_status = models.CharField(max_length=50, choices= Status.choices, default=Status.PENDING)

    objects = models.Manager()
    approved_students = ApprovedManagerSecond()

    def __str__(self):
        return "%s (%s)" % (
            self.room,
            ", ".join(student.name for student in self.students.all()),
        )
    
@receiver(m2m_changed, sender=SecondClassRoom.students.through)
def limit_students_to_second_class(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == 'pre_add' and not reverse:
        # Check if any student in the pk_set is not from the 'Second_class'
        students_not_in_second_class = Student.objects.filter(pk__in=pk_set, school_year='Second_class')
        if students_not_in_second_class.count() != len(pk_set):
            raise ValidationError(f"All students must belong to the 'Second class' school year. Students not in 'Second_class': {students_not_in_second_class}.")
    
    

class LastClassRoom(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PD', 'Pending'
        REJECTED = 'RJ', 'Rejected'
        APPROVED = 'AP', 'Approved'

    class_room_options = [
        ('Java Script', 'Java Script'),
        ('Websockets', 'Websockets'),
        ('Database', 'Database'), 
        ('UI-UX', 'UI-UX')
    ] 
    students = models.ManyToManyField(Student, related_name='last_class_rooms')
    room = models.CharField(max_length=50, choices=class_room_options)
    school_year = models.CharField(max_length=50, choices=Student.SCHOOL_YEAR_CHOICES)
    approval_status = models.CharField(max_length=50, choices= Status.choices, default=Status.PENDING)

    objects = models.Manager()
    approved_students = ApprovedManagerLast()
    
    def __str__(self):
        return "%s (%s)" % (
            self.room,
            ", ".join(student.name for student in self.students.all()),
        )
@receiver(m2m_changed, sender=LastClassRoom.students.through)
def limit_students_to_last_class(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == 'pre_add' and not reverse:
        # Check if any student in the pk_set is not from the 'Last_class'
        students_not_in_last_class = Student.objects.filter(pk__in=pk_set, school_year='Last_class')
        if students_not_in_last_class.count() != len(pk_set):
            raise ValidationError(f"All students must belong to the 'Last class' school year. Students not in 'Last_class': {students_not_in_last_class}.")