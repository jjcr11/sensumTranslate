from google.cloud.translate_v2 import Client
from html import unescape

class Translator(Client):

    def __init__(self):
        super().__init__()
        self.original_text = ""
        self.translated_text = ""

    def to_translate(self, original_text):
        self.original_text = original_text
        result = super().translate(self.original_text, target_language="en")
        self.translated_text = unescape(result['translatedText'])
        return self.translated_text

translator = Translator()

print(translator.to_translate("Hola"))
print(translator.to_translate("Mundo"))
print(translator.to_translate("Peludo"))