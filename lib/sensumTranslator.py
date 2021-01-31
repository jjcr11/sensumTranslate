from __init__ import *

class SensumTranslator(Client):

    def __init__(self):
        super().__init__()
        self.originalText = ""
        self.translatedText = ""

    def toTranslate(self, originalText):
        self.originalText = originalText
        result = super().translate(self.originalText, target_language="en")
        self.translatedText = unescape(result['translatedText'])
        return self.translatedText