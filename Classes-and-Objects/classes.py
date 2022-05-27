from ast import Param


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name, self.age, self.score = name, age, score
        self.track = tracks
        
    def change_name(self,param):
        self.name = param
       
    def change_age(self,param):
        self.age = param 
      
    def add_track(self,param):
        self.track.append(param)
      
    def get_score(self):
        return self.score



Bob = Student("Bob",26,["FE","BE"],20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(self,param)


