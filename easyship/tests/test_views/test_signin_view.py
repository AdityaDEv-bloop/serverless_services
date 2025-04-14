import json

from django.test import Client, RequestFactory, TestCase

from easyship.models.auth import Account


class TestSignIn(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = Account(
            email="testemail@email.com",
            username="test username signin",
            firstname="test firstname",
            lastname="test lastname",
            phonenumber="+123456978",
        )

        self.user.set_password("test_password")
        self.user.save()

    def test_signin(self):
        response = self.client.post(
            "/ship-easy/signin/",
            content_type="application/json",
            data=json.dumps(
                {
                    "email": self.user.email,
                    "password": "test_password",
                }
            ),
        )
        self.assertEqual(response.status_code, 200)

    def test_signin_serializer_error(self):
        response = self.client.post(
            "/ship-easy/signin/",
            content_type="application/json",
            data=json.dumps(
                {
                    "email": self.user.email,
                }
            ),
        )
        self.assertEqual(response.status_code, 400)

    def test_signin_unathorized_error(self):
        response = self.client.post(
            "/ship-easy/signin/",
            content_type="application/json",
            data=json.dumps(
                {
                    "email": self.user.email,
                    "password": "test",
                }
            ),
        )
        self.assertEqual(response.status_code, 401)
