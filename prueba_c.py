vectpar=[14,58,2,33,44]
aux=0
band=0
    
while band==0:
    band=1
    for i in range(0,len(vectpar)-1):
        if vectpar[i] > vectpar[i+1] :
            aux= vectpar[i]
            vectpar[i]= vectpar[i+1]
            vectpar[i+1]=aux
            band=0 

print(vectpar)
print("el vector esta ordenado exitosamente!"
