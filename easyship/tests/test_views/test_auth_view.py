import json

from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase

from easyship.views.auth import Signup


class TestAuth(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_signup_view(self):
        # Create an instance of a GET request.
        request = self.factory.post(
            "/ship-easy/signup/",
            content_type="application/json",
            data=json.dumps(
                {
                    "email": "testemail@email.com",
                    "username": "test user",
                    "firstname": "test firstname",
                    "lastname": "test lastname",
                    "phonenumber": "+123456978",
                    "password": "test_password",
                }
            ),
        )

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        # request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Use this syntax for class-based views.
        response = Signup.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_signup_view_failure(self):
        # Create an instance of a GET request.
        request = self.factory.get("/ship-easy/signup/")

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        # request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Use this syntax for class-based views.
        response = Signup.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_signup_view_serializer_failure(self):
        # Create an instance of a GET request.
        request = self.factory.post(
            "/ship-easy/signup/",
            content_type="application/json",
            data=json.dumps(
                {
                    "email": "testemail@email.com",
                    "username": "test user",
                }
            ),
        )

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        # request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Use this syntax for class-based views.
        response = Signup.as_view()(request)
        self.assertEqual(response.status_code, 400)
