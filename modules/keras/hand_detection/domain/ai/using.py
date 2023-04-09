import cv2
import numpy as np
from keras.models import load_model

model = load_model('C:\Programming\AI\GitHub\TheMostColorAI\modules\keras\hand_detection\model\hand_detection_model.h5')
cap = cv2.VideoCapture(0)

while True:
    success, image = cap.read()
    cv2.imshow("WebCamera", image)
    image = cv2.resize(image, (650, 1000))
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image)

    class_index = int(prediction[0][0] + 0.5)

    print("class index =", class_index)

    if class_index == 0:
        label = 'Without Hands'
        print('Without Hands')
    else:
        label = 'With Hands'
        print('With Hands')

    print()
    cv2.putText(image, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
