from django.test import TestCase
from easyship.models import Account
from django.db.utils import IntegrityError

class TestAuthModel(TestCase):
    def setUp(self):
        self.account = Account.objects.create(
            email = "test@test.com",
            username = "testUser",
            phonenumber = "+123456789"
        )

    def test_account_create(self):
        account = Account.objects.get(email="test@test.com")
        self.assertEqual(account.username, "testUser")

    def test_unique_email_entry(self):
        with self.assertRaises(IntegrityError):
            Account.objects.create(
            email = "test@test.com",
            username = "testUser1",
            phonenumber = "+523456789"
        )
