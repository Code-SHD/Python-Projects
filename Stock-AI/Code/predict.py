from tensorflow.keras.models import load_model
import numpy as np

model = load_model("Your Model Path")

_input = np.array([62900])

print(model.predict(_input))
