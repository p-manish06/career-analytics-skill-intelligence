import pickle


# Load trained model
with open("models/career_model.pkl", "rb") as file:

    model = pickle.load(file)


def predict_career(skills):

    skills_text = " ".join(skills)

    prediction = model.predict([skills_text])

    return prediction[0]