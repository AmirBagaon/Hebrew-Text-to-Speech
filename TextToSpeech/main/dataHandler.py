import json
from typing import Match
import pickle
import random
import requests
import base64


class DataHanlder():
    def __init__(self, data, data_type = "Numerology") -> None:
        self._data = data
        self._data_type = data_type
    
    def handle(self):
        returnValue = ""

        if self._data_type == "Numerology":
            return self.numerology()
        elif self._data_type == "ToUpper":
            return self.toUpper()
        elif self._data_type == "ToLower":
            return self.toLower()
        elif self._data_type == "Encryption":
            return self.encryption()
        elif self._data_type == "Decryption":
            return self.decryption()
        elif self._data_type =="TextToSpeechPlay":
            return self.toSpeechURL()
        elif self._data_type =="Translate":
            return self.translate(str(self._data))
        elif self._data_type =="Reverse":
            return self.reverse_txt()

    def toUpper(self):
        return str(self._data).upper()
    
    def toLower(self):
        return str(self._data).lower()
    
    def decryption(self):
            data = self._data
            decryption_dict = self.load_obj("dces_fullMap.db")
            output = ""
            for letter in data:
                if letter in decryption_dict:
                    output += list(decryption_dict[letter])[0]
                else:
                    output += letter
            return output

    def encryption(self):
        data = str(self._data).lower()
        encryption_dict = self.load_obj("my_db.db")
        output = ""
        for letter in data:
            if letter.upper() in encryption_dict:
                p = random.randint(1, 9) 
                if  p <= 3:
                    output += random.choice(encryption_dict[letter])
                else:
                    output += letter
            else:
                output += letter
        return output
    
    def reverse_txt(self):
        return str(self._data)[::-1]



    def numerology(self):
        letters_map = (
            (1, u'א'),
            (2, u'ב'),
            (3, u'ג'),
            (4, u'ד'),
            (5, u'ה'),
            (6, u'ו'),
            (7, u'ז'),
            (8, u'ח'),
            (9, u'ט'),
            (10, u'י'),
            (20, u'כ'),
            (30, u'ל'),
            (40, u'מ'),
            (50, u'נ'),
            (60, u'ס'),
            (70, u'ע'),
            (80, u'פ'),
            (90, u'צ'),
            (100, u'ק'),
            (200, u'ר'),
            (300, u'ש'),
            (400, u'ת'),
        )
        letters_dict = dict([(k, v) for v, k in letters_map])
        letters_dict[u'ך'] = 20
        letters_dict[u'ם'] = 40
        letters_dict[u'ן'] = 50
        letters_dict[u'ף'] = 80
        letters_dict[u'ץ'] = 90

        result = 0

        for letter in self._data:
            if letter in letters_dict:
                result += letters_dict[letter]
        
        return result
    def load_obj(self, name):
        with open(r"main/obj/" + name + '.pkl', 'rb') as f:
            return pickle.load(f)

    def getVoicePerson(self):
        if self.containsHebrew(str(self._data)):
            return "he-IL-Asaf"
        
        import random
        return random.choice(['Graham22k', 'Lucy22k', 'Peter22k', 'QueenElizabeth22k', 'Rachel22k', 'Heather22k', 'Karen22k', 'Kenny22k', 'Laura22k', 'Micah22k', 'Nelly22k', 'Rod22k', 'Ryan22k', 'Saul22k', 'Sharon22k', 'Tracy22k', 'Will22k'])

    def toSpeechURL(self):
        data = self._data
        BASE_URL = f"https://voice.reverso.net/RestPronunciation.svc/v1/output=json/GetVoiceStream/voiceName={self.getVoicePerson()}?inputText="
        #Convert it to base 64
        text_b64 = base64.b64encode(data.encode()).decode()
        full_url = BASE_URL + text_b64
        print(full_url)
        return full_url

    def getTranslation():
        __data = {
                "source_text": "hello",
                "target_text": "world",
                "source_lang": "en",
                "target_lang": "he",
            }
        x=json.dumps(__data)
        print(x)
        HEADERS = {"User-Agent": "Mozilla/5.0",
            "Content-Type": "application/json; charset=UTF-8"
            }
        translations_json = requests.post("https://context.reverso.net/bst-query-service", headers=HEADERS,
                                            data=json.dumps(__data)).json()["dictionary_entry_list"]
        for translation in translations_json:
            print(translation["term"])
    
    def containsHebrew(self, s):
        return any("\u0590" <= c <= "\u05EA" for c in s)
    def translate(self,txt_to_translate, to_language="auto", from_language="auto"):
        #if text doesn't contain Hebrew - translate it to Hebrew
        if not self.containsHebrew(txt_to_translate):
            to_language="iw"

        #based on mtranslate library
        import re, html, urllib.request, urllib.parse
        txt_to_translate = urllib.parse.quote(txt_to_translate)
        print("Here!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        HEADERS = {'User-Agent': "Mozilla/4.0 (compatible;MSIE 6.0;Windows NT 5.1;SV1;.NET CLR 1.1.4322;.NET CLR 2.0.50727;.NET CLR 3.0.04506.30)"}
        BASE_URL = "http://translate.google.com/m?tl=%s&sl=%s&q=%s"
        full_url = BASE_URL % (to_language, from_language, txt_to_translate)
        request = urllib.request.Request(full_url, headers=HEADERS)
        data = urllib.request.urlopen(request).read().decode("utf-8")
        expr = r'(?s)class="(?:t0|result-container)">(.*?)<'
        result = re.findall(expr, data)
        return html.unescape(result[0])