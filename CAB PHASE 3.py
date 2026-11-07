import time
import json
import heapq
import copy
def displayS(student):
        print(f"student name:{student.name}\nstudent destination:{student.destination}")
        print(f"student timeslot:{student.timeslot}")
        print(f"student year:{student.year}")
        print("________")   
def displayC(cab):       
            print(f"Drivername:{cab.drivername}")
            print(f"DriverDestination:{cab.destination}")
            print(f"Cabseat:{cab.cabseat}")
            print("__________")             

class Cab:
    def __init__(self,drivername,cabseat,destination,timeslot,available,studentincab):
        self.drivername=drivername
        self.cabseat=cabseat
        self.destination=destination
        self.timeslot=timeslot
        self.available=available
        self.studentincab=studentincab
        self.matchlist=[]
    def match(self,students):
        copystd=students[self.destination,self.timeslot].copy()
        count=0
        while count<self.cabseat and copystd:
            item=heapq.heappop(copystd)
            displayS(item[2])
            count=count+1
        if count==0:
            print("no match available")
    def dispatch(self,students):
        print("Student info going to cab:")
        count=0
        qu=students[self.destination,self.timeslot]
        while count<self.cabseat and qu:
            item=heapq.heappop(qu)
            self.studentincab.append(item[2])
            displayS(item[2])
            count=count+1
        if count==0:
            print("No studens available for this cab , Cab still available")
        else:
            print(f"Cab has been dispatched with {count} students")
            self.available=False
        

class RideRequest:
    def __init__(self,name,destination,timeslot,year,sumbittime):
        self.name=name
        self.destination=destination
        self.timeslot=timeslot
        self.year=year
        self.sumbittime=sumbittime

isintrested=True
with open("cabs.json", "r") as file:
    cabs = json.load(file)
cab_objects = []

for cab_data in cabs:
    cab = Cab(
        cab_data["drivername"],
        cab_data["cabseat"],
        cab_data["destination"],
        cab_data["timeslot"],
        cab_data["available"],                     
        cab_data["studentincab"]
    )

    cab_objects.append(cab)
students= {
    ("Delhi", "Morning"): [],
    ("Delhi", "Afternoon"): [],
    ("Delhi", "Evening"): [],
    ("Delhi", "Night"): [],
    ("Jaipur", "Morning"): [],
    ("Jaipur", "Afternoon"): [],
    ("Jaipur", "Evening"): [],
    ("Jaipur", "Night"): []
}

print("*********CAB SERVICES**********")
while isintrested:
    print("Choose one of the following")
    print("1.Request Cab")
    print("2.See wait list and available cab")
    print("3.find match")
    print("4.Dispatch Cab")
    print("5.quit") 
    choice=int(input("enter your choice:"))
    if choice==1:  
        name=input("enter your name for cab request:")
        destination=input("enter your destination(Delhi/Jaipur):")
        if destination!="Delhi" and destination!="Jaipur":
            print("Sorry! we do not provide this location")
            continue
        timeslot=input("at what timeslot do you want to leave(Morning,Afternoon,Evening,Night):")
        if timeslot!="Morning" and timeslot!="Afternoon" and timeslot!="Evening" and timeslot!="Night":
            print("you provided wrong timeslot try again")
            continue
        year=int(input("enter your year(1,5):"))
        if (year>5 or year<1):
            print("you choose wrong year please try again")
            continue
        sumbittime=time.time()
        student=RideRequest(name,destination,timeslot,year,sumbittime)
        heapq.heappush(students[(student.destination, student.timeslot)],
               (-student.year, student.sumbittime, student))
      
    if choice==2:
        option1=input("enter your destination check available cab:")
        option2=input("enter you time slot:")
        count=0
        print("Available Cab")
        for i in range(0,len(cab_objects)):
            if option1==cab_objects[i].destination and option2==cab_objects[i].timeslot and cab_objects[i].available:
                displayC(cab_objects[i])
                count=count+1
        if count==0:
            print("No cab available")

        print("Waitlist")
        copystd=students[option1,option2].copy()
        count=0
        while count<len(copystd):
            item=heapq.heappop(copystd)
            displayS(item[2])
            count=count+1
        if count==0:
            print("no student available")    
#i don't think match is needed now
    if choice==3:
        for i in range(0,len(cab_objects)):
            if cab_objects[i].available:
                print(f"cab driver name:{cab_objects[i].drivername}")
                print(f"cab destination:{cab_objects[i].destination}")
                print("Match Student")
                cab_objects[i].match(students)
                print("____________")
    if choice==4:
        option1=input("enter your destination check available cab:")
        option2=input("enter you time slot:")
        count=0
        avacab=[]
        print("Cab for you")
        for i in range(0,len(cab_objects)):
            if option1==cab_objects[i].destination and option2==cab_objects[i].timeslot and cab_objects[i].available:
                displayC(cab_objects[i])
                count=count+1
                avacab.append(cab_objects[i])
        if count==0:
            print("No cab available")
        else:
            cabno=int(input("enter which cab no to dispatch:"))
            avacab[cabno-1].dispatch(students)
    
     
    if choice==5:
        isintrested=False    
    



