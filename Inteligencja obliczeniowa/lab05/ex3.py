from os import listdir

import tensorflow as tf
from keras.api.callbacks import (
    EarlyStopping,
    History,
    ModelCheckpoint,
    ReduceLROnPlateau,
)
from keras.api.layers import (
    BatchNormalization,
    Conv2D,
    Dense,
    Dropout,
    Flatten,
    MaxPooling2D,
)
from keras.api.models import Sequential
from keras.api.optimizers import SGD
from keras.api.preprocessing.image import img_to_array, load_img
from numpy import asarray, load, save
from sklearn.model_selection import train_test_split

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
    "ex3.keras", monitor="val_accuracy", save_best_only=True
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

model.evaluate(test_photos, test_labels)
