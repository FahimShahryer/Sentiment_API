from transformers import AutoModelForSequenceClassification

#download and save the huggingface pre-trained model locally for performance

model_name = "cardiffnlp/twitter-roberta-base-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model_directory = "myapp/model2"
