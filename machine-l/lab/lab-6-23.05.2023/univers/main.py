import random

import numpy as np
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import RandomUnderSampler
import tensorflow as tf

np.random.seed(1)
size = 100

math = np.random.normal(175, 15, size)
eng = np.random.normal(175, 15, size)
ukr = np.random.normal(175, 15, size)
ben = random.choices([0, 1], [80, 20], k=size)

students = [[math, eng, ukr, ben] for math, eng, ukr, ben in zip(math, eng, ukr, ben) if
            math <= 200 and eng <= 200 and ukr <= 200]

weights = [0.4, 0.3, 0.3]

students = [[sum(student[i] * weight for i, weight in enumerate(weights))] + student for student in students]

students = sorted(students, key=lambda x: (-x[4], -x[0]))

size = len(students)
labels = np.zeros(size)
good_size = size * 350 / 1500
ben_size = size * 0.05

for i, student in enumerate(students):
    if good_size < 0:
        break
    if student[4] == 1:
        if student[0] > 144 and student[1] > 120 and student[2] > 120 and student[3] > 120 and ben_size > 0:
            labels[i] = 1
            ben_size -= 1
            good_size -= 1
    else:
        if student[0] > 160 and student[1] > 140:
            labels[i] = 1
            good_size -= 1

for student, label in zip(students, labels):
    print(student, label)

data = [student[1:] for student in students]

data = np.array(data)
labels = np.array(labels)

under_sampler = RandomUnderSampler(sampling_strategy='majority', random_state=42)

resampled_data, resampled_labels = under_sampler.fit_resample(data, labels)

train_data, test_data, train_labels, test_labels = train_test_split(resampled_data, resampled_labels,
                                                                    test_size=0.2, random_state=42)

unique_classes, class_counts = np.unique(train_labels, return_counts=True)
print("Class Distribution in Training Set:")
for class_label, count in zip(unique_classes, class_counts):
    print("Class {}: {} samples".format(class_label, count))

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1000, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(1000, activation='relu', ),
    tf.keras.layers.Dense(1000, activation='relu', ),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(train_data, train_labels, epochs=150, batch_size=50)

test_loss, test_accuracy = model.evaluate(test_data, test_labels)

# Print the test accuracy
print("Test Accuracy: {:.2f}%".format(test_accuracy * 100))
# model.save('univers.h5')
