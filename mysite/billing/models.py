from django.contrib.auth.decorators import login_required
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from Users.models import Profile

# Create your models here.

@login_required
class Bill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE) #link model to profile
    address = models.CharField(max_length=225, default='')
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField(default=timezone.now)
    date_issued = models.DateField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    class Meta:
        # ensure a user cannot have two bills with the same address
        unique_together = ('profile', 'address')

    def save(self, *args, **kwargs):
        # logic to generate the bill when an address is entered
        if not self.pk:  # ensures only run when bill created
            self.amount_due = self.calculate_bill()

        super(Bill, self).save(*args, **kwargs)

    def calculate_bill(self):
        # placeholder for actual bill calculation logic, could be more complex
        return 250.00

    def __str__(self):
        return f"bill for {self.profile.user.usernqame} at {self.address} - Amount Due: {self.amount_due}"