from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout


# define model architecture

# Initialize model
model = Sequential()

# LSTM layer 1
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(Dropout(0.25))

# LSTM layer 2
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.25))

# LSTM layer 3
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.25))

# LSTM layer 4
model.add(LSTM(units=50))
model.add(Dropout(0.25))

# final layer
model.add(Dense(units=1))
model.summary()
