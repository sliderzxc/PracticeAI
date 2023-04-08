from modules.keras.color_classification.domain.ai.color_classification import ColorClassificationAI
from keras.saving.saving_api import load_model
from utils.constants import BASE_MODEL_PATH
import random


# You can generate your new model using this method
def init_new_model():
    color_classification = ColorClassificationAI()

    color_classification.creating_model()
    color_classification.training_model()
    color_classification.save_model()


def testing_model():
    model = load_model(f"{BASE_MODEL_PATH}\keras\color_classification\model\color_classification_model.h5")
    ColorClassificationAI.testing_model(model, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def main():
    # init_new_model()
    testing_model()


if __name__ == "__main__":
    main()
