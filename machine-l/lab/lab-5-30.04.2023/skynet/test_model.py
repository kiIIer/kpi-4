from keras.models import load_model
import cv2

model = load_model('numberer.h5')

tst = 255 - cv2.imread('../assets/secret.jpg', 0)
tst = cv2.resize(tst, (28, 28))
tst = tst.reshape((1, 28 * 28))
tst = tst.astype('float32') / 255

pred = list(model.predict(tst)[0])
print(pred)
