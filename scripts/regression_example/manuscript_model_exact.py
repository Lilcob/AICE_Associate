import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Activation, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.utils import to_categorical
tf.keras.utils.set_random_seed(1)
# 딥러닝 모델 구성
model = Sequential([  # ①
   tf.keras.Input(shape=(X_train.shape[1],)),
   Dense(128, activation='relu'),
   Dense(64, activation='relu'),
   Dense(32, activation='relu'),
   Dropout(0.3),  # ②
   Dense(16, activation='relu'),
   Dense(1)
])
# 모델 컴파일
import tensorflow as tf
model.compile(optimizer='adam', loss='mean_squared_error', metrics=[tf.keras.metrics.MeanSquaredError(name='mse')])  # ③
# 모델 학습
history = model.fit(X_train, y_train,  # ④ ⑤ ⑥
                  epochs=50,
                  batch_size=32,
                  validation_data=(X_valid, y_valid))
