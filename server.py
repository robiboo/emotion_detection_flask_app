from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

# Route to render the index page
@app.route("/")
def render_index_page():
    return render_template('index.html') 

@app.route("/emotionDetector", methods=['GET'])
def emotion_detection():

    # Get the text to analyze from the query parameters (from URL)
    text_to_analyze = request.args.get("textToAnalyze")  # Guaranteed to be present

    # Get the emotion scores by calling the emotion_detection method
    response = emotion_detector(text_to_analyze)

    # Extract the emotion scores and dominant emotion from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Create the formatted result string
    formatted_result = (
        f"For the given statement, the system response is 'anger' : {anger_score}, 'disgust' : {disgust_score}, "
        f"'fear' : {fear_score}, 'joy' : {joy_score} and 'sadness' : {sadness_score}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    # Return the formatted result directly as the response
    return formatted_result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
