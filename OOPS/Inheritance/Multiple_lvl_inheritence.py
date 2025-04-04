class Father():
    height = 5.8
    physique = "bulk"
    
class Mother():
    color = "white"
    eye_color = "brown"

class child(Father, Mother):
    def display(self):
        print("Height = ",self.height)
        print("physique = ",self.physique)
        print("color = ",self.color)
        print("eye_color = ",self.eye_color)

print("Baby characters are .... ")
obj = child()
obj.display()
