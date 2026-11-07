import time
import json
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
        count=0
        for i in range(0,len(students)):
            if students[i].destination==self.destination and students[i].timeslot==self.timeslot:
                print(f"student name:{students[i].name}|studnet year:{students[i].year}|")
                count=count+1
            if count>=self.cabseat:
                break
    def dispatch(self,students):
        print()
        for i in range(0,len(students)):
            if students[i].destination==self.destination and students[i].timeslot==self.timeslot:
                self.studentincab.append(students[i])
                print(f"student name:{students[i].name}|studnet year:{students[i].year}|")
            if len(self.studentincab)>=self.cabseat:
                break
        for student in self.studentincab:
            students.remove(student)
        print("these students have been dispatched")
        self.available=False




class RideRequest:
    def __init__(self,name,destination,timeslot,year,sumbittime):
        self.name=name
        self.destination=destination
        self.timeslot=timeslot
        self.year=year
        self.sumbittime=sumbittime

students=[]
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
        students.append(student)
      
    if choice==2:
        print("Available Cab")
        for i in range(0,len(cab_objects)):
                print(f"Cab no {i+1}")          
                print(f"Drivername:{cab_objects[i].drivername}")
                print(f"DriverDestination:{cab_objects[i].destination}")
                print(f"Cabseat:{cab_objects[i].timeslot}")
                print(f"Available:{cab_objects[i].available}")
                print("__________")
        print("Waitlist")
        for i in range(0,len(students)):       
            print(f"student no {i+1}")
            print(f"student name:{students[i].name}\nstudent destination:{students[i].destination}")
            print(f"student timeslot:{students[i].timeslot}")
            print(f"student year:{students[i].year}")
            print("________")
    if choice==3:
        for i in range(0,len(cab_objects)):
            if cab_objects[i].available:
                print(f"cab driver name:{cab_objects[i].drivername}")
                print(f"cab destination:{cab_objects[i].destination}")
                print("Match Student")
                cab_objects[i].match(students)
                print("____________")
    if choice==4:
        cabno=int(input("choose cab no:"))
        if cab_objects[cabno-1].available:
            cab_objects[cabno-1].dispatch(students)
        else:
            print("Cab already dispatched")
     
    if choice==5:
        isintrested=False    
    



