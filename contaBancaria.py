class ContaBancaria():
    def __init__(self, numeroConta: str, titular: str, saldo: float): 
        self.numeroConta = numeroConta
        self.titular = titular 
        self.saldo = saldo
    
    def depositar(self, adicional: float):
        self.saldo += adicional
        return self.saldo
    
    def sacar(self, debito: float):
        self.saldo -= debito
        return self.saldo 
    
    def __eq__(self, objeto):
        return self.numeroConta == objeto.objnumeroConta
    
    def __str__(self,):
        return f'Conta{self.numeroConta}\nTitular: {self.titular}\nSalado: {self.saldo}'
    
if __name__ == "__main__":
    objContaBancaria = ContaBancaria("10", "Daniel", 100000)
    print(objContaBancaria)
