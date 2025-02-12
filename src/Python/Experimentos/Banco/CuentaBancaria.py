import datetime
class CuentaBancaria:
    def _init_(self, numero_tarjeta, pin, fecha_vencimiento, saldo_inicial):
        self.numero_tarjeta = numero_tarjeta
        self.pin = pin
        self.fecha_vencimiento = fecha_vencimiento
        self.saldo = saldo_inicial

    def es_tarjeta_valida(self):
        return self.fecha_vencimiento >= 2024 #datetime.date.today().year

    def consultar_saldo(self, pin_ingresado):
        if pin_ingresado == self.pin and self.es_tarjeta_valida():
            return self.saldo
        else:
            print("Algo esta mal :(")
            return 0.0

def main():
    #creación de objetos
    tarjeta1 = CuentaBancaria(numero_tarjeta=12345678910, pin=1234, fecha_vencimiento=2025, saldo_inicial=1000.00)

    # if  tarjeta1.es_tarjeta_valida():
    # print("Tarjeta valida :)")
    #else:
    #  print("Tarjeta invalida :(")
    saldo = tarjeta1.consultar_saldo(1234)
    print(saldo)
main()