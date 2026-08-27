from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os


# 1. Load the Iris dataset
iris = load_iris()

X = iris.data
y = iris.target


# 2. Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 3. Train the model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


# 4. Evaluate the model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy:.2f}")


# 5. Save the trained model
os.makedirs("outputs", exist_ok=True)

joblib.dump(
    model,
    "outputs/iris_model.pkl"
)

print("Model saved to outputs/iris_model.pkl")