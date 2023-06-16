from Cuenta_Bancaria import Cuenta_Bancaria

class Cuenta_ahorro(Cuenta_Bancaria):
    def __init__(self, interes: float = 0, numero_cuenta=None, propietario=None, balance: float = 0):
        self._interes = interes
        super().__init__(numero_cuenta=numero_cuenta, propietario=propietario, balance=balance)

    @property
    def interes(self):
        return self._interes

    @interes.setter
    def interes(self, interes):
        self._interes = interes

    def pagar_interes(self):
        self._balance += (self._balance * self._interes) / 100
        return self._balance

if __name__ == "__main__":
    Cuentas_ahorros = Cuenta_ahorro(6, '0943928291', 'bryan', 450)

    Cuentas_ahorros.mostrar_balance()
    Cuentas_ahorros.credito(1400)

    Cuentas_ahorros.mostrar_balance()
    Cuentas_ahorros.debito(30)

    print(Cuentas_ahorros)
