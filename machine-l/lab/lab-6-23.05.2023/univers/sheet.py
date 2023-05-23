import random

import numpy as np
from keras.models import load_model
import pandas as pd

np.random.seed(1)
size = 10

math = np.random.normal(175, 15, size)
eng = np.random.normal(175, 15, size)
ukr = np.random.normal(175, 15, size)
ben = random.choices([0, 1], [80, 20], k=size)

students = [[math, eng, ukr, ben] for math, eng, ukr, ben in zip(math, eng, ukr, ben) if
            math <= 200 and eng <= 200 and ukr <= 200]

model = load_model("./univers.h5")

labels = model.predict(students)

students = [[labels[i][0]] + student for i, student in enumerate(students)]

student_names = [
    "John",
    "Emily",
    "Michael",
    "Sarah",
    "David",
    "Emma",
    "Daniel",
    "Olivia",
    "Matthew",
    "Sophia"
]

surnames = [
    "Smith",
    "Johnson",
    "Williams",
    "Brown",
    "Jones",
    "Miller",
    "Davis",
    "Garcia",
    "Rodriguez",
    "Wilson"
]

students = [[random.choice(student_names), random.choice(surnames)] + student for i, student in enumerate(students)]

students = np.array(students)

df = pd.DataFrame(students, columns=['name', 'surname', 'chance', 'math', 'eng', 'ukr', 'benefit'])

df.to_excel('test.xlsx')
