def main():
    #escribe tu código abajo de esta línea
    pesoInicial = float(input("Dame el peso inicial: "))
    pesoFinal = float(input("Dame el peso final: "))
    cantidadMeses = int(input("Dame la cantidad de meses: "))
    pesoBajar = (pesoInicial-pesoFinal)/cantidadMeses
    
    print("Lo que debes bajar por mes es: " + str(pesoBajar))



if __name__ == '__main__':
    main()
