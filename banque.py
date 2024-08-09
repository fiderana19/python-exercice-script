#!/usr/bin/env python3

comptes = {"Paul":154.74 , "Marie":418.45 , "Jean":96.20 , "Lionel":914.21}

def depot(client):
    valeur = float(input("Quel montant voulez-vous deposer ?"))
    comptes[client] += valeur
    print("Operation effectué.")
def retrait(client):
    valeur = float(input("Quel montant voulez-vous retirer ?"))
    if comptes[client] >= valeur:
        comptes[client] -= valeur
        print("Retrait reussi.")
    else:
        print("Operation impossible : Votre solde est insuffisant.")
while True:
    print("BANQUE\n")
    print("Client \t Solde")
    print("-----------------")
    for client,solde in comptes.items():
        print(client,"\t",str(solde))
    operation = input("Choisissez une operation (D : Depot - R : Retrait - Q : Quitter) : ").upper()
    if operation == 'D':
        client = input("Entrez le nom du client sur lequel effectuer le depot : ")
        depot(client)
    elif operation == 'R':
        client = input("Entrez le nom du client sur lequel effectuer le retrait : ")
        retrait(client)
    elif operation == 'Q':
        print("Au revoir !")
