# Import required modules and functions

from django.shortcuts import render
from rest_framework.decorators import api_view
from transformers import pipeline, AutoTokenizer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

# Load the pre-trained sentiment analysis model and tokenizer

from transformers import pipeline, AutoModelForSequenceClassification

model_directory = "myapp/models"
tokenizer = AutoTokenizer.from_pretrained(model_directory)
model = AutoModelForSequenceClassification.from_pretrained(model_directory)
classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Define the API view and specify the HTTP method(s) it accepts

@api_view(['POST'])
def sentiment_analysis(request):
    # Extract the 'text' field from the request data
    text = request.data.get('text')

    # Check if the 'text' field is missing or empty
    if not text:
        # Return a response indicating the error with an appropriate status code
        return Response(
            {"error": "Invalid input. 'text' field is required."},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Perform input validation by checking the length of the text
    max_text_length = 1000
    if len(text) > max_text_length:
        # Return a response indicating the error with an appropriate status code
        return Response(
            {"error": f"Invalid input. Maximum allowed text length is {max_text_length} characters."},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Make predictions on the input text using the pre-trained model
    preds = classifier(text)

    # Map the predicted label to human-readable sentiment names/ expected output format
    label_mapping = {
        "LABEL_0": "NEGATIVE",
        "LABEL_1": "NEUTRAL",
        "LABEL_2": "POSITIVE"
    }

    # Extract the predicted sentiment label and score from the predictions
    sentiment_label = preds[0]['label']
    sentiment_score = preds[0]['score']

    # Prepare the JSON response containing the predicted sentiment
    response_data = {
        "sentiment": label_mapping[sentiment_label.upper()]
    }

    # Return the JSON response with the predicted sentiment
    return Response(data=response_data)
