'''
    These module is used to define routes for the Flask app
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# Route to render the index page
@app.route("/")
def render_index_page():
    '''
        This route returns the index.html for rendering
    '''
    return render_template('index.html')

@app.route("/emotionDetector", methods=['GET'])
def emotion_detection():
    '''
        This route the emotion_detection function.
        Gets the textToAnalyze input and process it.
        Returns the desired output
    '''

    # Get the text to analyze from the query parameters (from URL)
    text_to_analyze = request.args.get("textToAnalyze")  # Guaranteed to be present

    # Get the emotion scores by calling the emotion_detection method
    response = emotion_detector(text_to_analyze)

    # Return text if the dominant emotion is None
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extract the emotion scores and dominant emotion from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Create the formatted result string
    formatted_result = f"For the given statement, the system response is 'anger': {anger_score}, "
    formatted_result += f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and"
    formatted_result += f" 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."

    # Return the formatted result directly as the response
    return formatted_result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
