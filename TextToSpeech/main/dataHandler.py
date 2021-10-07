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

    def toSpeechURL(self):
        data = self._data
        BASE_URL = "https://voice.reverso.net/RestPronunciation.svc/v1/output=json/GetVoiceStream/voiceName=he-IL-Asaf?inputText="
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