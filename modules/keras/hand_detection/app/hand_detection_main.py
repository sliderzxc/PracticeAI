from modules.keras.hand_detection.domain.ai.hand_detection import HandDetectionAI


def main():
    hand_detection = HandDetectionAI()

    hand_detection.create_model()
    hand_detection.training_model()
    hand_detection.save_model()


if __name__ == "__main__":
    main()
