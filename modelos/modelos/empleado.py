class Empleado:
    def __init__(self, nombre: str, cedula: str):
        # Encapsulación: atributos privados
        self.__nombre = nombre
        self.__cedula = cedula

    def nombre(self) -> str:
        return self.__nombre

    def cedula(self) -> str:
        return self.__cedula

    def cambiar_nombre(self, nuevo_nombre: str) -> None:
        if not nuevo_nombre or not nuevo_nombre.strip():
            raise ValueError("El nombre no puede quedar vacío")
        self.__nombre = nuevo_nombre.strip()

    def calcular_pago(self) -> float:
        # Método pensado para polimorfismo
        return 0.0

    def info(self) -> str:
        return f"{self.nombre()} (CI: {self.cedula()})"


class EmpleadoFijo(Empleado):
    def __init__(self, nombre: str, cedula: str, sueldo_mensual: float):
        super().__init__(nombre, cedula)
        self.sueldo_mensual = sueldo_mensual

    def calcular_pago(self) -> float:
        return float(self.sueldo_mensual)

    def info(self) -> str:
        return f"{super().info()} | Fijo | Sueldo: ${self.sueldo_mensual:.2f}"


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre: str, cedula: str, horas: float, tarifa: float):
        super().__init__(nombre, cedula)
        self.horas = horas
        self.tarifa = tarifa

    def calcular_pago(self) -> float:
        return float(self.horas * self.tarifa)

    def info(self) -> str:
        return f"{super().info()} | Por horas | Horas: {self.horas} | Tarifa: ${self.tarifa:.2f}"
