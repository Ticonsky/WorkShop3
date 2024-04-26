
from engines import Engine


class Vehicle:
    """This class represents an abstraction of a vehicle inside the catalog business model."""

    def __init__(self,engine: Engine,chassis: str, price: float,model: str,year: int,
        consumption: float, placa:str):
        self.engine = engine
        self.chassis = chassis
        self.price = price
        self.model = model
        self.year = year
        self.consumption = consumption
        self.placa=placa
    def __str__(self):
        return f"Vehicle: {self.model} - {self.year} - {self.price} - \
            {self.consumption} - {self.engine} - {self.chassis}"


class Helicopter(Vehicle):
    def __init__(self, engine: Engine, chassis: str, price: float, model: str, year: int, consumption: float, placa: str):
        super().__init__(engine, chassis, price, model, year, consumption, placa)


class Scooter(Vehicle):
    def __init__(self, engine: Engine, chassis: str, price: float, model: str, year: int, consumption: float, placa: str):
        super().__init__(engine, chassis, price, model, year, consumption, placa)


class Motorcycle(Vehicle):
    def __init__(self, engine: Engine, chassis: str, price: float, model: str, year: int, consumption: float, placa: str):
        super().__init__(engine, chassis, price, model, year, consumption, placa)


class Car(Vehicle):

    def __init__(
        self,
        placa: str,
        engine: Engine,
        chassis: str,
        price: float,
        model: str,
        year: int,
        consumption: float,
        transmission: str,
        trade: str,
        combustible_type: str,

    ):
        super().__init__(engine, chassis, price, model, year, consumption,placa )
        self.transmission = transmission
        self.trade = trade
        self.combustible_type = combustible_type

class Truck(Vehicle):
    def __init__(self, engine: Engine, chassis: str, price: float, model: str, year: int, consumption: float, placa: str):
        super().__init__(engine, chassis, price, model, year, consumption, placa)

    def calculate_gas_consupmtion(self) -> float:
        """
        This method calculates consumption based on engine
        values.

        Returns:
        - float: vehicle consumption
        """
        consumption = (
            (1.1 * self.engine.power)
            + (0.2 * self.engine.weight)
            + (0.3 if self.chassis == "A" else 0.5)
        )
        return consumption


class Yacht(Vehicle):
    """This class is a concrete implementation of a yatch"""

    def __init__(
        self,
        engine: Engine,
        chassis: str,
        price: float,
        model: str,
        year: int,
        consumption: float,
        length: float,
        weight: float,
        placa:str,
        trade: str,
    ):
        super().__init__(placa, engine, chassis, price, model, year, consumption)
        self.length = length
        self.weight = weight
        self.trade = trade