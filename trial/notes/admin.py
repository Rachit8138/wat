from django.contrib import admin
from .models import Notes

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created') #displays notes title on the list

admin.site.register(Notes, NotesAdmin) #so that it appears on admin Dashboard UI
