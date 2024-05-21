from django.urls import path
from .views import person_list, update_person, delete_person

urlpatterns = [
    path('', person_list, name='person_list'),
    path('update/<int:person_id>/', update_person, name='update_person'),
    path('delete/<int:person_id>/', delete_person, name='delete_person'),
]
