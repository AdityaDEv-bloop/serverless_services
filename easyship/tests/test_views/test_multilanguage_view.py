import json

from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase

from easyship.views.multilanguage_content import MultilanguageTranslate


class TestMultilanguageTranslation(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        # self.user = User.objects.create_user(
        #     username="jacob", email="jacob@…", password="top_secret"
        # )

    def test_multilanguage_view(self):
        # Create an instance of a GET request.
        request = self.factory.post(
            "/ship-easy/translate/",
            content_type="application/json",
            data=json.dumps({"language": "ko", "content": ["Hello", "Test This View"]}),
        )

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        # request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Use this syntax for class-based views.
        response = MultilanguageTranslate.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_multilanguage_view_failure(self):
        # Create an instance of a GET request.
        request = self.factory.get("/ship-easy/translate/")

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        # request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Use this syntax for class-based views.
        response = MultilanguageTranslate.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_multilanguage_view_serializer_failure(self):
        # Create an instance of a GET request.
        request = self.factory.post(
            "/ship-easy/translate/",
            content_type="application/json",
            data=json.dumps({"language": "ko"}),
        )

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        # request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Use this syntax for class-based views.
        response = MultilanguageTranslate.as_view()(request)
        self.assertEqual(response.status_code, 400)
