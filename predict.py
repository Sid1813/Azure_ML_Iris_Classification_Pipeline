import joblib

model = joblib.load("outputs/iris_model.pkl")

sample = [[5.1, 3.5, 1.4, 0.2]]

prediction = model.predict(sample)

print(f"Predicted class: {prediction[0]}")