from django.urls import path
from .views import LkView, VacationRequestListView, BossVacationRequestListView, CreateEmployerView
from vacations.views import VacationRequestUpdateView

urlpatterns = [
    path('lk', LkView.as_view(), name='lk'),
    path('lk/vacation_list', VacationRequestListView.as_view(), name='vacation_list'),
    path('lk/vacation_request_list', BossVacationRequestListView.as_view(), name='vacation_request_list'),
    path('lk/vacation_approvalr/<slug:pk>/', VacationRequestUpdateView.as_view(), name='vacation_approval'),
    path('lk/add_employer', CreateEmployerView.as_view(), name='add_employer'),


]