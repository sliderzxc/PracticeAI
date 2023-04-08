from src.domain.ai.find_the_most_using_color_ai import FindTheMostUsingColorAI
from PyQt6.QtWidgets import QApplication
from src.ui.main_layout import MainLayout
from keras.models import load_model
import sys


def main():
    testing_model()


def testing_model():
    image_path = "C:/Programming/AI/GitHub/TheMostColorAI/utils/images/test_image_1.jpg"
    FindTheMostUsingColorAI.testing_photo(image_path, load_model("model/ai_model.h5"), FindTheMostUsingColorAI.colors_names)


# You can create a new AI model, for this simple delete old model from path: src/app/model/ai_model.h, and launch this function
def init_new_model():
    FindTheMostUsingColorAI.creating_model(FindTheMostUsingColorAI.model)
    FindTheMostUsingColorAI.training_model(FindTheMostUsingColorAI.model, FindTheMostUsingColorAI.x, FindTheMostUsingColorAI.y)
    FindTheMostUsingColorAI.save_model(FindTheMostUsingColorAI.model)


if __name__ == '__main__':
    main()
