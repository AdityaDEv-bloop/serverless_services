from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.test import TestCase

from easyship.models import BankDetails, Member


class TestMemberModel(TestCase):
    def setUp(self):
        BankDetails.objects.create(
            bankname="Test Bank",
            accountno="Test Account No",
            ifsccode="Test IFSC",
            branchname="Test Branch",
        )
        self.account = User.objects.create_user(
            "Test User", "test@test.com", "testpassword"
        )
        self.bd = BankDetails.objects.get(accountno="Test Account No")
        self.member = Member.objects.create(
            user=self.account,
            companyname="Test Company",
            address="Test Address",
            gst="Test Gst No",
            ref="Test IEC",
            bankdetails=self.bd,
        )

    def test_member_create(self):
        member = Member.objects.get(user=self.account)
        self.assertEqual(member.companyname, "Test Company")
        self.assertEqual(member.address, "Test Address")
        self.assertEqual(member.gst, "Test Gst No")
        self.assertEqual(member.bankdetails, self.bd)
        self.assertEqual(member.id, self.member.id)

    def test_unique_member_entry(self):
        with self.assertRaises(IntegrityError):
            Member.objects.create(
                user=self.account,
                companyname="Test Company 1",
                address="Test Address 1",
                gst="Test Gst No 1",
                ref="Test IEC",
                bankdetails=self.bd,
            )
