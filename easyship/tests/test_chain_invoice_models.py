from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from easyship.models import BankDetails, ChainInvoices, Member


class TestChainModel(TestCase):
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
        self.date = datetime.now()
        ChainInvoices.objects.create(
            name="Test Name",
            description="Test Description",
            consigner=self.member,
            consignee="Test Consignee",
            ref="Test Ref",
            orderno="Test Order No",
            orderdate=self.date,
            buyer="Test Buyer",
            countryoforigin="Test Country Of Origin",
            countryofdestination="Test Country Of Destination",
            termsofdelivery="Test Delivery Term",
            paymentterms="Test Payment Term",
            precarrigemode="Test Pre Crraige Mode",
            vesselno="Test Vessel No",
            portofdischarge="Test Port of Discharge",
            placeofreceipt="Test Port of Receipt",
            placeofloading="Test Port of Loading",
            finaldestination="Test Final Destination",
            invoiceitems="Test invoice items",
            totalcartons=5,
            netweight=10,
            grossweight=10,
            unit="Test Unit",
            variationpercentage="Test Percentage",
            amountinwords="Test Amount Words",
            amount=10000,
            amountunit="Test Amount Unit",
            exporterbankdetails=self.bd,
            importerbankdetails="Test Importer Bank Details",
            dutydrawback=None,
            roadtep=None,
            igst=None,
            isProFormaInvoiceCreated=True,
            isGstInvoiceCreated=False,
            isPreShipmentCreted=True,
            isCommercialInvoiceCreated=False,
            isPackegingInvoiceCreated=False,
            datecreated=self.date,
        )

    def test_chain_create(self):
        chain = ChainInvoices.objects.get(name="Test Name")
        self.assertEqual(chain.id, 1)
        self.assertEqual(chain.description, "Test Description")
        self.assertEqual(chain.buyer, "Test Buyer")
        self.assertEqual(chain.consigner, self.member)
        self.assertEqual(chain.consignee, "Test Consignee")
        self.assertEqual(chain.countryoforigin, "Test Country Of Origin")
        self.assertEqual(chain.countryofdestination, "Test Country Of Destination")
        self.assertEqual(chain.finaldestination, "Test Final Destination")
        self.assertEqual(chain.termsofdelivery, "Test Delivery Term")
        self.assertEqual(chain.ref, "Test Ref")
        self.assertEqual(chain.orderno, "Test Order No")
        self.assertEqual(chain.precarrigemode, "Test Pre Crraige Mode")
        self.assertEqual(chain.vesselno, "Test Vessel No")
        self.assertEqual(chain.portofdischarge, "Test Port of Discharge")
        self.assertEqual(chain.placeofreceipt, "Test Port of Receipt")
        self.assertEqual(chain.invoiceitems, "Test invoice items")
        self.assertEqual(chain.unit, "Test Unit")
        self.assertEqual(chain.variationpercentage, "Test Percentage")
        self.assertEqual(chain.amountinwords, "Test Amount Words")
        self.assertEqual(chain.importerbankdetails, "Test Importer Bank Details")
        self.assertEqual(chain.amountunit, "Test Amount Unit")
        self.assertEqual(chain.dutydrawback, None)
        self.assertEqual(chain.roadtep, None)
        self.assertEqual(chain.igst, None)
        self.assertEqual(chain.isProFormaInvoiceCreated, True)
        self.assertEqual(chain.isPackegingInvoiceCreated, False)
        self.assertEqual(chain.isGstInvoiceCreated, False)
        self.assertEqual(chain.isPreShipmentCreted, True)
        self.assertEqual(chain.isCommercialInvoiceCreated, False)
        self.assertEqual(type(chain.orderdate), type(self.date))

    def test_default_chain_entry(self):
        chain = ChainInvoices.objects.create(
            name="Test Name",
            description="Test Description",
            consigner=self.member,
            consignee="Test Consignee",
            ref="Test Ref",
            orderdate=self.date,
            buyer="Test Buyer",
            countryoforigin="Test Country Of Origin",
            countryofdestination="Test Country Of Destination",
            termsofdelivery="Test Delivery Term",
            paymentterms="Test Payment Term",
            precarrigemode="Test Pre Crraige Mode",
            portofdischarge="Test Port of Discharge",
            placeofreceipt="Test Port of Receipt",
            placeofloading="Test Port of Loading",
            finaldestination="Test Final Destination",
            invoiceitems="Test invoice items",
            totalcartons=5,
            netweight=10,
            grossweight=10,
            unit="Test Unit",
            variationpercentage="Test Percentage",
            amountinwords="Test Amount Words",
            amount=10000,
            amountunit="Test Amount Unit",
            exporterbankdetails=self.bd,
        )

        self.assertEqual(chain.isProFormaInvoiceCreated, False)
        self.assertEqual(chain.isPackegingInvoiceCreated, False)
        self.assertEqual(chain.isGstInvoiceCreated, False)
        self.assertEqual(chain.isPreShipmentCreted, False)
        self.assertEqual(chain.isCommercialInvoiceCreated, False)
        self.assertEqual(chain.orderno, None)
        self.assertEqual(chain.importerbankdetails, None)
        self.assertEqual(chain.roadtep, None)
        self.assertEqual(chain.dutydrawback, None)
        self.assertEqual(chain.igst, None)
