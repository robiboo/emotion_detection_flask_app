import requests
import json 

def emotion_detector(text_to_analyze):
    '''
    Define a function, emotion_detector, that takes a string input, text_to_analyze.
    '''
        
    # If blank inputs are given 
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    #Define API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Make the post request
    response = requests.post(url, json=myobj, headers=header)
    
    # Return None for all emotions if status code is 400
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion' : None
        }
    

    if response.status_code == 200:
        # Extract Emotion Scores
        formatted_response = json.loads(response.text)

        anger_score = formatted_response['emotionPredictions'][0]["emotion"]['anger']
        disgust_score = formatted_response['emotionPredictions'][0]["emotion"]['disgust']
        fear_score = formatted_response['emotionPredictions'][0]["emotion"]['fear']
        joy_score = formatted_response['emotionPredictions'][0]["emotion"]['joy']
        sadness_score = formatted_response['emotionPredictions'][0]["emotion"]['sadness']

        # Create dictionary for emotion scores 
        emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        }

        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return dictionary of emotion scores and dominant emotion
    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            }