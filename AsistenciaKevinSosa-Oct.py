class Empleado:  # No hereda sino solo de la clase object
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f'Empleado: [Nombre: {self.nombre}, Sueldo: {self.sueldo}]'

    def mostrar_detalles(self):
        return self.__str__()




class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return f'Gerente [ Departamento: {self.departamento}] {super().__str__()}'






def imprimir_detalles(objeto): # Este es el método para aprender lo que es el polimorfismo
    # print(objeto)  # De manera indirecta llama al str de la clase Empleado o Gerente
    print(type(objeto))  # Esto es para saber el tipo de dato que recibe
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado('Fernando', 50000)
imprimir_detalles(empleado)

gerente = Gerente('Darío', 60000, 'Sistemas')
imprimir_detalles(gerente)