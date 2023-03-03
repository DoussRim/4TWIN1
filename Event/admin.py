from django.contrib import admin,messages
from django.db import models
from .models import Event,participation_event
from datetime import datetime
# Register your models here.
class upcomingEvent(admin.SimpleListFilter):
    title="Event Date"
    parameter_name='evt_date'
    def lookups(self,request,model_admin ):
        return (
            ('Past Events',("Past Events")),
            ('Upcoming ',('Upcoming Events')),
            ('Today Events',('Today Events'))
        )
    def queryset(self, request,queryset):
        if self.value()== 'Past Events':
            return queryset.filter(evt_date__lt=datetime.today())
        if self.value()== 'Upcoming ':
            return queryset.filter(evt_date__gt=datetime.today())
        if self.value()== 'Today Events':
            return queryset.filter(evt_date__exact=datetime.today())
        
class ParticipantList(admin.SimpleListFilter):
    title="Participant"
    parameter_name='nbe_participant'
    def lookups(self,request,model_admin ):
        return (
            ('0',("No Participant")),
            ('more ',('There are participants'))
             )
    def queryset(self, request,queryset):
        if self.value()== '0':
            return queryset.filter(nbe_participant__exact=0)
        else:
            return queryset.filter(nbe_participant__gt=0)
def set_true(ModelAdmin,request,queryset):
    req=queryset.update(state=True)
    if req==1:
        message="1 event was "
    else:
        message=f"{req} events were"
    messages.success(request,message="%s successfully accepted"%message)
set_true.short_description="Accept"

class ParticipationsAdmin(admin.StackedInline):
    model=participation_event
    extra=2
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=('title','description',
                  'nbe_participant',
                  'category',
                  'state','image',
                  'evt_date',
                  'creation_date',
                  'updated_at','organizer',
                  'evt_participation')
    def evt_participation(self,obj):
        count=obj.participation.count()
        return count
    ordering=('-title','evt_date')
    list_per_page=2
    list_filter=('state','category',upcomingEvent,ParticipantList)
    def set_false(self,request,queryset):
        req=queryset.filter(state=False)
        if(req.count()>0):
            messages.error(request,f"{req.count()} events are already marked refused")
        else:
            req=queryset.update(state=False)
            if req==1:
                message="1 event was "
            else:
                message=f"{req} events were"
            messages.success(request,message="%s successfully refused"%message)
    set_false.short_description="Refused"
    actions=[set_true,set_false]
    fieldsets=(
        ('A propos',{'fields':('title','description','image')}),
        ('Date',{'fields':('evt_date','creation_date','updated_at')}),
        ('Others',{'fields':('category','nbe_participant')}),
        ('Personal',{'fields':('organizer',)})
    )
    readonly_fields=['creation_date','updated_at']
    inlines=(ParticipationsAdmin,)
    autocomplete_fields=['organizer']
    
# admin.site.register(Event,EventAdmin)