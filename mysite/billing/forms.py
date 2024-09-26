from django import forms
from .models import Bill

#creates the bill form

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['address', 'amount_due', 'due_date']