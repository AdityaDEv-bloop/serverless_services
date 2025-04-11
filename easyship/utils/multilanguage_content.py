from googletrans import Translator




def translate_content(language:str,content):
    return_content = []
    translator = Translator()
    translations = translator.translate(content, dest=language)
    for translation in translations: return_content.append(translation.text)
    return return_content