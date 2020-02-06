from Model.agendaModel import *

if __name__ == "__main__":

    Choice=""

    while Choice != 'q':
        Choice = input("Créer un événement [C]\nSupprimer un évènement [S]\nQue souhaitez vous faire ?").upper()
        if Choice == "C":
            test = Event()
            test.create_event()
        if Choice == "S":
            pass
        if Choice == "Q":
            exit()
        
        