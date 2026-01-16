from modelos.empleado import Empleado

class NominaService:
    def __init__(self):
        self._empleados: list[Empleado] = []

    def agregar(self, empleado: Empleado) -> None:
        self._empleados.append(empleado)

    def imprimir_nomina(self) -> None:
        print("\n=== NÓMINA ===")
        for emp in self._empleados:
            print(emp.info())
            print(f"Pago: ${emp.calcular_pago():.2f}")
            print("-" * 30)
