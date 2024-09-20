from django.shortcuts import render, redirect, get_object_or_404
from .models import Bill
from Users.models import Profile
from .forms import BillForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# View all bills for the logged-in user
@login_required
def view_bills(request):
    #get the profile of the logged in user
    profile = Profile.objects.get(user=request.user)

    #go to all bills linked to profile
    bills = Bill.objects.filter(profile=profile)

    return render(request, 'billing/view_bills.html', {'bills': bills})

# Create a new bill, automatically assigned to the logged-in user
@login_required
def create_bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            bill = form.save(commit=False)
            bill.user = request.user.profile
            bill.save()
            messages.success(request, 'Bill successfully created')
            return redirect('view_bills')
    else:
        form = BillForm()
    return render(request, 'billing/create_bill.html', {'form': form})

# Update an existing bill if the user owns it
@login_required
def update_bill(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id, user=request.user)
    if request.method == 'POST':
        form = BillForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            return redirect('view_bills')
    else:
        form = BillForm(instance=bill)
    return render(request, 'billing/update_bill.html', {'form': form})

# Delete a bill if the user owns it
@login_required
def delete_bill(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id, user=request.user)
    if request.method == 'POST':
        bill.delete()
        return redirect('view_bills')
    return render(request, 'billing/delete_bill.html', {'bill': bill})