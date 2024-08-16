
import joblib
from django.db import models

# Pre-trained model loaded for fake review detection
class ReviewClassifier:
    def __init__(self):
        self.model = joblib.load('api/ml_model.pkl')  # Assuming the model is stored in 'api/ml_model.pkl'
    
    def predict(self, review_text):
        # Process the review text and predict if it's fake or real
        return self.model.predict([review_text])[0]  # Returns the prediction

class Reviews(models.Model):
    user = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    rating = models.CharField(max_length=5)
    review = models.CharField(max_length=100000000000000)
    url = models.CharField(max_length=255)
    is_fake = models.BooleanField(default=False)  # New field to store fake/real classification
    objects = models.Manager()

    def save(self, *args, **kwargs):
        # Perform fake review detection before saving
        classifier = ReviewClassifier()
        self.is_fake = classifier.predict(self.review)
        super(Reviews, self).save(*args, **kwargs)

    def __str__(self):
        return self.url

class User_Credentials(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=1000)
    objects = models.Manager()

    def __str__(self):
        return self.email
