def main():
    #escribe tu código abajo de esta línea
    saldoInicial = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el número de cheques: "))
        
    saldoFinal=saldoInicial+ingresos-egresos-(13*cheques)
    saldoFinal=saldoFinal-saldoFinal*.075
    print("El saldo final de la cuenta es: "+ str(saldoFinal))



if __name__ == '__main__':
    main()
