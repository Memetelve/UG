from ultralytics import YOLO
import torch


model_config = "data/data.yaml"
model_weights = "yolo.pt"

# training params
batch_size = 8
epochs = 100
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device} for training")

train_img_dir = "data/train/images"
train_label_dir = "data/train/labels"

val_img_dir = "data/val/images"
val_label_dir = "data/val/labels"

# Initialize model
model = YOLO()

# Train model
model.train(
    data=model_config,
    epochs=epochs,
    batch=batch_size,
    imgsz=640,
    project="runs/train",
    name="exp",
)

# Evaluate model
results = model.evaluate(
    img_dir=val_img_dir,
    label_dir=val_label_dir,
    batch_size=batch_size,
    img_size=640,
)
