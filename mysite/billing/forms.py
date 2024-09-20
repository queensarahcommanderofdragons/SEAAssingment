from django import forms
from .models import Bill

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['address', 'amount_due', 'due_date']

    def save(self, user, *args, **kwargs):
        bill = super(BillForm, self).save(commit=False)
        bill.profile = user.profile #set the profile to the current logged in user
        bill.save()
        return bill