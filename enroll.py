class Course:
    def enroll(self):
        print("You are enrolled in a general course.")

class Engineering(Course):
    def enroll(self):
        print("You are enrolled in a programming course with coding practice.")

class ArtCourse(Course):
    def enroll(self):
        print("You are enrolled in an art course with drawing assignments.")


p = Engineering()
a = ArtCourse()
p.enroll()  
a.enroll()  
