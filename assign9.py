######################
#### Polymorphism ####
######################
class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        if self.sword_type == "bronze" and other.sword_type == "bronze":
            return Sword("iron")
        if self.sword_type == "iron" and other.sword_type == "iron":
            return Sword("steel")
        else: 
            raise Exception("can't craft")

s1 = Sword("iron")
s2 = Sword("iron")

s3 = s1 + s2
print(s3.sword_type)
