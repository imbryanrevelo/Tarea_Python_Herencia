from Cuenta_Bancaria import Cuenta_Bancaria

class Cuenta_corriente(Cuenta_Bancaria):

    def __init__(self, numero_cuenta=None, propietario=None, balance: float = 0, tiene_cheque: bool = False):
        self._tiene_cheque = tiene_cheque
        super().__init__(numero_cuenta=numero_cuenta, propietario=propietario, balance=balance)

    @property
    def tiene_cheque(self):
        return self._tiene_cheque

    @tiene_cheque.setter
    def tiene_cheque(self, tiene_cheque):
        self._tiene_cheque = tiene_cheque

    def pagar_cheque(self):
        if self._tiene_cheque:
            self._balance -= self._balance
        return self._balance

if __name__ == "__main__":
    Cuentas_corrientes = Cuenta_corriente('0943928291', 'bryan', 750, True)

    Cuentas_corrientes.mostrar_balance()
    Cuentas_corrientes.credito(1400)

    Cuentas_corrientes.mostrar_balance()
    Cuentas_corrientes.debito(30)

    print(Cuentas_corrientes)
