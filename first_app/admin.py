from django.contrib import admin
from first_app.models import TaskModel

class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','is_completed']
    
admin.site.register(TaskModel,TaskModelAdmin)

# Register your models here.
