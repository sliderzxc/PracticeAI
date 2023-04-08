from src.domain.image.handle_image import HandleImage
from keras.models import Sequential
from keras.layers import Dense
import numpy as np


class FindTheMostUsingColorAI:
    colors = np.array([
        [255, 0, 0, 0],  # Червоний - 0
        [0, 255, 0, 1],  # Зелений - 1
        [0, 0, 255, 2],  # Синій - 2
        [255, 255, 0, 3],  # Жовтий - 3
        [255, 0, 255, 4],  # Фіолетовий - 4
        [0, 255, 255, 5],  # Бірюзовий - 5
        [255, 255, 255, 6],  # Білий - 6
        [0, 0, 0, 7],  # Чорний - 7
        [128, 128, 128, 8],  # Сірий - 8
        [128, 0, 0, 9],  # Темно-червоний - 9
        [0, 128, 0, 10],  # Темно-зелений - 10
        [0, 0, 128, 11]  # Темно-синій - 11
    ])

    colors_names = [
        'Червоний',
        'Зелений',
        'Синій',
        'Жовтий',
        'Фіолетовий',
        'Бірюзовий',
        'Білий',
        'Чорний',
        'Сірий',
        'Темно-червоний',
        'Темно-зелений',
        'Темно-синій',
    ]

    x = colors[:, :3]
    y = colors[:, 3]

    model = Sequential()

    @staticmethod
    def creating_model(model):
        model.add(Dense(units=64, activation='relu', input_dim=3))
        model.add(Dense(units=32, activation='relu'))
        model.add(Dense(units=16, activation='relu'))
        model.add(Dense(units=12, activation='softmax'))

    @staticmethod
    def training_model(model, x, y):
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        model.fit(x, y, epochs=2500, batch_size=8)

    @staticmethod
    def save_model(model):
        model.save('model/ai_model.h5')

    @staticmethod
    def testing_photo(image_path, model, colors_names):
        r, g, b = HandleImage.handle(image_path)
        predicted_indices = np.argmax(model.predict([[r, g, b]]), axis=-1)
        print(f'The most using color on photo is: {colors_names[predicted_indices[0]]}\n')
