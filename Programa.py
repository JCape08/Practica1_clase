class Carro:
    def __init__(self, marca, modelo, color, kilometraje, gasolina):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color 
        self.__kilometraje = kilometraje
        self.__gasolina = gasolina

    def get_marca(self):
        return self.__marca

    def set_marca(self, nueva_marca):
        self.__marca = nueva_marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, nuevo_modelo):
            self.__modelo = nuevo_modelo

    def get_color(self):
        return self.__color

    def set_color(self, nuevo_color):
        self.__color = nuevo_color

    def get_kilometraje(self):
        return self.__kilometraje

    def set_kilometraje(self, nuevo_km):
            self.__kilometraje = nuevo_km

    def get_gasolina(self):
        return self.__gasolina

    def set_gasolina(self, nueva_gas):
        self.__gasolina = nueva_gas

    def conducir(self, km_recorridos):
        self.__kilometraje += km_recorridos
        self.__gasolina = self.__gasolina -5
        print (f"Condujiste {km_recorridos} km. El kilometraje subio a {self.__kilometraje}.")

    def cargar_gasolina(self,porcentaje):
         self.__gasolina = porcentaje
         print(f"Tanque actualizado. Gasolina al {self.__gasolina}%")

    def info(self):
         print("INFO DEL AUTO")
         print("Marca:",self.__marca)
         print("Modelo:",self.__modelo)
         print("Color:",self.__color)
         print("Kilometraje:",self.__kilometraje)
         print("Gasolina:",self.__gasolina)

#USO_CLASE
objeto_carro = Carro ("Chevrolet", "Camaro", "Blanco", "1000", "50")
objeto_carro.info()
objeto_carro.conducir(50)
objeto_carro.info()
objeto_carro.gasolina(50)
objeto_carro.info()
