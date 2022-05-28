class Student:
    name = ""
    score = 0
    track = [""]
    score = 0.0
    def change_name(self, name):
        self.name
        print("\n\nStudent name: ", name)

    def change_age(self, age):
        self.age
        print("\nStudent name: ", age)
        
    def add_track(self, track):
        self.track
        print("\nStudent track: ", track)

    def get_score(self, score):
        self.score
        print("\nStudent score: ", score)
        
    def __init__(self, name, age, track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score

    def setDetails(self):
         print("Student name: ",self.name,"\nStudent age: ",self.age,"\nStudent track",self.track,"\nStudent score: ",self.score)
         
Bob = Student(name="Bob", age=26, track=["FE","BE"],score=20.90)
Bob.setDetails()

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(0.0)

        
