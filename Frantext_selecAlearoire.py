#! /usr/bin/env python3
# coding: utf-8
"""
- sélectioonner aléatoirement 20 exemples dans chaucun des fichiers csv
- regrouper dans un fichier csv les exemples retenus, et dans un autre fichier csv les exemples non retenus
- compter le nombre d'exemples par intervalle temporel et par motif (pivot)
"""
import csv
import os
import re

import random

folder_path = "export_frantext_ajoutCol/"

compteGlobal = open("compte.csv",'w')
myCompte = csv.writer(compteGlobal, delimiter=",", dialect='excel', lineterminator='\n')
myCompte.writerow(['verbe','nb occ','interval', 'nb occ par interv'])

newFile = open("verbes_choixAletoire.csv",'w')

myAjout = csv.writer(newFile, delimiter=",", dialect='excel', lineterminator='\n')
myAjout.writerow(['ID select','verbe','id Frantext','auteur','titre','intervale tps','date','page','ctx gauche','mot gauche','ponct G','pivot','ponct D','mot droit','ctx droit'])

pioche = open("verbes_pioche.csv",'w')

myPioche = csv.writer(pioche, delimiter=",", dialect='excel', lineterminator='\n')
myPioche.writerow(['verbe','id','auteur','titre','intervale tps','date','page','ctx gauche','mot gauche','ponct G','pivot','ponct D','mot droit','ctx droit'])

# ajouter un ID qui permettra de garder trace de l'ordre aléatoire de sélection
ID = 0

for path, dirs, files in os.walk(folder_path):
	for filename in files:
		
		vb_lemme = re.sub(r'_new\.csv','',filename)
		print("Le fichier traité concerne le pivot " + str(vb_lemme))
		
		with open("export_frantext_ajoutCol/"+filename) as csv_file:
			csv_reader = csv.reader(csv_file,delimiter=",")
			
			line_count=-1
			
			interval_count=dict()
			dicGlobal=dict()

			for row in csv_reader:
				line_count += 1
				# ne pas prendre l'entête
				if line_count > 0:
					if row[4] in dicGlobal :
						dicGlobal[row[4]].append(row)
					else:
						dicGlobal[row[4]] = [row]

			for interv,lstExples in dicGlobal.items():
				myCompte.writerow([vb_lemme,line_count,interv,len(lstExples)])
				
				if len(lstExples) < 21:
					for exemple in lstExples:
						ID+=1
						exemple.insert(0, ID)
						myAjout.writerow(exemple)
				else:
					random.shuffle(lstExples)
					for i in range(20):
						ID+=1
						myList = lstExples[i]
						myList.insert(0, ID) 
						myAjout.writerow(myList)
					for p in range(21, len(lstExples)):
						myPioche.writerow(lstExples[p])
