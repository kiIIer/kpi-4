import numpy as np
from keras.models import load_model

model = load_model("./univers.h5")


class Student:
    def __init__(self, name, math, ukr, eng, bonus):
        self.bonus = bonus
        self.eng = eng
        self.ukr = ukr
        self.math = math
        self.name = name


me = Student("Mike", 191, 182, 193, 0)
super = Student("Super", 200, 200, 200, 0)
good = Student("Good", 180, 180, 180, 1)
average = Student("Average", 175, 175, 175, 0)
bad = Student("Bad", 150, 150, 150, 0)
reallyBad = Student("REALLY bad", 0, 0, 0, 0)


def predict(student):
    # Make sure to reshape the data to add an extra dimension
    X = np.array([student.math, student.eng, student.ukr, student.bonus]).reshape(1, -1)
    print(student.name,
          model.predict(X))  # Also, the model's output is a probability. Let's convert it to a boolean value


predict(me)
predict(super)
predict(good)
predict(average)
predict(bad)
predict(reallyBad)
