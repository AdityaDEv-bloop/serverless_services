from django.test import TestCase

from easyship.utils.multilanguage_content import translate_content


class TestTranslation(TestCase):
    def setUp(self):
        return super()

    def test_translation(self):
        expected_return = ["안녕하세요", "나는 aditya입니다"]
        data = {"language": "ko", "content": ["Hello", "I Am Aditya"]}
        translatedData = translate_content(data["language"], data["content"])
        self.assertEqual(translatedData, expected_return)
        self.assertEqual(len(translatedData), len(data["content"]))
