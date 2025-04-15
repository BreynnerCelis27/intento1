''' canecas,py
    Código que permite crear canecas y a la vez estas mismas rellenar con 3 materiales o vaciarlas cuando esten llenas. Ademas 
    dependiendo del material permite reciclar, compostar o eliminar
    Breynner David Celis Flórez
    Código: 1.092.531.892
    Tel: 3504639016
    Email:breynner.celisflo@unipamplona.edu.co
    fecha: 18-03-2025
    asignatura= Fundamentos de la Progrmación Orientada a Obejectos (POO)
    ingeniería mecatrónica 
    '''

''' importar módulos'''


'''Clases y funciones'''
class Caneca:
    def __init__(self, color, tamaño, modelo, precio, material):
        self.color = color
        self.tamaño = tamaño
        self.modelo = modelo
        self.precio = precio
        self.material = material
        self.capacidad = False  
        self.relleno = None  
        self.cantidad_actual = 0
        self.limite = 10  

    def almacenar(self):
        if self.capacidad:
            print("La caneca ya está llena. Vacíela antes de agregar más residuos.")
            return

        print("\nOpciones de relleno:")
        print("1. Orgánico")
        print("2. Reciclable")
        print("3. Tóxico")

        try:
            opcion_relleno = int(input("Seleccione el tipo de residuo a ingresar (1-3): "))
            tipo_relleno = {1: "Orgánico", 2: "Reciclable", 3: "Tóxico"}.get(opcion_relleno)

            if tipo_relleno is None:
                print("Opción inválida.")
                return

            cantidad = int(input(f"Ingrese la cantidad de {tipo_relleno} (máximo 10 unidades): "))
            if cantidad <= 0 or self.cantidad_actual + cantidad > self.limite:
                print("No se puede agregar esa cantidad.")
                return  

            if self.cantidad_actual == 0:
                self.relleno = tipo_relleno  

            if self.relleno == tipo_relleno:
                self.cantidad_actual += cantidad
                print(f"Se agregaron {cantidad} unidades de {tipo_relleno}. Ahora hay {self.cantidad_actual} unidades.")

                if self.cantidad_actual == self.limite:
                    self.capacidad = True
                    print("La caneca está llena.")
            else:
                print(f"No se pueden mezclar tipos de residuos.")
        
        except ValueError:
            print("Entrada inválida.")

    def vaciar(self):
        if self.cantidad_actual == 0:
            print("La caneca ya está vacía.")
            return

        print("\nTipos de relleno en la caneca:")
        print("1. Orgánico")
        print("2. Reciclable")
        print("3. Tóxico")

        try:
            opcion_relleno = int(input("Seleccione el tipo de residuo que desea vaciar (1-3): "))
            tipo_relleno = {1: "Orgánico", 2: "Reciclable", 3: "Tóxico"}.get(opcion_relleno)

            if tipo_relleno != self.relleno:
                print(f"No hay residuos de tipo {tipo_relleno}.")
                return

            print(f"Actualmente hay {self.cantidad_actual} unidades de {self.relleno}.")
            cantidad_vaciar = int(input("¿Cuántas unidades desea vaciar?: "))

            if cantidad_vaciar <= 0 or cantidad_vaciar > self.cantidad_actual:
                print("Cantidad inválida.")
                return
            
            self.cantidad_actual -= cantidad_vaciar
            print(f"Se han vaciado {cantidad_vaciar} unidades. Ahora quedan {self.cantidad_actual}.")

            if self.cantidad_actual == 0:
                self.capacidad = False
                self.relleno = None
                print("La caneca ha quedado  vacía.")

        except ValueError:
            print("Entrada inválida.")

    def reciclar(self):
        if self.cantidad_actual == 0:
            print("No hay residuos en esta caneca para reciclar.")
            return
        
        if self.relleno == "Orgánico":
            print("Los residuos orgánicos han sido convertidos en compost.")
        elif self.relleno == "Reciclable":
            print("Los residuos reciclables han sido procesados y reutilizados.")
        elif self.relleno == "Tóxico":
            print("Los residuos tóxicos han sido eliminados de manera segura.")
        else:
            print("Error en el tipo de residuo.")
        
        self.cantidad_actual = 0
        self.capacidad = False
        self.relleno = None
        print("La caneca ahora está vacía y lista para ser reutilizada.")

def menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Crear canecas")
    print("2. Almacenar en caneca")
    print("3. Vaciar caneca")
    print("4. Reciclar")
    print("5. Salir")

    try:
        return int(input("Seleccione una opción: "))
    except ValueError:
        print("Ingrese un número válido.")
        return None

''' Variables y constantes '''

''' Algoritmo principal '''
canecasnuevas = []

while True:
    opcion = menu()

    if opcion == 1:
        try:
            ncanecas = int(input("¿Cuántas canecas desea crear?: "))
            if ncanecas <= 0:
                print("Ingrese un número mayor que 0.")
                continue

            for i in range(ncanecas):
                print(f"\nCreando Caneca {len(canecasnuevas) + 1}:")
                color = input("Ingrese el color: ")
                tamaño = input("Ingrese tamaño: ")
                modelo = input("Ingrese modelo: ")
                precio = input("Ingrese precio: ")
                material = input("Ingrese material: ")

                nueva_caneca = Caneca(color, tamaño, modelo, precio, material)
                canecasnuevas.append(nueva_caneca)

        except ValueError:
            print("Entrada inválida.")

    elif opcion == 2:
        if canecasnuevas:
            for idx, caneca in enumerate(canecasnuevas, start=1):
                print(f"{idx}. {caneca.color}")
            try:
                num = int(input("Seleccione una caneca: ")) - 1
                canecasnuevas[num].almacenar()
            except IndexError:
                print("Selección inválida.")
            except ValueError:
                print("Entrada inválida.")
        else:
            print("No hay canecas creadas.")

    elif opcion == 3:
        if canecasnuevas:
            for idx, caneca in enumerate(canecasnuevas, start=1):
                print(f"{idx}. {caneca.color}")
            try:
                num = int(input("Seleccione una caneca: ")) - 1
                canecasnuevas[num].vaciar()
            except IndexError:
                print("Selección inválida.")
            except ValueError:
                print("Entrada inválida.")
        else:
            print("No hay canecas creadas.")

    elif opcion == 4:
        if canecasnuevas:
            for idx, caneca in enumerate(canecasnuevas, start=1):
                print(f"{idx}. {caneca.color}")
            try:
                num = int(input("Seleccione una caneca: ")) - 1
                canecasnuevas[num].reciclar()
            except IndexError:
                print("Selección inválida.")
            except ValueError:
                print("Entrada inválida.")
        else:
            print("No hay canecas creadas.")

    elif opcion == 5:
        print("Saliendo del programa, bonito día o noche...")
        break

    else:
        print("Opción no válida.")
