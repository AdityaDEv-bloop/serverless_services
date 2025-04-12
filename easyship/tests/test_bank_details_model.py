from django.db.utils import IntegrityError
from django.test import TestCase

from easyship.models import BankDetails


class TestBankDetailsModel(TestCase):
    def setUp(self):
        self.bd = BankDetails.objects.create(
            bankname="Test Bank",
            accountno="Test Account No",
            ifsccode="Test IFSC",
            branchname="Test Branch",
        )

    def test_bank_details_create(self):
        bd = BankDetails.objects.get(accountno="Test Account No")
        self.assertEqual(bd.bankname, "Test Bank")
        self.assertEqual(bd.ifsccode, "Test IFSC")
        self.assertEqual(bd.branchname, "Test Branch")
        self.assertEqual(bd.id, 1)

    def test_unique_bank_details_entry(self):
        with self.assertRaises(IntegrityError):
            BankDetails.objects.create(
                bankname="Test Bank 1",
                accountno="Test Account No",
                ifsccode="Test IFSC 1",
                branchname="Test Branch 1",
            )
