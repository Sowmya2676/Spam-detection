import pandas as pd

# Load dataset
df = pd.read_csv("spam.csv", encoding="latin-1")

# Keep only useful columns
df = df[["v1", "v2"]]

# Rename columns
df.columns = ["label", "message"]

# Convert labels to numbers
df["label"] = df["label"].map({
    "ham": 0,
    "spam": 1
})

print(df.head())

print("\nShape:")
print(df.shape)

print("\nLabel counts:")
print(df["label"].value_counts())

X = df["message"]
y = df["label"]

print("\nFirst message:")
print(X.iloc[0])

print("\nFirst label:")
print(y.iloc[0])

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words="english")

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print("\nTF-IDF shape:", X_train_tfidf.shape)


from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()

model.fit(X_train_tfidf, y_train)


y_pred = model.predict(X_test_tfidf)

from sklearn.metrics import accuracy_score, classification_report

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

sample_messages = [
    "Congratulations! You won a free iPhone. Claim now!",
    "Hey, are we meeting tomorrow at 10 AM?"
]

sample_tfidf = vectorizer.transform(sample_messages)

predictions = model.predict(sample_tfidf)

for message, prediction in zip(sample_messages, predictions):
    result = "Spam" if prediction == 1 else "Ham"

    print("\nMessage:", message)
    print("Prediction:", result)

import joblib

joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("\nModel and vectorizer saved successfully!")    