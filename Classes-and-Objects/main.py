from ast import Param

class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = str(tracks)
        self.score = float(score)

    def change_name(abc, name):
        abc.name = name
        return name

    def change_age(abc, age):
        abc.age = age
        return age

    def add_tracks(abc, tracks):
        abc.tracks = tracks
        return tracks

    def get_score(abc, score):
        abc.score = score
        return score

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name(str("Peter"))
Bob.change_age(int(34))
Bob.add_tracks(["UI/UX"])
Bob.get_score(float(87))

print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.score)

