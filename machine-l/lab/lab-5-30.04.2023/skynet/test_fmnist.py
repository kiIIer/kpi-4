import cv2
import numpy as np
from keras.models import load_model

model = load_model('fmnist.h5')

img = cv2.imread('../assets/t-shirt.png')

img = cv2.resize(img, (28, 28))

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = img.reshape((1, 28, 28, 1))

img = img / 255.0

predictions = model.predict(img)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

for i in range(len(class_names)):
    class_prob = predictions[0][i] * 100
    print(class_names[i], '=', '{:.2f}%'.format(class_prob))
