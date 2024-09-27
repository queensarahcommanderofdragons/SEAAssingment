from django.test import TestCase
from django.contrib.auth.models import User
from billing.models import Bill

#bill creation test

class BillCreationTest(TestCase):

    def setUp(self):
        # Create a user first to assign the bill
        self.user = User.objects.create_user(username='testuser', password='testpassword123')

    def test_bill_creation(self):
        # Simulate creating a bill for the user
        bill = Bill.objects.create(user=self.user, address="123 Example St", amount_due=500.00)

        # Check if the bill was created successfully
        self.assertEqual(bill.address, "123 Example St")
        self.assertEqual(bill.amount_due, 500.00)
        self.assertEqual(bill.user.username, 'testuser')
