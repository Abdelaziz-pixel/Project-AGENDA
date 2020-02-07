from Model.agendaModel import *

if __name__ == "__main__":

    Choice=""

    while Choice != 'q':
        Choice = input("Créer un événement [C]\nSupprimer un évènement [S]\nModifier un évènement [M]\nQue souhaitez-vous faire ?").upper()
        if Choice == "C":
            test = Event()
            test.create_event()
        if Choice == "S":
            test = Event()
            test.delete_event()
        if Choice == "M":
            test = Event()
            test.update_event()
        if Choice == "Q":
            print("À bientôt pour un prochain évènement ;-)")
            exit()
            
        
        