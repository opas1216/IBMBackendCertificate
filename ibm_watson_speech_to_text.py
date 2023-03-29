from ibm_watson import SpeechToTextV1

# API: pJQ6VgE_Iqp1SIf1NmurH_rQ623vHA0Cp2x-hHVIws4p
# URL: https://api.jp-tok.speech-to-text.watson.cloud.ibm.com/instances/4d607188-8769-4945-b96f-4c16996b76e0
url_s2t = "Https://stream.watsonplatform.net/speech-to-text/api"
iam_apikey_s2t = "pJQ6VgE_Iqp1SIf1NmurH_rQ623vHA0Cp2x-hHVIws4p"

s2t = SpeechToTextV1(iam_apikey=iam_apikey_s2t, url=url_s2t)