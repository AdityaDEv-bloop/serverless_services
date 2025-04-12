import json

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from easyship.utils import translate_content


class MultilanguageTranslate(APIView):
    def post(self, request):
        body = json.loads(request.body)
        print(body)
        language = body["data"]["language"]
        content = body["data"]["content"]
        try:
            translated_content = translate_content(language=language, content=content)
            return Response(
                {
                    "msg": "Content Scucessfully translated",
                    "data": translated_content,
                    "status": status.HTTP_201_CREATED,
                }
            )
        except Exception as e:
            return Response(
                {
                    "msg": "Somthing Went wrong",
                    "error": str(e),
                    "status": status.HTTP_417_EXPECTATION_FAILED,
                }
            )
