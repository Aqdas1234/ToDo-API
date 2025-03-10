from django.contrib import admin
from .models import ToDo

@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'completed', 'created_at')  
    list_filter = ('completed', 'created_at')  
    search_fields = ('title', 'user__username') 