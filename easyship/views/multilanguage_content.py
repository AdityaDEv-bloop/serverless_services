import json

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from easyship.serializers import TranslateSerializer
from easyship.utils import translate_content
from loguru import logger
class MultilanguageTranslate(APIView):
    @swagger_auto_schema(request_body=TranslateSerializer,)
    def post(self, request):
        try:
            request_body = json.loads(request.body)
            serializer = TranslateSerializer(data=request_body)
            logger.info("Translation Has Requested")
            if serializer.is_valid():
                language = request_body["language"]
                content = request_body["content"]
                logger.info("Translating to language {0}".format(language))
                
                translated_content = translate_content(
                    language=language, content=content
                )
                logger.info("Translation is completed to language {0}".format(language))
                return Response(
                    {
                        "msg": "Content Scucessfully translated",
                        "data": translated_content,
                        "status": status.HTTP_201_CREATED,
                    }
                )
                    
            else:
                logger.error("Translation is not completed to language due to invalid request params")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error("Translation is not completed to language due to {0}".format(e))
            return Response(
                        {
                            "msg": "Somthing Went wrong",
                            "error": str(e),
                            "status": status.HTTP_417_EXPECTATION_FAILED,
                        }
                    )

