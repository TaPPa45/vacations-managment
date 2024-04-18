from django.urls import path
from .views import VacationRequestView, import_from_excel

urlpatterns = [
    path('vacation_request', VacationRequestView.as_view(), name="vacation_request"),
    path('import/', import_from_excel, name='import_from_excel'),
]