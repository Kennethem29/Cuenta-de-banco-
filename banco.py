class CuentaBancaria:
    def __init__(self, numero_cuenta, nombre_titular, saldo=0, tipo_cuenta="Ahorro"):
        self.numero_cuenta = numero_cuenta
        self.nombre_titular = nombre_titular
        self.saldo = saldo
        self.tipo_cuenta = tipo_cuenta
        self.transacciones = []

    def consultar_saldo(self):
        print(f"Saldo disponible: ${self.saldo:.2f}")

    def depositar_dinero(self, monto):
        if monto > 0:
            self.saldo += monto
            self.transacciones.append(f"Depósito de ${monto:.2f}")
            print(f"Depósito exitoso. Saldo actual: ${self.saldo:.2f}")
        else:
            print("Monto inválido. No se puede depositar un monto negativo.")

    def retirar_dinero(self, monto):
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
            self.transacciones.append(f"Retiro de ${monto:.2f}")
            print(f"Retiro exitoso. Saldo actual: ${self.saldo:.2f}")
        elif monto > self.saldo:
            print("Saldo insuficiente. No se puede retirar un monto mayor al saldo disponible.")
        else:
            print("Monto inválido. No se puede retirar un monto negativo.")

    def transferir_dinero(self, cuenta_destino, monto):
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
            cuenta_destino.saldo += monto
            self.transacciones.append(f"Transferencia de ${monto:.2f} a la cuenta {cuenta_destino.numero_cuenta}")
            cuenta_destino.transacciones.append(f"Transferencia de ${monto:.2f} desde la cuenta {self.numero_cuenta}")
            print(f"Transferencia exitosa. Saldo actual: ${self.saldo:.2f}")
        elif monto > self.saldo:
            print("Saldo insuficiente. No se puede transferir un monto mayor al saldo disponible.")
        else:
            print("Monto inválido. No se puede transferir un monto negativo.")

    def mostrar_transacciones(self):
        print("Historial de transacciones:")
        for transaccion in self.transacciones:
            print(transaccion)


def main():
    cuenta1 = CuentaBancaria("123456789", "Juan Pérez", 1000)
    cuenta2 = CuentaBancaria("987654321", "María García", 500)

    while True:
        print("\nMenú de opciones:")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Transferir dinero")
        print("5. Mostrar transacciones")
        print("6. Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            cuenta1.consultar_saldo()
        elif opcion == "2":
            monto = float(input("Ingrese el monto a depositar: "))
            cuenta1.depositar_dinero(monto)
        elif opcion == "3":
            monto = float(input("Ingrese el monto a retirar: "))
            cuenta1.retirar_dinero(monto)
        elif opcion == "4":
            monto = float(input("Ingrese el monto a transferir: "))
            cuenta1.transferir_dinero(cuenta2, monto)
        elif opcion == "5":
            cuenta1.mostrar_transacciones()
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
