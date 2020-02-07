from Model.agendaModel import *
from View.agendaView import *

if __name__ == "__main__":

    x = datetime.datetime.now()
    print(x.strftime("      %x"))
    vue = Loginview()
    vue.monthcurrent()

    Choice=""
    while Choice != 'q':
        print("Passer au mois suivant [N], Passer au mois précédent [P]")
        Choice = input("Créer un événement [C], Supprimer un évènement [S], Modifier un évènement [M], Regarder un évènement [L]\nQue souhaitez-vous faire ?").upper()
        if Choice == "P":       
            vue.previousmonth()

        if Choice == "N":    
            vue.nextmonth()

        if Choice == "C":
            test = Event()
            test.create_event()

        if Choice == "S":
            test = Event()
            test.delete_event()

        if Choice == "M":
            test = Event()
            test.update_event()

        if Choice == "L":
            test = Event()
            test.read_event()

        if Choice == "Q":
            print("À bientôt pour un prochain évènement ;-)")
            exit()
            
        
        