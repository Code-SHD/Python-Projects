from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import ModelCheckpoint

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import numpy as np

df = pd.read_csv("./data/Samsung_Stock.csv")
df = pd.get_dummies(df)
df = df.fillna(df.mean())
df_corr = df.corr()
df_corr_sort = df_corr.sort_values('High', ascending=False)

cols_train = ['Open']
X_train_pre = df[cols_train]

y = df['High'].values

X_train, X_test, y_train, y_test = train_test_split(X_train_pre, y, test_size=0.2)

model = Sequential()
model.add(Dense(10, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(30, activation='relu'))
model.add(Dense(40, activation='relu'))
model.add(Dense(30, activation='relu'))
model.add(Dense(1))
model.summary()

model.compile(optimizer='adam', loss='mean_squared_error')

ESC = EarlyStopping(monitor='val_loss', patience=50)

modelpath = "./model/samsung_stock.hdf5"
check_pointer = ModelCheckpoint(filepath=modelpath, monitor='val_loss', verbose=0, save_best_only=True)

history = model.fit(X_train, y_train, validation_split=0.25, epochs=2000, batch_size=64, callbacks=[ESC, check_pointer])

real_p = []
pred = []
x_num = []

n_iter = 0
y_pred = model.predict(X_test).flatten()
for i in range(25):
    real = y_test[i]
    prediction = y_pred[i]
    print("real: ", real, "pred: ", prediction)
    real_p.append(real)
    pred.append(prediction)
    n_iter = n_iter + 1
    x_num.append(n_iter)

plt.plot(x_num, pred, label="pred")
plt.plot(x_num, real_p, label="real")
plt.legend()
plt.show()
