class Cuenta_Bancaria:
    def __init__(self, numero_cuenta=None, propietario=None, balance: float = 0):
        self._numero_cuenta = numero_cuenta
        self._propietario = propietario
        self._balance = balance

    def __str__(self):
        return f'Cuenta Bancaria: número_cuenta={self._numero_cuenta}, propietario={self._propietario}, balance={self._balance}'

    @property
    def numero_cuenta(self):
        return self._numero_cuenta

    @numero_cuenta.setter
    def numero_cuenta(self, numero_cuenta):
        self._numero_cuenta = numero_cuenta

    @property
    def propietario(self):
        return self._propietario

    @propietario.setter
    def propietario(self, propietario):
        self._propietario = propietario

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    def credito(self, valor: float = 0):
        self._balance += valor
        return self._balance

    def debito(self, valor: float = 0):
        self._balance -= valor
        return self._balance

    def mostrar_balance(self):
        print(self._balance)
