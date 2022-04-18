class Staff(object):
    def __init__(self,a,b,c,d):
        self.firstName = a
        self.lastName = b
        self.location = c
        self.role = d

a = Staff('young','robot','Edinburgh','faculty')

print('His first name is:',a.firstName,'\nHis last name is:',a.lastName)
print('His location is:',a.location,'\nHis role is:',a.role)