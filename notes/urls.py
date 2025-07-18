from django.urls import path
from . import views
urlpatterns = [
   
    #path('',views.home,name='home'),
    path('',views.index,name='index'),
    path('note_list',views.note_list,name='note_list'),
    path('note_create',views.note_create,name='note_create'),
    path('note_update/<int:pk>/',views.note_update,name='note_update'),
    path('note_delete/<int:pk>/',views.note_delete,name='note_delete')

]
