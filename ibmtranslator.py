import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = '2bD4baLDk4-suALxSjoLyXDJxj72hiVDmvTuwzXO1uAk'
url = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/da21a171-cebd-4a9e-a8e8-d1ff371ef524'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-04-09',
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)



def englishToFrench(englishText):
    #write the code here
    translation = language_translator.translate(
    text = englishText,
    model_id = 'en-fr').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    frenchText = translation['translations'][0]['translation']
    return frenchText


def frenchToEnglish(frenchText):
    #write the code here
    translation = language_translator.translate(
    text = frenchText,
    model_id = 'fr-en').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    englishText = translation['translations'][0]['translation']
    return englishText