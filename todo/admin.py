from django.contrib import admin
from .models import ToDo

@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
	list_display = ('id', 'description', 'is_complete', 'created_at')
