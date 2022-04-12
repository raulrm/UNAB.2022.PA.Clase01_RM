import datetime
from pydoc import doc

import docutils

class CuentaBancaria():
    ''' Clase que nos permite la gestión de una Cuenta Bancaria genérica
    '''
    
    def __init__(self, saldo_inicial, nombre, apellido):
        """Constructor d ela clase

        Args:
            saldo_inicial (_type_): _description_
            nombre (_type_): _description_
            apellido (_type_): _description_
        """
        # TODO: Agregar un atributo de moneda
        # TODO: Ver la forma de soportar cajas de ahorro y/o cuentas corrientes
        self.saldo = saldo_inicial
        self.nombre = nombre
        self.apellido = apellido
        self.movimientos = []

    def registrar(self, monto, operacion):
        """_summary_

        Args:
            monto (_type_): _description_
            operacion (_type_): _description_
        """
        dato = [operacion, monto, datetime.now()]
        self.movimientos.append(dato)

    def depositar(self, monto):
        """Método que nos permite realizar un depósito bancario

        Args:
            monto (_type_): _description_
        """
        ''''''
        self.registrar(monto,"DEPOSITO")
        self.saldo = self.saldo + monto

    def extraer(self, monto):
        """Metodo que nos permite extraer dinero d ela cuenta

        Args:
            monto (_type_): _description_
        """
        if self.saldo - monto >=0:
            self.registrar(monto,"RETIRO")
            self.saldo = self.saldo - monto
        else:
            self.registrar(monto,"SALDO INSUFICIENTE")

    def datos_titular(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.apellido + ', ' + self.nombre
    
    def datos_saldo(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.saldo

    def _reset_saldo(self):
        """_summary_
        """
        self.saldo = 0 

    def listar(self):
        """_summary_
        """
        for dato in self.movimientos[]:
            print("Operacion: " + x[1] + " monto: " + str(x[2]) +  " fecha: " + x[3].strftime("%Y-%m-%d %H:%M:%S"))