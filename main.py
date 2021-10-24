class Asiento :
    
    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self,color):
        colores = ['rojo','verde','negro','blanco','amarillo']
        if colores.count(color) != 0:
            self.color = color

class Motor : 
    def __init__(self,numeroCilindros,tipo,registro):
          self.tipo = tipo
          self.registro = registro
          self.numeroCilindros = numeroCilindros

    def cambiarRegistro(self,registro):
         self.registro = registro

    def asignarTipo(self,tipo):
        if tipo == 'electrico' or tipo == 'gasolina':
            self.tipo = tipo

class Auto:
    cantidadCreados = 0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio 
        self.asientos = asientos
        self.marca = marca 
        self.motor = motor 
        self.registro = registro 

    def cantidadAsientos(self):
        contador = 0
        for i in self.asientos:
            if type(i) == Asiento:
                contador += 1
        return contador          

    def verificarIntegridad(self):
        verificacion = True 
        if self.registro == self.motor.registro :
            for i in self.asientos:
               if type(i) == Asiento: 
                if i.registro != self.registro:
                    verificacion = False
                    break
            if verificacion == True:
                return('Auto original')
            else:
                return('Las piezas no son originales') 

        else:
            return('Las piezas no son originales')            

         


 