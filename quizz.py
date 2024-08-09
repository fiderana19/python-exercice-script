#!/usr/bin/env python3

print("Bienvenue dans ce quizz LDC !!!!!!")
point  = 0
q1 = input(" Question 1 : Qui a gagné la LDC en 2012 ? : ")
if q1 == 'chelsea':
    point = point + 5

q2 = input(" Question 2 : Qui est le buteur en final 2023 ? : ")
if q2 == 'Rodri':
    point = point + 5
    
q3 = input(" Question 3 : Qui a marqué en final 2021 ? : ")
if q3 == 'Havertz':
    point = point + 5

q4 = input(" Question 4 : Qui a gagné la competition en 2019 ? : ")
if q4 == 'liverpool':
    point = point + 5

if point >= 10:
    print("Bien joué ! , vous avez " , point , "points")
else:
    print("Dommage ! , vous avez ", point , "points")
