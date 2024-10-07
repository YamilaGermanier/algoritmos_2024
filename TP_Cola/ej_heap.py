"""
3. El general Hux es la persona encargada de administrar todas las operaciones de la base Starkiller,
para lo cual nos solicita desarrollar un algoritmo que permita controlar las actividades que
se realizan, contemplando lo siguiente:
        a. debe contemplar distintas prioridades para el control de operaciones de acuerdo al siguiente
        criterio: pedidos de líder supremo Snoke y de Kylo Ren nivel tres, de capitán Phasma
        nivel dos y el resto de las operaciones nivel a cargo de los generales de la base de nivel uno;
        b. de cada actividad se conoce quien es el encargado, una descripción, la hora y opcionalmente
        la cantidad de Stormtroopers requeridos;
        c. utilizar una cola de prioridad para administrar las distintas operaciones, debe cargar al
        menos ocho: dos de nivel tres, cuatro de nivel dos y cuatro de nivel uno;
        d. opcionalmente se podrán agregar operaciones luego de atender una;
        e. realizar la atención de las operaciones de la cola;
        f. luego de atender la quinta operación, agregar una operación solicitada por capitán Phasma
        para revisión de intrusos en el hangar B7 que requiere 25 Stormstroopers;
        g. luego de atender la sexta operación, agregar una operación solicitada por el líder supremo
        Snoke para destruir el planeta Takodana.
"""

from heap import HeapMax

# encargado, descripción, hora y Stormtroopers requeridos;

class Operacion:
    def __init__(self, nombre, descripcion, hora, prioridad, stormtroopers=0):
        self.nombre = nombre
        self.descripcion = descripcion
        self.hora = hora
        self.prioridad = prioridad
        self.stormtroopers = stormtroopers

    def __repr__(self):
        return (f"Operacion(Nombre: {self.nombre}, Descripcion: {self.descripcion}, "
                f"Hora: {self.hora}, Priority: {self.prioridad}, "
                f"Stormtroopers: {self.stormtroopers})")


class Operador:
    def __init__(self):
        self.heap = HeapMax()

    def agregar_operacion(self, operation):
        self.heap.arrive(operation.descripcion, operation.prioridad)

    def atender_operacion(self):
        operation = self.heap.atention()
        if operation:
            print(f"Atendiendo: {operation}")
            return operation
        else:
            print("No more operations to attend.")
            return None

    def agregar_operaciones_prioritarias(self):
        self.agregar_operacion(Operacion("Operación 1", "Solicitud del Líder Supremo Snoke", "10:00", 3))
        self.agregar_operacion(Operacion("Operación 2", "Solicitud del Líder Supremo Snoke", "10:05", 3))
        self.agregar_operacion(Operacion("Operación 3", "Solicitud del Capitán Phasma", "10:10", 2))
        self.agregar_operacion(Operacion("Operación 4", "Solicitud del Capitán Phasma", "10:15", 2))
        self.agregar_operacion(Operacion("Operación 5", "Operación de Rutina", "10:20", 1))
        self.agregar_operacion(Operacion("Operación 6", "Operación de Rutina", "10:25", 1))
        self.agregar_operacion(Operacion("Operación 7", "Operación de Rutina", "10:30", 1))
        self.agregar_operacion(Operacion("Operación 8", "Operación de Rutina", "10:35", 1))

    def ejecutar_operaciones(self):
            for i in range(8):
                self.atender_operacion()
                if i == 4:
                    self.agregar_operacion(Operacion("Operación 9", "Revisar intrusos en el hangar B7", "10:40", 2, 25))
                elif i == 5:
                    self.agregar_operacion(Operacion("Operación 10", "Destruir el planeta Takodana", "10:45", 3))


base = Operador()
base.agregar_operaciones_prioritarias()
base.ejecutar_operaciones()
