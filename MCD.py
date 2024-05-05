import unittest


def calculo_MCM (nroA,nroB):
    divisor = 1
    valor = 'true'
    MCM = []

    while (nroA !=1 or nroB!=1 ):
        valor = 'false'

        while(valor == 'false'):
            ##Cada vez que entra al bucle el divisor se incrementa
            divisor+=1

            ##Entra si se dividen en divisores comunes 
            while (nroA%divisor==0 and nroB%divisor==0):
                nroA/=divisor
                nroB/=divisor
                MCM.append(divisor)

            ##Entra divisores solo para nroA
            while(nroA%divisor==0):
                nroA/=divisor
                MCM.append(divisor)
            ##Entra divisores solo para nroB
            while(nroB%divisor==0):
                nroB/=divisor
                MCM.append(divisor)
            ##Saldra del bucle while si el divisor no es para ningun numero 
            valor = 'true' 
        ##Regresa al valor false para que vuelva probarse el divisor en ambos numeros 
        valor = 'false'
    print(nroA," ",nroB)
    
    print(MCM)
    mcm = 1
    ## MCM de ambos numeros 
    for i in range(len(MCM)):
        mcm *=MCM[i]


    print("El minimo comun multiplo es : ",mcm)
    return mcm


def calculo_MCD(nroA,nroB):
    divisor = 1
    valor = 'false'
    MCD = []
    mcd = 1
    #Dividiremos solo el divisor que sea comun para ambos numeros 
    while (valor=='false'):
        #prueba de divisor para comparar
        divisor +=1
        if ( nroA%divisor==0 and nroB%divisor==0 ) :
            nroA/=divisor
            nroB/=divisor
            #Se registrar valor en el MCD
            MCD.append(divisor)
        else: 
            #Si no hay divisores comunes sale del bucle
            valor = 'true'
## MCD de ambos numeros 
    for i in range(len(MCD)):
        mcd *=MCD[i]
    print("El maximo comun divisor es : ",mcd)
    return mcd
  

class TestCalculoDeMCM_MCD(unittest.TestCase):
    
    def test_calcular_MCD(self):
        esperado = 24
        nroa = 24
        nrob = 48
        self.assertEqual(calculo_MCD(nroa,nrob),esperado)
    def test_calcular_MCM(self):
        esperado = 272
        nroa = 34
        nrob = 16
        self.assertEqual(calculo_MCM(nroa,nrob),esperado)




if __name__ == "_main_":
    unittest.main()
















