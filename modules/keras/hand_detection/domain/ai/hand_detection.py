from keras import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from keras.preprocessing.image import ImageDataGenerator


class HandDetectionAI:
    def __init__(self):
        self.data_dir = 'C:/Programming/AI/LearnAI/Hands/Hands'
        self.model = Sequential()

    def create_model(self):
        self.model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(1600, 1200, 3)))
        self.model.add(MaxPooling2D((2, 2)))
        self.model.add(Conv2D(64, (3, 3), activation='relu'))
        self.model.add(MaxPooling2D((2, 2)))
        self.model.add(Flatten())
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(1, activation='sigmoid'))

    def training_model(self):
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    def save_model(self):
        self.model.save("C:/Programming/AI/GitHub/TheMostColorAI/modules/keras/hand_detection/model/hand_detection_model.h5")
