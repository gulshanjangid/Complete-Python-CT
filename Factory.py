class Factory:
    def __init__(self,matrial,zips,packets):
       self.material = matrial
       self.zips = zips
       self.packets = packets



    def show(self):
        print("your object details are {self.materials} , {self.packets},{self.zips}")


reebok = Factory("leather" ,3,2)
        
        