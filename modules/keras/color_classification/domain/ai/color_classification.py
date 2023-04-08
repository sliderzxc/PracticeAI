from modules.keras.color_classification.data.colors import colors_names
from modules.keras.color_classification.data.colors import colors
from utils.constants import BASE_MODEL_PATH
from keras.models import Sequential
from keras.layers import Dense
import numpy as np


class ColorClassificationAI:
    x = colors.colors[:, :3]
    y = colors.colors[:, 3]

    model = Sequential()

    def creating_model(self):
        self.model.add(Dense(units=128, activation='relu', input_dim=3))
        self.model.add(Dense(units=100, activation='relu'))
        self.model.add(Dense(units=64, activation='relu'))
        self.model.add(Dense(units=32, activation='relu'))
        self.model.add(Dense(units=180, activation='softmax'))

    def training_model(self):
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        self.model.fit(self.x, self.y, epochs=5000, batch_size=800)

    def save_model(self):
        self.model.save(f"{BASE_MODEL_PATH}\keras\color_classification\model\color_classification_model.h5")

    @staticmethod
    def testing_model(model, r, g, b):
        predicted_indices = np.argmax(model.predict([[r, g, b]]), axis=-1)
        print(f'Color name is: {colors_names.colors_names[predicted_indices[0]]} | Color RGB is {r, g, b}\n')
