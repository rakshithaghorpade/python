class Student:
    def init(self,sid,age,marks):
        self.sid=sid
        self.age=age
        self.marks=marks
    def validate_marks(self):
        if self.marks<0 and self.marks>100:
            return False
        else:
            return True
    def validate_age(self):
        if self.age>20:
            return True
        else:
            return False
    def setValue(self,s,a,m):
        self.sid=s
        self.age=a
        self.marks=m
    def getvalue(self):
        return self.sid,self.age,self.marks
    def check(self):
        if self.marks>65:
            print("eligible")
        else:
            print("not eligible")
        
a=Student()
a.setValue(12,24,87)
print("sid: ",a.sid," age: ",a.age," marks: ",a.marks)
y=a.validate_marks()
x=a.validate_age()
if x==True and y==True:
    a.check()
else:
    print("not eligible")
    
        
        
