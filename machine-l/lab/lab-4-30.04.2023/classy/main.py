import matplotlib.pyplot as plt
from onedal.svm import SVC
from sklearn.datasets import load_digits
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

digits = load_digits()

figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(6, 4))

for item in zip(axes.ravel(), digits.images, digits.target):
    axes, image, target = item
    axes.imshow(image, cmap=plt.cm.gray_r)

    axes.set_xticks([])
    axes.set_yticks([])

    axes.set_title(target)
plt.tight_layout()

X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, random_state=11, test_size=0.2)

print(X_train.shape)
print(X_test.shape)

knn = KNeighborsClassifier(n_neighbors=7)

knn.fit(X=X_train, y=y_train)

predicted = knn.predict(X=X_test)

expected = y_test

print(predicted[:20])
print(expected[:20])

print(f'{knn.score(X_test, y_test):.2%}')

confusion = confusion_matrix(y_true=expected, y_pred=predicted)

print(confusion)

names = [str(digit) for digit in digits.target_names]
print(classification_report(expected, predicted, target_names=names))
