import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.naive_bayes import MultinomialNB

from sklearn.pipeline import Pipeline

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


# Load dataset
data = pd.read_csv(
    "data/career_data.csv"
)

# Features and Labels
X = data["skills"]

y = data["career"]


# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.2,

    random_state=42
)


# ML Pipeline
model = Pipeline([

    ("tfidf", TfidfVectorizer()),

    ("classifier", MultinomialNB())

])


# Train Model
model.fit(X_train, y_train)


# Predictions
y_pred = model.predict(X_test)


# Accuracy
accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nModel Accuracy:\n")

print(f"{accuracy * 100:.2f}%")



# Classification Report
print("\nClassification Report:\n")

print(

    classification_report(
        y_test,
        y_pred
    )
)


# Confusion Matrix
print("\nConfusion Matrix:\n")

print(

    confusion_matrix(
        y_test,
        y_pred
    )
)


# Save Model
with open(
    "models/career_model.pkl",
    "wb"
) as file:

    pickle.dump(model, file)


print("\nModel Trained Successfully")