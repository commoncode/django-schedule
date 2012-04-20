from django.contrib import admin
from django import forms
from schedule.models import Calendar, Event, CalendarRelation, Rule

class CalendarAdminOptions(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']
admin.site.register(Calendar, CalendarAdminOptions)


class EventFormAdmin(forms.ModelForm):
    detailed_description = forms.CharField(widget=forms.Textarea(attrs={'class':'rich-text'}), required=False)
    contact_details = forms.CharField(widget=forms.Textarea(attrs={'class':'rich-text'}), required=False)
    class Meta:
        model = Event
class EventAdmin(admin.ModelAdmin):
    form = EventFormAdmin
    class Media:
        js = ['/static/tinymce/jscripts/tiny_mce/tiny_mce.js', '/static/tinymce_setup.js',]
admin.site.register(Event, EventAdmin)

admin.site.register([Rule, CalendarRelation])
