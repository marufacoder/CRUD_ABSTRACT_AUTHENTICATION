from django.urls import path
from project_app.views import *





urlpatterns=[
    path('', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('logout/',logout_view, name='logout_view'),
    path('home/',home_view, name='home_view'),

    path('project_list/', project_list, name='project_list'),
    path('add_project/', add_project, name='add_project'),
    path('update_project/<str:p_id>/',update_project, name='update_project'),
    path('delete_project/<str:p_id>/',delete_project, name='delete_project')
]