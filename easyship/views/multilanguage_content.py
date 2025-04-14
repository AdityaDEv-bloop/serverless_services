import json

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from easyship.serializers import TranslateSerializer
from easyship.utils import translate_content


class MultilanguageTranslate(APIView):
    @swagger_auto_schema(request_body=TranslateSerializer)
    def post(self, request):
        request_body = json.loads(request.body)
        serializer = TranslateSerializer(data=request_body)
        if serializer.is_valid():
            language = request_body["language"]
            content = request_body["content"]
            try:
                translated_content = translate_content(
                    language=language, content=content
                )
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
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
