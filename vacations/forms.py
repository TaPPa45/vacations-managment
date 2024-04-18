from django import forms
from django.core.exceptions import ValidationError
from .models import VacationRequest


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class VacationRequestForm(forms.ModelForm):
    class Meta:
        model = VacationRequest
        fields = ['start_date', 'finish_date']
        widgets = {
            'start_date': DatePickerInput(),
            'finish_date': DatePickerInput(),
        }

    def save(self, user, vacation_days, commit=True):
        vacation_request = VacationRequest.objects.create(
            user=user,
            start_date=self.cleaned_data['start_date'],
            finish_date=self.cleaned_data['finish_date'], 
            days=vacation_days,           
        )
        return vacation_request
    

class VacationRequestUpdateForm(forms.ModelForm):
    class Meta:
        model = VacationRequest
        fields = ['status', 'comment']
    def __init__(self, *args, **kwargs):
        super(VacationRequestUpdateForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['status'].label = 'Статус'
        self.fields['comment'].label = 'Комментарий'
        self.fields['comment'].widget.attrs['class'] = 'form-control'
        
    def save(self, commit=True):
        vacation_request = VacationRequest.objects.update(
            status=self.cleaned_data['status'],
            comment=self.cleaned_data['comment'], 
           
        )
        print (vacation_request)
        return vacation_request