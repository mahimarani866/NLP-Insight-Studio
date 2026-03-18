from textblob import TextBlob
import spacy


class API:

    def __init__(self):
        # Load spaCy model for NER
        try:
            self.nlp = spacy.load('en_core_web_sm')
        except:
            print("⚠️  spaCy model not found. Run: python -m spacy download en_core_web_sm")
            self.nlp = None

        # Emotion keywords for simple emotion detection
        self.emotion_keywords = {
            'joy': ['happy', 'joy', 'joyful', 'excited', 'wonderful', 'great', 'love', 'excellent',
                    'amazing', 'fantastic', 'delighted', 'pleased', 'cheerful', 'glad', 'thrilled'],
            'sadness': ['sad', 'unhappy', 'depressed', 'miserable', 'sorry', 'disappointed',
                        'hurt', 'lonely', 'heartbroken', 'blue', 'down', 'gloomy', 'sorrow'],
            'anger': ['angry', 'mad', 'furious', 'annoyed', 'irritated', 'hate', 'rage',
                      'upset', 'outraged', 'infuriated', 'hostile', 'bitter'],
            'fear': ['scared', 'afraid', 'terrified', 'worried', 'anxious', 'nervous', 'fear',
                     'frightened', 'panic', 'alarmed', 'concerned', 'uneasy'],
            'surprise': ['surprised', 'shocked', 'amazed', 'astonished', 'unexpected', 'wow',
                         'incredible', 'unbelievable', 'startled', 'stunned'],
            'disgust': ['disgusting', 'gross', 'nasty', 'awful', 'terrible', 'horrible',
                        'revolting', 'repulsive', 'sick', 'yuck'],
            'love': ['love', 'adore', 'cherish', 'treasure', 'care', 'affection', 'fond',
                     'devoted', 'passion', 'romance']
        }

    def sentiment_analysis(self, text):
        """Analyze sentiment using TextBlob"""
        try:
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity  # -1 to 1
            subjectivity = blob.sentiment.subjectivity  # 0 to 1

            if polarity > 0.1:
                sentiment = "Positive"
            elif polarity < -0.1:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

            return {
                'sentiment': {
                    'sentiment': sentiment,
                    'confidence': round(abs(polarity), 2),
                    'polarity': round(polarity, 2),
                    'subjectivity': round(subjectivity, 2)
                }
            }
        except Exception as e:
            raise Exception(f"Sentiment analysis failed: {str(e)}")

    def ner(self, text):
        """Named Entity Recognition using spaCy"""
        if not self.nlp:
            raise Exception("spaCy model not loaded. Please install: python -m spacy download en_core_web_sm")

        try:
            doc = self.nlp(text)

            entities = {}
            for ent in doc.ents:
                if ent.label_ not in entities:
                    entities[ent.label_] = []
                if ent.text not in entities[ent.label_]:  # Avoid duplicates
                    entities[ent.label_].append(ent.text)

            return {
                'entities': entities
            }
        except Exception as e:
            raise Exception(f"NER failed: {str(e)}")

    def emotion_prediction(self, text):
        """Simple emotion prediction using keyword matching"""
        try:
            text_lower = text.lower()
            emotion_scores = {}

            # Count emotion keywords in text
            for emotion, keywords in self.emotion_keywords.items():
                score = sum(1 for keyword in keywords if keyword in text_lower)
                if score > 0:
                    emotion_scores[emotion] = score

            # If no emotions detected, use sentiment as fallback
            if not emotion_scores:
                blob = TextBlob(text)
                polarity = blob.sentiment.polarity

                if polarity > 0.3:
                    emotion_scores['joy'] = 0.7
                elif polarity > 0:
                    emotion_scores['joy'] = 0.4
                elif polarity < -0.3:
                    emotion_scores['sadness'] = 0.7
                elif polarity < 0:
                    emotion_scores['sadness'] = 0.4
                else:
                    emotion_scores['neutral'] = 0.5
            else:
                # Normalize scores
                total = sum(emotion_scores.values())
                emotion_scores = {k: round(v / total, 2) for k, v in emotion_scores.items()}

            # Sort by score
            emotion_scores = dict(sorted(emotion_scores.items(),
                                         key=lambda x: x[1],
                                         reverse=True))

            return {
                'emotion': emotion_scores
            }
        except Exception as e:
            raise Exception(f"Emotion prediction failed: {str(e)}")