from Model.agendaModel import *

if __name__ == "__main__":

    Choice=""

    while Choice != 'q':
        Choice = input("Que souhaitez vous faire ?\nCréer un événement [C]\nSupprimer un évènement [S]").upper()
        if Choice == "C":
            test = CreateRDV()
            test.create_rdv()
        if Choice == "Q":
            exit()
        
        