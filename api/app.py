from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

app = FastAPI(title="IRIS API")

# train a tiny model on startup (fast; keeps image simple)
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)
_model = RandomForestClassifier(n_estimators=100, random_state=42)
_model.fit(X_train, y_train)

class IrisIn(BaseModel):
    instances: list[list[float]]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(x: IrisIn):
    X = np.array(x.instances)
    return {"predictions": _model.predict(X).tolist()}
