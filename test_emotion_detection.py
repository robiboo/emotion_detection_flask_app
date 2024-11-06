import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        '''
        This function test the function, emotion_detector, whether it returns the appropriate emotion detected.
        '''
        
        test_joy = emotion_detector("I am glad this happened")
        self.assertEqual(test_joy["dominant_emotion"], 'joy')

        test_anger = emotion_detector("I am really mad about this")
        self.assertEqual(test_anger["dominant_emotion"], 'anger')

        test_disgust = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(test_disgust["dominant_emotion"], 'disgust')

        test_sadness = emotion_detector("I am so sad about this")
        self.assertEqual(test_sadness["dominant_emotion"], 'sadness')

        test_fear = emotion_detector("I am reall afraid that this will happen")
        self.assertEqual(test_fear["dominant_emotion"], 'fear')

unittest.main()