class Car:
    Make = "Mercedes_Benz"
    Model = "M Class"
    Year = 2014
    Condition = "New"
    Color = "White"
    Body = "SUV"
    Transmission = "Automatic"


    def __init__(self):
        # self.start = start
        # self.reverse = reverse
        # self.drive = drive
        # self.park = park
        self.race()

        

    def race(self):
        print("Welcome to Car")
        print()
        self.selectGear()


    def selectGear(self):
        driveMode=("start", "drive", "park", "reverse")
        for each in driveMode:
            print(each)
        user = input("Select drive mode: ")
        if user =="start":
            print("The car engine is starting now")
            self.driveCar()
        else:
            print("You need to start the car")
            self.selectGear()

    def driveCar(self):
        self.drive = input("Select drive to move the car: ")
        if self.drive == "drive":
            print("The car is moving now")
            self.parkCar()
        else:
            print("You need to select drive before car can move")
            self.driveCar()

    def parkCar(self):
        self.park = input("Select park to stop the car: ")
        if self.park == "park":
            print("the car parked successfully. Please off your engine")
            self.selectGear()
        
        else:
            print("You need to select park to stop the car")
            self.parkCar()


    def reverseCar(self):
        self.reverse = input("Select reverse: ")
        if self.reverse == "reverse":
            print("The car is moving backward")
            self.selectGear()

        else:
            print("select reverse to move the car backward")
            self.reverseCar()
    
motocar=Car()

        
        #self.park = input("Choose park to stop the car: ")     

        

        #else:
            #print("Select drive to move the car")
            #self.onCar()
    
    #def driveCar(self):
        #print("The car is moving now")
        #self.park = input("Choose park to stop the car: ")
        #if self.park.lower() == "park":
            #self.parkCar()
        #else:
            #print("select park to stop the car")
    
    #def parkCar():
        #print("the car is ready to park")
        

    #def reverseCar():

        








    
    
    

        
        
