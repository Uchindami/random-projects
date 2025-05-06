# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-classification", model="swarupt/industry-classification")

# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("swarupt/industry-classification")
model = AutoModelForSequenceClassification.from_pretrained("swarupt/industry-classification")

label = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
label("Consumers enjoy PepsiCo products more than one billion times a day in more than 200 countries and territories. In 2023, PepsiCo generated more than $91 billion in net revenue, driven by a complementary beverage and convenient foods portfolio that includes Lay’s, Doritos, Cheetos, Gatorade, Pepsi-Cola, Mountain Dew, Quaker and SodaStream.")
