from decoradores import calcular_tiempo, calcular_memoria, log_funcion, lru_cache_size, run_all_decorators
from typing import List
from time import time
from vehicles import Vehicle


class Catalog:

    def __init__(self):
        self.__vehicles = List[Vehicle]

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Catalog, cls).__new__(cls)
            cls.instance.vehicles = []
        return cls.instance
    @run_all_decorators
    def get_all_vehicles(self) -> List[Vehicle]:
        return self.__vehicles
    @run_all_decorators
    def get_price_by_range(self, min_price: float, max_price: float) -> List[Vehicle]:
        return [vehicle for vehicle in self.__vehicles if min_price <= vehicle.price <= max_price]
    @run_all_decorators
    def add_vehicle(self, vehicle: Vehicle):
        self.__vehicles.append(vehicle)
    @run_all_decorators
    def remove_vehicle(self, placa):
        for vehicle in self.__vehicles:
            if placa == vehicle.placa:
                self.__vehicles.remove(vehicle)
                break
    @run_all_decorators
    def get_by_supply(self, supply:str):
        for vehicle in self.__vehicles:
            if supply==vehicle.supply:
                getSupply=[]
                getSupply.append(vehicle)
                break
    @run_all_decorators
    def get_by_rangeYears(self, year:str):
        for vehicle in self.__vehicles:
            x=input()
            y=input()
            if year==vehicle.year and year>x and year<y:
                getRangeYear=[]
                getRangeYear.append(vehicle)
                return getRangeYear
                break
                
    @run_all_decorators
    def update_vehicle(self, placa:str):
        for vehicle in self.__vehicles:
            if placa == vehicle.placa:
                print("-----------------------------------------")
                
                print("1=engine")
                print("2=chassis")
                print("3=price")
                print("4=model")
                print("5=year")
                print("6=comsuption")
                print("7=length")
                print("8=weight")
                print("9=placa")
                print("10=trade")
                print("11=combustible_type")
                self.atribute=input()
                if self.atribute==1:
                    self.atribute=="engine"
                if self.atribute==2:
                    self.atribute=="chassis"
                if self.atribute==3:
                    self.atribute=="price"
                if self.atribute==4:
                    self.atribute=="model"
                if self.atribute==5:
                    self.atribute=="year"
                if self.atribute==6:
                    self.atribute=="comsuption"
                if self.atribute==7:
                    self.atribute=="length"
                if self.atribute==8:
                    self.atribute=="placa"
                if self.atribute==9:
                    self.atribute=="trade"
                if self.atribute==10:
                    self.atribute=="combustible_type"
                else:
                    print("opcion invalida")
                    break
                    exit
                print("como lo quiere modificar")
                self.newValue=input()
                setattr(self.__vehicles, "attribute","newValue")
    
