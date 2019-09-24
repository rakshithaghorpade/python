class CallDetail:
    def __init__(self, calledBy, calledTo, duration, typeCall):
        self.calledBy = calledBy
        self.calledTo = calledTo
        self.duration = duration
        self.typeCall = typeCall
    
    def displayDetails(self):
        print("Caller's Phone Number : ",self.calledBy)
        print("Receiver's Phone Number : ", self.calledTo)
        print("Duration of Call : ", self.duration)
        print("Call type : ", self.typeCall) 

class Util:
    def __init__(self):
        self.list_of_call_objects=None
    def parse_customer(self,listStr):
        callDetail = []
        for i in range(len(listStr)):
            print("CALL DETALS-",i+1)
            a = listStr[i].split(',')
            callDetail.append( CallDetail(a[0], a[1], a[2], a[3]))
            callDetail[i].displayDetails()
            print()
            
call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'
listStr=[call,call2,call3]
Util().parse_customer(listStr)
