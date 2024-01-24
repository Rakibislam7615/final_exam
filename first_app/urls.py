from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('add_new_task/',views.add_task,name='add_task'),
    path('show_task/',views.show_tasks,name='show_tasks'),
    path('edit_task/<int:id>',views.edit_task,name='edit_task'),
    path('delete_task/<int:id>',views.delete_task,name='delete_task'),
    path('complete_task/<int:id>',views.complete_task,name='complete_task'),
    path('completed_task/',views.completed_task,name='completed_task'),
]
