from django.urls import path
from .views import branch,employee,cars
from . import views
urlpatterns = [
    path('branches/',views.branch, name='all-branchs'),
    path('branches/<int:branch_id>',views.branch, name='add-branch'),
    path('branches/employee/', views.employee, name='all-cars-in-branch'),
    path('branches/<int:branch_id>/employee/',views.employee, name='employees-in-branch'),
    path('branches/<int:branch_id>/cars/',views.cars, name='cars-in-branch'),
    path('branches/all-cars/',views.cars, name='all-cars-in-branch'),
]