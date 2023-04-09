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

class AnalysedText(object):
    def __init__(self, text):

        pass
    # text2 = "Michael is handsome MichaelMichaelMichaelMichael"
    # text3 = text2.replace('Michael', 'Julie')
    # print(f"Text3 {text3}")
    # print(f"Type of {text2.split()} is {type(text2.split())}")
    # print(f"Count of Michael = {text2.count('Michael')}")


def shuffle(input_list, card_number):
    print(f"Origin cards = {input_list}, will be shuffle by each partition of {card_number} cards.")
    start_index = 0
    partition_list = []

    if len(input_list)%card_number == 0:
        partition = len(input_list)//card_number
        for group_index in range(partition):
            partition_list.append(result[start_index:start_index + card_number:])
            start_index+=card_number
        print(f"partition_list = {partition_list}")
    else:
        partition = len(input_list) // card_number + 1
        for group_index in range(partition):
            if group_index == partition-1:
                partition_list.append(result[start_index::])
                start_index+=card_number
            else:
                partition_list.append(result[start_index:start_index + card_number:])
                start_index += card_number
        print(f"partition_list = {partition_list}")

    if len(partition_list)%2 == 0:
        for index in range(int(len(partition_list)/2)):
            partition_list[index], partition_list[len(partition_list)-1-index] = partition_list[len(partition_list)-1-index], partition_list[index]
    else:
        for index in range(len(partition_list)//2):
            partition_list[index], partition_list[len(partition_list) - 1 - index] = partition_list[
                                                                                         len(partition_list) - 1 - index], \
                                                                                     partition_list[index]
    print(f"After shuffle = {partition_list}")
    input_list = []
    for group in partition_list:
        for element in group:
            input_list.append(element)
    print(f"Return input_list = {input_list}")
    return input_list




def englishToFrench(englishText):
    #write the code here
    frenchText = ""
    translation = language_translator.translate(
    text = englishText,
    model_id = 'en-fr').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    print(f"translation= {translation['translations'][0]['translation']}")
    # frenchText = translation[]
    return frenchText


def frenchToEnglish(frenchText):
    #write the code here
    englishText = ""
    translation = language_translator.translate(
    text = frenchText,
    model_id = 'fr-en').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    print(f"translation= {translation}")
    return englishText


# frenchToEnglish("")
frenchToEnglish("Bonjour")
# englishToFrench("")
englishToFrench("Hello")



