

class Engine:
    """This class represents an abstraction of an engine for any vehicle."""
    def __init__(
        self,
        torque: int,
        maximum_speed: int,
        dimenssions: str,
        power: int,
        stability: str,
        weight: float,
    ):
        self.__torque = torque
        self.__maximum_speed = maximum_speed
        self.__dimenssions = dimenssions
        self.__power = power
        self.__stability= stability
        self.__weight = weight

class GasEngine(Engine):
    """This class represents the behavior of a gas engine"""
    def __init__(self, supply:str, torque: int, maximum_speed: int, dimenssions: str, power: int, stability: str, weight: float):
        super().__init__(torque, maximum_speed, dimenssions, power, stability, weight)
        self.supply=supply

class ElectricEngine(Engine):
    """This class represents the behavior of an electric engine"""
    def __init__(self, supply:str, torque: int, maximum_speed: int, dimenssions: str, power: int, stability: str, weight: float):
        super().__init__(torque, maximum_speed, dimenssions, power, stability, weight)
        self.supply=supply
