from modelos.empleado import EmpleadoFijo, EmpleadoPorHoras
from servicios.nomina_service import NominaService

def main():
    nomina = NominaService()

    e1 = EmpleadoPorHoras("Ana Torres", "1102456789", horas=40, tarifa=3.50)
    e2 = EmpleadoFijo("Luis Mena", "1109876543", sueldo_mensual=550.00)

    e1.cambiar_nombre("Ana T. Torres")

    nomina.agregar(e1)
    nomina.agregar(e2)

    nomina.imprimir_nomina()

if __name__ == "__main__":
    main()
