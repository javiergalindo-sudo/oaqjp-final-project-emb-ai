import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the emotion detector API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)
    emotion = formatted_response['emotionPredictions'][0]['emotion']
    
    # Extraer todas las emociones (incluyendo joy que faltaba)
    anger = emotion['anger']
    disgust = emotion['disgust']
    fear = emotion['fear']
    joy = emotion['joy']
    sadness = emotion['sadness']
    
    emotions = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    
    # Encontrar la emoción dominante (la que tiene el valor más alto)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Agregar la emoción dominante al diccionario
    emotions['dominant_emotion'] = dominant_emotion

    # Retornar el diccionario completo
    return emotions