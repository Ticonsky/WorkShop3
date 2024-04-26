from datetime import datetime
from catalog import Catalog 
class userFactory:
    """this class represents the behavior of an user"""
    def __init__(self, rol:str,name:str, email:str, password:str):
        self.rol=rol
        self.name=name
        self.email=email
        self.password=password

    def search(self):
        Catalog.get_all_vehicles
        Catalog.get_price_by_range

class admin(userFactory):
    """this class represents the behavior of an Admin user"""
    def __init__(self, rol: str, name: str, email: str, password: str):
        super().__init__(rol, name, email, password)
    def deleteVehicle():
        Catalog.remove_vehicle()
    def addVecicle():
        Catalog.add_vehicle
    def updateVehicle():
        Catalog.update_vehicle()

class user(userFactory):
        """this class represents the behavior of a normal user"""
        def __init__(self, rol: str, name: str, email: str):
            super().__init__(rol, name, email)
            super().__init__(rol)

def CreateUser(userType:str):
    if userType == "admin" or userType == "user":         
        user_instance=userType(" ","","","")
        with open(f"{userType}.txt","w") as file:
            file.write(f"User Info:\n"#0
                f"Rol: {user_instance.rol}\n"#1
                f"Name: {user_instance.name}\n"#2
                f"Email: {user_instance.email}\n"#3---------> most important
                f"Password: {user_instance.password}\n")#4----> most important

    else:
        print("papi escriba bien")
        exit
        
def autenticacion(userType:str):
    Email=input()
    Password=input()
    EmailBD=f"Email: {Email}"
    PasswordBD=f"Password: {Password}"
    if userType == "admin" or userType == "user":         
        with open(f"{userType}.txt","r") as file:
            for linea in file:
                if  EmailBD in linea and PasswordBD in linea:
                    print("Puede pasar mi perro ojo con el perro")
    else:
        print("papi escriba bien")
        exit
        

