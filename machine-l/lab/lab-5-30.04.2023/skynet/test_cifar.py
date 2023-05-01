import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing import image

model = load_model('cifar.h5')

img = cv2.imread('../assets/car.jpeg')

img = cv2.resize(img, (32, 32))

cv2.imshow('CIFAR-10 Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = img / 255.0

img = np.expand_dims(img, axis=0)

predictions = model.predict(img)

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

for i in range(len(class_names)):
    class_prob = predictions[0][i] * 100
    print(class_names[i], '=', '{:.2f}%'.format(class_prob))