from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.employee_form,name='employee_insert'), #get or post request. for insert operations
    path('<int:id>/',views.employee_form,name='employee_update'), # get or post request, for update operations.
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'), # get or post request, for update operations.
    path('list/',views.employee_list,name='employee_list') #get req. to retrive and display all records.
]