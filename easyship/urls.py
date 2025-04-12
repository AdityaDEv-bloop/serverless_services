from django.urls import path

from easyship.views import MultilanguageTranslate

urlpatterns = [
    path("translate/", view=MultilanguageTranslate.as_view(), name="translate"),
]
