# Cab-dispatcher
SO this is my cab dispatcher first of all i forget to save phase 1 so i am sorry 
now when you run Cab file you will see menu which will consist of 5 option 1st one is adding a request it will take student info and store it into student.json
second option is waiting list and available cab option user will enter their destination and time slot app will give list of available driver and then give waitlist they will be in order of student for that combination
third option is match after phase 2 i think it is useless so i have done less work in it 
fourth option is dispatch cab it will first take user destination and user time slot the show all available cab you will be given a option to dispatch cab according to their number and cab will be dispatched if there is no student then cab will not dispatched and student and cab json will be updated
in last quit that will close program 
JSON file format
[
    {
        "drivername": "Rahul Sharma",
        "cabseat": 4,
        "destination": "Delhi",
        "timeslot": "Morning",
        "available": true,
        "studentincab": []
    }
]

tricky question answer
1. it will be fine cab can leave with 1 or 2 students
2. if there are no cab student will see there are no cab available message nothing happen to student
3. so while setting order in heap it check both student year and submit time which will be recorded during add request option so if year is same then it will check which one has lowest submit time ,it is not possible to have same submit time in this app
4. a)it ill o(nlogn)
   b)picking and removing one student from heap take o(logN) so 4 will take at max o(4logN)
   c) since when finding cab it take destination and slot it will check cab file with input destination and timeslot with element c so it will o(c)

so this is my code it is not perfect but i try to do all task please forgive for my small mistake i am new to coding
