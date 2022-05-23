class Staff(object):
    def __init__(self,a,b,c,d):
        self.firstName = a
        self.lastName = b
        self.location = c
        self.role = d

    def output(self):
        print(self.firstName,self.lastName,'is the',self.role,'of',self.location)

a = Staff('Rob','Young','Edinburgh','faculty')
a.output()