import time
import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import torch
import torch.nn as nn
from sklearn.preprocessing import MinMaxScaler
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.metrics import mean_squared_error

plt.switch_backend("qtagg")

PLOT = False

AMZN = pd.read_csv("./data/AMZN.csv").sort_values("Date")

lookback = 30


print(AMZN.head())
print(AMZN.describe())
print(AMZN.info())
print(AMZN.isnull().sum())

# Plotting the data
if PLOT:
    plt.figure(figsize=(12, 6))
    plt.plot(AMZN["Date"], AMZN["Close"])
    plt.title("Amazon Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.show()

# Seasonal Decomposition
if PLOT:
    result = seasonal_decompose(AMZN["Close"], model="additive", period=365)
    result.plot()
    plt.show()

scaler = MinMaxScaler(feature_range=(0, 1))

price_amazon = AMZN[["Close"]]
print(price_amazon.head())


price_amazon["Close"] = scaler.fit_transform(
    price_amazon["Close"].values.reshape(-1, 1)
)

print(price_amazon.head())


def split_data(stock, split_ratio, lookback):
    data_raw = stock.to_numpy()

    data = [
        data_raw[index : index + lookback] for index in range(len(data_raw) - lookback)
    ]

    data = np.array(data)
    test_set_size = int(np.round((1 - split_ratio) * data.shape[0]))
    train_set_size = data.shape[0] - (test_set_size)

    x_train = data[:train_set_size, :-1, :]
    y_train = data[:train_set_size, -1, :]

    x_test = data[train_set_size:, :-1, :]
    y_test = data[train_set_size:, -1, :]

    return [x_train, y_train, x_test, y_test]


train_X, train_y, test_X, test_y = split_data(price_amazon, 0.8, lookback)

print(train_X.shape)
print(train_y.shape)
print(test_X.shape)
print(test_y.shape)


x_train = torch.from_numpy(train_X).type(torch.Tensor)
x_test = torch.from_numpy(test_X).type(torch.Tensor)
y_train_gru = torch.from_numpy(train_y).type(torch.Tensor)
y_test_gru = torch.from_numpy(test_y).type(torch.Tensor)


class GRU(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_layers, output_dim):
        super(GRU, self).__init__()
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers

        self.gru = nn.GRU(input_dim, hidden_dim, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_dim).requires_grad_()
        out, (hn) = self.gru(x, (h0.detach()))
        out = self.fc(out[:, -1, :])
        return out


input_dim = 1
hidden_dim = 32
num_layers = 2
output_dim = 1
num_epochs = 110


model = GRU(
    input_dim=input_dim,
    hidden_dim=hidden_dim,
    output_dim=output_dim,
    num_layers=num_layers,
)
criterion = torch.nn.MSELoss(reduction="mean")
optimiser = torch.optim.Adam(model.parameters(), lr=0.01)

hist = np.zeros(num_epochs)
start_time = time.time()
gru = []

for t in range(num_epochs):
    y_train_pred = model(x_train)

    loss = criterion(y_train_pred, y_train_gru)
    print("Epoch ", t, "MSE: ", loss.item())
    hist[t] = loss.item()

    optimiser.zero_grad()
    loss.backward()
    optimiser.step()


training_time = time.time() - start_time
print(f"Training time: {training_time * 1000:2f}ms")

predict = pd.DataFrame(scaler.inverse_transform(y_train_pred.detach().numpy()))
original = pd.DataFrame(scaler.inverse_transform(y_train_gru.detach().numpy()))

if PLOT:
    sns.set_style("darkgrid")

    fig = plt.figure()
    fig.subplots_adjust(hspace=0.2, wspace=0.2)

    plt.subplot(1, 2, 1)
    ax = sns.lineplot(x=original.index, y=original[0], label="Data", color="royalblue")
    ax = sns.lineplot(
        x=predict.index, y=predict[0], label="Training Prediction (GRU)", color="tomato"
    )
    ax.set_title("Amazon stock price", size=14, fontweight="bold")
    ax.set_xlabel("Days", size=14)
    ax.set_ylabel("Cost (USD)", size=14)
    ax.set_xticklabels("", size=10)

    plt.subplot(1, 2, 2)
    ax = sns.lineplot(data=hist, color="royalblue")
    ax.set_xlabel("Epoch", size=14)
    ax.set_ylabel("Loss", size=14)
    ax.set_title("Training Loss", size=14, fontweight="bold")
    fig.set_figheight(6)
    fig.set_figwidth(16)

y_test_pred = model(x_test)

# invert predictions
y_train_pred = scaler.inverse_transform(y_train_pred.detach().numpy())
y_train = scaler.inverse_transform(y_train_gru.detach().numpy())
y_test_pred = scaler.inverse_transform(y_test_pred.detach().numpy())
y_test = scaler.inverse_transform(y_test_gru.detach().numpy())

# calculate root mean squared error
trainScore = math.sqrt(mean_squared_error(y_train[:, 0], y_train_pred[:, 0]))
print("Train Score: %.2f RMSE" % (trainScore))
testScore = math.sqrt(mean_squared_error(y_test[:, 0], y_test_pred[:, 0]))
print("Test Score: %.2f RMSE" % (testScore))
gru.extend((trainScore, testScore, training_time))
# shift train predictions for plotting
trainPredictPlot = np.empty_like(price_amazon)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[lookback : len(y_train_pred) + lookback, :] = y_train_pred

# shift test predictions for plotting
testPredictPlot = np.empty_like(price_amazon)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(y_train_pred) + lookback - 1 : len(price_amazon) - 1, :] = (
    y_test_pred
)

original = scaler.inverse_transform(price_amazon["Close"].values.reshape(-1, 1))

predictions = np.append(trainPredictPlot, testPredictPlot, axis=1)
predictions = np.append(predictions, original, axis=1)
result = pd.DataFrame(predictions)


if PLOT:
    plt.figure(figsize=(12, 6))
    plt.plot(result[0], color="royalblue")
    plt.plot(result[1], color="tomato")
    plt.plot(result[2], color="green")
    plt.title("Amazon Stock Price")
    plt.xlabel("Days")
    plt.ylabel("Close Price")
    plt.legend(["Train", "Test", "Original"], loc="upper left")
    plt.show()

# UP DOWN
# __ ____ UP
# __ ____ DOWN


predicted_changes = [0, 0, 0, 0]

for i in range(len(y_test)):

    predicted_change = y_test_pred[i] - y_test[i - 1]
    actual_change = y_test[i] - y_test[i - 1]

    if predicted_change > 0 and actual_change > 0:
        predicted_changes[0] += 1
    elif predicted_change < 0 and actual_change < 0:
        predicted_changes[1] += 1
    elif predicted_change > 0 and actual_change < 0:
        predicted_changes[2] += 1
    elif predicted_change < 0 and actual_change > 0:
        predicted_changes[3] += 1

    # print(f"Day {i}: Predicted={y_test_pred[i]} Actual={y_test[i]}")
    # print(f"Predicted change: {predicted_change}, Actual change: {actual_change}")

# create confusion matrix
confusion_matrix = np.array(
    [
        [predicted_changes[0], predicted_changes[2]],
        [predicted_changes[3], predicted_changes[1]],
    ]
)

if PLOT:
    # show confusion matrix
    sns.heatmap(
        confusion_matrix,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=["UP", "DOWN"],
        yticklabels=["UP", "DOWN"],
    )
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")

    plt.show()

# calculate accuracy
accuracy = (confusion_matrix[0, 0] + confusion_matrix[1, 1]) / np.sum(confusion_matrix)
print(f"Accuracy: {accuracy * 100:.2f}%")


# predict last 30 days and compare with actual

predicted_price = price_amazon[:-lookback].copy()

print(predicted_price)

for _ in range(30):
    x_predict = torch.from_numpy(
        predicted_price[-lookback:].values.reshape(1, lookback, 1)
    ).type(torch.Tensor)
    y_predict = model(x_predict)
    # y_predict = scaler.inverse_transform(y_predict.detach().numpy())

    predicted_price = predicted_price._append(
        pd.DataFrame(
            y_predict.detach(), columns=["Close"], index=[predicted_price.index[-1] + 1]
        )
    )

# x_predict = torch.from_numpy(
#     price_amazon[-lookback:].values.reshape(1, lookback, 1)
# ).type(torch.Tensor)
# y_predict = model(x_predict)
# y_predict = scaler.inverse_transform(y_predict.detach().numpy())


unscaled = scaler.inverse_transform(price_amazon["Close"].values.reshape(-1, 1))
predicted_price = scaler.inverse_transform(
    predicted_price["Close"].values.reshape(-1, 1)
)
print(predicted_price[-lookback - 10 : -lookback])
print(predicted_price[-lookback:])


if 1:
    plt.figure(figsize=(12, 6))
    plt.plot(unscaled, color="royalblue")
    plt.plot(predicted_price, color="tomato")
    plt.title("Amazon Stock Price")
    plt.xlabel("Days")
    plt.ylabel("Close Price")
    plt.legend(["Original", "Predicted"], loc="upper left")
    plt.show()
