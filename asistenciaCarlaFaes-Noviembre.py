class Persona:
    contadorPersonas = 0    
    @classmethod
    def generarSiguienteValor(cls):
        cls.contadorPersonas += 1
        return cls.contadorPersonas

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generarSiguienteValor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [id = {self.id_persona}, nombre= {self.nombre}, edad = {self.edad}'


persona1 = Persona('Mati', 22)
print(persona1)
persona2 = Persona('Pedro', 18)
print(persona2)
persona3 = Persona('Juan', 19)
print(persona3)
Persona.generarSiguienteValor()
Persona4 = Persona('Willy', 26)
print(Persona4)
print(f'Valor contador personas: {Persona.contadorPersonas}')

