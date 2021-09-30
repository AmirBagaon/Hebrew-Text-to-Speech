import argparse
import base64
import requests
from os import path

def getTranslation(text, output_path):
    BASE_URL = "https://voice.reverso.net/RestPronunciation.svc/v1/output=json/GetVoiceStream/voiceName=he-IL-Asaf?inputText="
    #Convert it to base 64
    text_b64 = base64.b64encode(text.encode()).decode()
    full_url = BASE_URL + text_b64

    #Adding some headers for the requests
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

    request = requests.get(full_url, stream=True, headers=headers)
 
    with open(output_path, 'wb') as f:
            f.write(request.content)

def parse_args():
    parser = argparse.ArgumentParser(description='Text to Speech that supports hebrew')
    parser.add_argument('-t','--text', help='The text that should be translated to speech', required=True)
    parser.add_argument('-o','--output_path', help='Output path. Must end with .mp3 extension', required=False, default='myfile.mp3')
    
    #optional: argsdict = vars(parser.parse_args())
    args = parser.parse_args()
    _, extension = path.splitext(args.output_path)
    if extension != ".mp3":
        raise ValueError("Output must end with '.mp3' extension")
    
    return args

if __name__ == '__main__':
    print("hello")
    args = parse_args()
    getTranslation(args.text, args.output_path)

