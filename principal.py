import os
import citas
if __name__=="__main__":
    os.system('cls')
    isAddCitas=True
    while(isAddCitas):
        print('+','-'*55,'+')
        print("|{:^10}{}{:^10}".format('','MENU CENTRAL DE CITAS MEDICAS',''))
        print('+','-'*55,'+')
        print("1.Gestion Citas medicas")
        print("2.Finalizar programa.")
        opcion=int(input("Ingresa opción: "))
        if(opcion==1):
            citas.LoadInfocitas()
            citas.MainMenu()
        if(opcion==2):
            isAddCitas=False
        else:
            print("Opción no validad.. Por favor ingresa nuevamente")
            os.system('pause')
