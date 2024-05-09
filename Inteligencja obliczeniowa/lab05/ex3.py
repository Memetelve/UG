import itertools
from os import listdir

import tensorflow as tf
from sklearn.metrics import confusion_matrix
import numpy as np
from numpy import asarray, load, save
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import (
    EarlyStopping,
    History,
    ModelCheckpoint,
    ReduceLROnPlateau,
)
from tensorflow.keras.layers import (
    BatchNormalization,
    Conv2D,
    Dense,
    Dropout,
    Flatten,
    MaxPooling2D,
)
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.preprocessing.image import img_to_array, load_img

# check if gpu is available
print(tf.config.list_physical_devices("GPU"))

if 0:
    photos, labels = [], []

    folder = "dogs-cats-mini"

    for file in listdir(folder):
        output = 0.0
        if file.startswith("cat"):
            output = 1.0
        photo = img_to_array(load_img(f"{folder}/{file}", target_size=(50, 50)))
        photos.append(photo)
        labels.append(output)

    for photo in photos:
        photo = tf.expand_dims(photo, axis=0)

    photos = asarray(photos)
    labels = asarray(labels)

    save("ex3_photos.npy", photos)
    save("ex3_labels.npy", labels)

photos = load("ex3_photos.npy")
labels = load("ex3_labels.npy")

print(photos.shape, labels.shape)


train_photos, test_photos, train_labels, test_labels = train_test_split(
    photos, labels, test_size=0.25
)

model = Sequential()

model.add(Conv2D(32, (3, 3), activation="relu", input_shape=(50, 50, 3)))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), activation="relu"))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, (3, 3), activation="relu"))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512, activation="relu"))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(2, activation="softmax"))  # 2 because we have cat and dog classes

model.compile(
    loss="categorical_crossentropy", optimizer="rmsprop", metrics=["accuracy"]
)

model.summary()

early_stop = EarlyStopping(patience=10)

learning_rate_reduction = ReduceLROnPlateau(
    monitor="val_acc", patience=2, verbose=1, factor=0.5, min_lr=0.00001
)

train_datagen = tf.data.Dataset.from_tensor_slices((train_photos, train_labels))
test_datagen = tf.data.Dataset.from_tensor_slices((test_photos, test_labels))


opt = SGD(learning_rate=0.001, momentum=0.9)
model.compile(optimizer=opt, loss="binary_crossentropy", metrics=["accuracy"])

history = History()
model_checkpoint = ModelCheckpoint(
    "ex3.model", monitor="val_accuracy", save_best_only=True
)

train_labels = tf.keras.utils.to_categorical(train_labels, num_classes=2)
test_labels = tf.keras.utils.to_categorical(test_labels, num_classes=2)


model.fit(
    train_photos,
    train_labels,
    epochs=20,
    validation_data=(test_photos, test_labels),
    callbacks=[history, model_checkpoint],
)


import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(history.history["accuracy"], label="accuracy")
plt.plot(history.history["val_accuracy"], label="val_accuracy")
plt.plot(history.history["loss"], label="loss")
plt.plot(history.history["val_loss"], label="val_loss")
plt.legend()
plt.savefig("ex3.png")
plt.show()

# confusion matrix using matplotlib
import matplotlib.pyplot as plt

# Assuming 'odel' and 'test_photos', 'test_labels' are defined in the previous code

# Make predictions
predictions = model.predict(test_photos)

# Convert predictions to binary labels
predicted_labels = np.argmax(predictions, axis=1)

# Create confusion matrix
cm = confusion_matrix(np.argmax(test_labels, axis=1), predicted_labels)

# Define labels for the confusion matrix
class_names = ["Cat", "Dog"]


# Plot confusion matrix
def plot_confusion_matrix(
    cm, classes, normalize=False, title="Confusion matrix", cmap=plt.cm.Blues
):
    if normalize:
        cm = cm.astype("float") / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print("Confusion matrix, without normalization")

    print(cm)

    plt.imshow(cm, interpolation="nearest", cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = ".2f" if normalize else "d"
    thresh = cm.max() / 2.0
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(
            j,
            i,
            format(cm[i, j], fmt),
            horizontalalignment="center",
            color="white" if cm[i, j] > thresh else "black",
        )

    plt.ylabel("True label")
    plt.xlabel("Predicted label")
    plt.tight_layout()


# Call the function to plot the confusion matrix
plot_confusion_matrix(cm, class_names)
plt.savefig("ex3_confusion_matrix.png")
plt.show()

model.evaluate(test_photos, test_labels)
