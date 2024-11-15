import datetime

class CuentaBancaria:
    def __init__ (self, numero_tarjeta, pin, fecha_vencimiento, saldo):
        self.numero_tarjeta = numero_tarjeta
        self.pin = pin
        self.fecha_vencimiento = fecha_vencimiento
        self.saldo = saldo

    def es_tarjeta_valida(self):
        return self.fecha_vencimiento >= 2024

    def consultar_saldo(self, pin_ingresado):
        if pin_ingresado == self.pin and self.es_tarjeta_valida():
            return self.saldo


def main():
        #creacion de objetos

    cuenta1 = CuentaBancaria(numero_tarjeta = "123456789", pin = 1234, fecha_vencimiento = 2030, saldo = 1000)

    if cuenta1.es_tarjeta_valida():
        print(cuenta1.saldo)
        print(cuenta1.fecha_vencimiento)
        print(cuenta1.numero_tarjeta)
        print(cuenta1.pin)
    else:
        print("NO")

main()