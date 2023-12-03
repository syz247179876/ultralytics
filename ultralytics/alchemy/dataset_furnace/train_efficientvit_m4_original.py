"""
YoloV8 baseline + EfficientViT(backbone) 原版作为backbone
"""
from ultralytics.models import YOLO
from ultralytics.alchemy.settings import *

if __name__ == '__main__':
    model = YOLO('yolov8-EfficientVit-M4-backbone.yaml')
    model.train(data=DATASET_EXDARK, epochs=300, batch=32, lr0=0.05,
                name=f'train-{DATASET_EXDARK}-EfficientVit-M4-backbone')