from django.db import models

class BaseClass(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.TextField(max_length=200, null=True)
    class Meta:
        abstract = True
        
class Student(BaseClass):
    enrollment = models.CharField(max_length=20)
    STATES = (
    ('bsit','BSIT'),
    ('bscs', 'BSCS'),
    ('bsse','BSSE'),
    ('bsds','BSDS'),
    ('bsai','BSAI'),
)
    discipline = models.CharField(max_length=10, choices=STATES)
    
    def __str__(self):
        return self.name
    
class Teacher(BaseClass):
    # student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='department')
    STATES = (
    ('cs','Computer Science'),
    ('eng', 'English'),
    ('math','Mathematics'),
    ('chm','Chemistry'),
    ('phy','Physics'),
)
    department = models.CharField(max_length=20, choices=STATES)
    
    def __str__(self):
        return self.name