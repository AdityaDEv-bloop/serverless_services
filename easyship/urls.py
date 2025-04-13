from django.urls import path

from easyship.views import MultilanguageTranslate

urlpatterns = [
    path("ship-easy/translate/", view=MultilanguageTranslate.as_view(), name="translate"),
]
