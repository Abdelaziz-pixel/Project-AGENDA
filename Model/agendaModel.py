from Model.connection import *

class Event():

    def __init__(self):
        self.choice = connection()
        self.title = None
        self.date = None
        self.hour = None
        self.description = None

    def create_event(self):
        print("--------------------------------------------------------------------------")
        print("Bienvenu sur l'Agenda, nous allons procéder à l'ajout de votre événement!")
        print("--------------------------------------------------------------------------")

        self.choice.initialize_connection()
        self.title = input("Quel est le nom de l'événement ? ")
        self.date = input("À quel date ? ")
        self.hour = input("À quel heure ? ")
        self.description = input("Une description de l'événement ? ")
        
        
        self.choice.cursor.execute("INSERT INTO Agenda(title, date, hour, description) VALUES (%s, %s, %s, %s)",(self.title,self.date,self.hour,self.description))
        self.choice.connection.commit()
        self.choice.close_connection()

    def delete_event(self):
        self.choice.initialize_connection()
        self.date = input("À quel date à eu lieu l'évènement ? ")
        self.hour = input("À quel heure à eu lieu l'évèvement ? ")

        self.choice.cursor.execute("DELETE FROM Agenda WHERE date=%s AND hour=%s;",(self.date,self.hour,))
        self.choice.connection.commit()
        self.choice.close_connection()

    def update_event(self):
        self.choice.initialize_connection()
        column = ""
        while column not in ["title, date, hour, description"]:
            column = input("{title, date, hour, description}\nQue souhaitez-vous modifier ?")
            datta = input("Entrer la nouvelle information:")
            self.date = input("Entrer la date du rendez-vous:")
            self.hour = input("Entrer l'heure du rendez-vous:")
            self.choice.initialize_connection()
            self.choice.cursor.execute("UPDATE Agenda set " + column + " = %s WHERE date = %s AND hour = %s;", (datta, self.date, self.hour,))
            self.choice.connection.commit()
            self.choice.close_connection()

    def read_event(self):
        self.choice.initialize_connection()
        self.choice.cursor.execute("SELECT * FROM Agenda;")
        test = self.choice.cursor.fetchall()
        self.choice.close_connection()
        print(test)

        
        

