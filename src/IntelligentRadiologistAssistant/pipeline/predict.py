import torch
from ultralytics import YOLO 
import os 


class PredictPipeline:
    def __init__(self, filename):
        self.filename = filename 

    def predict(self):
        model = YOLO(os.path.join("Intelligent-Radiologist-Assistant-Knee-Injury-", "runs", "weights", "best.pt"))
        image = self.filename
        results = model.predict(image)
        