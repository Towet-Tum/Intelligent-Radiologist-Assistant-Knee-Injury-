from ultralytics import YOLO 
from IntelligentRadiologistAssistant.config.configuration import ConfigurationManager

class Training:
    
    def model_train_val(self):
        config = ConfigurationManager()
        save_dir, data, epochs, imgsz = config.training_config()
        model = YOLO('yolov8n.pt')
        results = model.train(data=data, epochs=epochs, imgsz=imgsz, save_dir=save_dir)
        metrics = model.val()
        return results, metrics