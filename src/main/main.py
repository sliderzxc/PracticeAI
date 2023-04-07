from keras.models import Sequential
from keras.layers import Dense
import numpy as np
from src.image.handle_image import HandleImage

# Задаємо набір даних для тренування
# RGB значення кожного кольору та його відповідний індекс
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

# Розділяємо дані на вхідні (RGB) та вихідні (індекс кольору) значення
X = colors[:, :3]  # Вхідні значення - перші 3 стовпці (RGB)
y = colors[:, 3]  # Вихідні значення - останній стовпець (індекс кольору)

# Створюємо модель нейронної мережі
model = Sequential()


def creating_model():
    model.add(Dense(units=64, activation='relu', input_dim=3))
    model.add(Dense(units=32, activation='relu'))
    model.add(Dense(units=16, activation='relu'))
    model.add(Dense(units=12, activation='softmax'))


def training_model():
    # Компілюємо модель
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(X, y, epochs=2500, batch_size=8)


def testing_photo(image_path):
    r, g, b = HandleImage.handle(image_path)
    predicted_indices = np.argmax(model.predict([[r, g, b]]), axis=-1)
    print(f'Найбільш популярний колір на фото: {colors_names[predicted_indices[0]]}\n')


def main():
    creating_model()
    training_model()
    for i in range(20):
        testing_photo("utils/images/sky.jpg")


main()
