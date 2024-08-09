#!/usr/bin/env python3

import csv

fichier = open("fichier.csv","rt")
lect = csv.reader(fichier,delimiter=";")
for ligne in lect:
    print(ligne)

