from django.db import models
from django.utils.timezone import datetime
from datetime import date
#from Appname.models import model
from Person.models import Person
# Create your models here.
# def is_date_event(value):
#     if value <= date.today():
#         raise ValidationError('Event date is incorrect!!!')
#     return value
class Event(models.Model):
    title=models.CharField("Titre",max_length=255)
    description=models.TextField()
    image=models.ImageField(upload_to='images/',blank=True)
    CATEGORY_EVENT=(
        ('Music','M'),
        ('Sprot','S'),
        ('Cinema','C')
    )
    category=models.CharField(max_length=8,choices=CATEGORY_EVENT)
    state=models.BooleanField(default=False)
    nbe_participant=models.IntegerField(default=0)
    creation_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    evt_date=models.DateField()
    organizer=models.ForeignKey(
        Person,
        on_delete=models.CASCADE
        # on_delete=models.SET_NULL,
        # null=True                 
    )
    participation=models.ManyToManyField(
        Person,    
        through="participation_event"  ,
        related_name="participations"       
    )
    class Meta:
        constraints=[
            models.CheckConstraint(
                check=models.Q(evt_date__gte=datetime.now()),
                name="Please check the event date!"
            )
        ]
class participation_event(models.Model):
    person=models.ForeignKey(Person,on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    participation_date=models.DateField(auto_now=True)
    class Meta:
        unique_together=('person','event')