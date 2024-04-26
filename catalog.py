
from decoradores import calcular_tiempo, calcular_memoria, log_funcion, lru_cache_size
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
    @lru_cache_size(5)
    @log_funcion
    @calcular_tiempo
    @calcular_memoria
    def get_all_vehicles(self) -> List[Vehicle]:
        return self.__vehicles
    @lru_cache_size
    @log_funcion
    @calcular_tiempo
    @calcular_memoria
    def get_price_by_range(self, min_price: float, max_price: float) -> List[Vehicle]:
        return [vehicle for vehicle in self.__vehicles if min_price <= vehicle.price <= max_price]
    @lru_cache_size(5)
    @log_funcion
    @calcular_tiempo
    @calcular_memoria
    def add_vehicle(self, vehicle: Vehicle):
        self.__vehicles.append(vehicle)
    @lru_cache_size(5)
    @log_funcion
    @calcular_tiempo
    @calcular_memoria
    def remove_vehicle(self, placa):
        for vehicle in self.__vehicles:
            if placa == vehicle.placa:
                self.__vehicles.remove(vehicle)
                break
    @lru_cache_size(5)  
    @log_funcion           
    @calcular_tiempo
    @calcular_memoria
    def update_vehicle(self, placa):
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
    
