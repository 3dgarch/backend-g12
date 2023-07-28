ingreso = int(input('Ingrese su monto: '))

if(ingreso>500):
    print("No recibe  el bono Yanapay")
elif(ingreso>=250 and ingreso<=500):
    print("Recibes el bono yanapay")
else:
    print("Recibe bono y balon gas")
