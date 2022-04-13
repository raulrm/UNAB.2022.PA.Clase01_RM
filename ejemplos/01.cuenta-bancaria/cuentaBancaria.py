import datetime
from pydoc import doc

import docutils

class CuentaBancaria():
    ''' Clase que nos permite la gestión de una Cuenta Bancaria genérica
    '''

    def __init__(self, saldo_inicial:int, nombre:str, apellido:str, moneda:str = "ar$"):
        """Constructor de la clase

        Args:
            saldo_inicial (int): monto inicial de la cuenta bancaria
            nombre (str): _El nombre del titular de la cuenta
            apellido (str): El apellido
            moneda (str): El nombre d ela moneda que va a usar la cuenta
        """
        # TODO: Ver la forma de soportar cajas de ahorro y/o cuentas corrientes
        # Inicializamos todos los atributos
        self.saldo = saldo_inicial
        self.nombre = nombre
        self.apellido = apellido
        self.movimientos = []
        self.moneda = moneda

    def registrar(self, monto:int, operacion:str):
        """ Esta funcion registra las operaciones que se realicen en la cuenta

        Args:
            monto (int): _el valor que se debita o deposita en la cuenta
            operacion (str): string que describe la accion realizada
        """
        # creamos una lista con el tipo d eoperacion, monto y la fecha actual
        dato = [operacion, monto, datetime.now()]
        # guardamos esa lista en la lista de movimientos
        self.movimientos.append(dato)

    def depositar(self, monto:int):
        """Método que nos permite realizar un depósito bancario

        Args:
            monto (int): monto que se deposita en la cuenta
        """
        # informamos de la operacion
        self.registrar(monto,"DEPOSITO")
        # sumamos el dinero a la cuenta
        self.saldo = self.saldo + monto

    def extraer(self, monto:int):
        """Metodo que nos permite extraer dinero d ela cuenta

        Args:
            monto (int): monto que se va a retirar de la cuenta bancaria
        """
        # rimero verifivcamos si es posible extraer dinero (si el saldo alcanza para cubrir el monto)
        if self.saldo - monto >=0:
            # Si es posible, lo restamos e informamos de la operacion
            self.registrar(monto,"RETIRO")
            self.saldo = self.saldo - monto
        else:
            # caso contrario, informamos de la imposibilidad de realizar el retiro
            self.registrar(monto,"SALDO INSUFICIENTE")

    def datos_titular(self):
        """ Funcion que reporta los datos del titular de la cuenta

        Returns:
            str: Un string con la concatenacion de nombre y apellido
        """
        return self.apellido + ', ' + self.nombre
    
    def datos_saldo(self) -> int:
        """ Funcion que reporta el saldo actual de la cuenta

        Returns:
            int: saldo actual
        """
        return self.saldo

    def _reset_saldo(self):
        """ Metodo que vacia la cuenta
        """
        self.saldo = 0 

    def listar(self):
        """ Metodo que imprime todos los movimeintos realizados en la cuenta
        """
        for dato in self.movimientos[]:
            print("Operacion: " + dato[1] + " monto: " + str(dato[2]) +  " fecha: " + dato[3].strftime("%Y-%m-%d %H:%M:%S"))