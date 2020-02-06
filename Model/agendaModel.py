from Model.connection import *

class CreateRDV():

    def __init__(self):
        self.choice = connection()
        self.title = None
        self.date = None
        self.hour = None
        self.description = None

    def create_rdv(self):
        print("--------------------------------------------------------------------------")
        print("Bienvenu sur l'Agenda, nous allons procéder à l'ajout de votre événements!")
        print("--------------------------------------------------------------------------")

        self.choice.initialize_connection()
        self.title = input("Quel est le nom de l'événement ? ")
        self.date = input("À quel date ? ")
        self.hour = input("À quel heure ? ")
        self.description = input("Une description de l'événement ? ")
        
        
        self.choice.cursor.execute("INSERT INTO Agenda(title, date, hour, description) VALUES (%s, %s, %s, %s)",(self.title,self.date,self.hour,self.description))
        self.choice.connection.commit()
        self.choice.close_connection()