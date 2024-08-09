#!/usr/bin/env python3


import sqlite3
baseDeDonnees = sqlite3.connect('contacts.db')
curseur = baseDeDonnees.cursor()

curseur.execute("INSERT INTO Contacts (nom, prenom, adresse, telephoneFixe) VALUES (?, ?, ?, ?)", ("Dupont", "Paul", "15 rue Louis Pasteur 10000 Troyes", "0325997452")) # On ajoute un enregistrement
baseDeDonnees.commit()
baseDeDonnees.close()


baseDeDonnees = sqlite3.connect('contacts.db')
curseur = baseDeDonnees.cursor()
curseur.execute("SELECT nom, prenom, telephoneFixe FROM Contacts WHERE id = ?", ("2",))
contact = curseur.fetchone()
print(contact , "ytfvyv")
baseDeDonnees.close()
