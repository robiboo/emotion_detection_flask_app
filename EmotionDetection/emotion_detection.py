import requests
import json 

def emotion_detector(text_to_analyze):
    '''
    Define a function, emotion_detector, that takes a string input, text_to_analyze.
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    anger_score = formatted_response['emotionPredictions'][0]["emotion"]['anger']
    disgust_score = formatted_response['emotionPredictions'][0]["emotion"]['disgust']
    fear_score = formatted_response['emotionPredictions'][0]["emotion"]['fear']
    joy_score = formatted_response['emotionPredictions'][0]["emotion"]['joy']
    sadness_score = formatted_response['emotionPredictions'][0]["emotion"]['sadness']

    emotion_scores = {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    }

    max_emotion_score = max(emotion_scores, key=emotion_scores.get)

   
    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': max_emotion_score
            }