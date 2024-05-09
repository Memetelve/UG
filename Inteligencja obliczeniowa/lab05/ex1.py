import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import plot_model


# Load the iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# Preprocess the data

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Encode the labels
encoder = OneHotEncoder(sparse_output=False)
y_encoded = encoder.fit_transform(y.reshape(-1, 1))

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_encoded, test_size=0.3, random_state=42
)

# Define the model
model = Sequential(
    [
        Dense(64, activation="relu", input_shape=(X_train.shape[1],)),
        Dense(64, activation="relu"),
        Dense(y_encoded.shape[1], activation="softmax"),
    ]
)

# Compile the model
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])


# Train the model
history = model.fit(X_train, y_train, epochs=100, validation_split=0.2, batch_size=64)

# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")

# Plot the learning curve
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(history.history["accuracy"], label="train accuracy")
plt.plot(history.history["val_accuracy"], label="validation accuracy")
plt.title("Model accuracy")
plt.ylabel("Accuracy")
plt.xlabel("Epoch")
plt.grid(True, linestyle="--", color="grey")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history["loss"], label="train loss")
plt.plot(history.history["val_loss"], label="validation loss")
plt.title("Model loss")
plt.ylabel("Loss")
plt.xlabel("Epoch")
plt.grid(True, linestyle="--", color="grey")
plt.legend()

plt.tight_layout()
plt.show()
plt.savefig("learning_curve.png")

# Save the model
model.save("iris_model.keras")
# Plot and save the model architecture
plot_model(model, to_file="model_plot.png", show_shapes=True, show_layer_names=True)


# a) StandardScaler standaryzuje dane liczbowe poprzez usuwanie średniej i skalowanie do jednostkowej wariancji.
#    Transformacja danych liczbowych polega na odjęciu średniej od każdej cechy i podzieleniu przez odchylenie standardowe.
#    Możemy użyć StandardScaler w celu dostosowania danych treningowych i testowych do tego samego zakresu.

# b) OneHotEncoder służy do kodowania „one hot”, co oznacza przekształcanie zmiennych kategorycznych na postać binarną,
#    gdzie każda etykieta klasy staje się wektorem, w którym jedno z wymiarów jest ustawione na 1, a reszta na 0.
#    Na przykład, jeśli mamy trzy klasy: "a", "b" i "c", to "a" może być zakodowane jako [1, 0, 0], "b" jako [0, 1, 0],
#    a "c" jako [0, 0, 1]. OneHotEncoder przekształca etykiety klas na tę formę.

# c) Warstwa wejściowa ma tyle neuronów, ile cech (kolumn) ma zbiór danych treningowych. X_train.shape[1] to liczba cech
#    w danych treningowych. Warstwa wyjściowa ma tyle neuronów, ile klas chcemy przewidzieć. y_encoded.shape[1] to liczba
#    klas w przekształconych etykietach klas.

# d) Relu wydaje sie najlepsza opcja

# e) Tal, daja rozne wyniki, mozemy

# f) batch_size = <int>, im mniejsza wartosc tym bardziej "jittery" jest learning curve

# g) jest dosc dobrze, nie tracimy na celnosci modelu

# h) Dotrenowujemy model przez dodatkowe 10 epok
