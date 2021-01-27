#! /usr/bin/env python3
# coding: utf-8
"""
Manipuler l'export Frantext
"""
import csv
import os
import re

# colonnes des fichiers csv exportés
# id, auteur, titre, date, page, ctx gauche, pivot, ctx droit
folder_path = "export_frantext/"

# LES INTERVALS TEMPORELS
def find_date(date):
	dicoDate = dict()
	# borne minimale temporel (ici corpus Frantext = XXe siècle)
	borneInf_initiale = 1900
	# créer des intervalles de 10 en 10 (de 1900 à 1999)
	for compteur in range(1,11):
		lstTemp= list()
		bornInf = borneInf_initiale+(compteur-1)*10
		bornMax = borneInf_initiale+(compteur*10)-1
		interv = str(bornInf) + "-" + str(bornMax)
		for i in range(bornInf, bornMax+1):
			lstTemp.append(i)
			dicoDate[i]=interv
	# associer à une date un interval temporel
	for k, val in dicoDate.items(): 
		if date == k:
			return val

# ponctuation qui sera isolée autour du pivot
lstPonc=[",",".",";",":","!","?","-","…"]			

for path, dirs, files in os.walk(folder_path):
	for filename in files:

		newFile = re.sub(r'\.csv','_new.csv',filename)
		vb_lemme = re.sub(r'\.csv','',filename)
		print("Le fichier traité concerne le pivot " + str(vb_lemme))

		ajout_newFile = open("export_frantext_ajoutCol/"+newFile,'w')
		myAjout = csv.writer(ajout_newFile, delimiter=",", dialect='excel', lineterminator='\n')
		myAjout.writerow(['verbe','id','auteur','titre','intervale tps','date','page','ctx gauche','mot gauche','ponct G','pivot','ponct D','mot droit','ctx droit'])
		
		with open("export_frantext/"+filename) as csv_file:
			csv_reader = csv.reader(csv_file,delimiter=",")
			
			for row in csv_reader:
				
				intervalTps = find_date(int(row[3]))

				# GAUCHE
				ctxGauche=list()
				ctxGauche=row[5].split()

				# Isoler la ponctuation gauche
				ponctGauche = list()
				while ctxGauche[len(ctxGauche)-1] in lstPonc:
					ponctGauche.append(ctxGauche[len(ctxGauche)-1])
					del ctxGauche[len(ctxGauche)-1]

				if not ponctGauche :
					ponctG = ""
				else:
					ponctG = " ".join(ponctGauche)

				dernMot = ctxGauche[len(ctxGauche)-1]
				del ctxGauche[len(ctxGauche)-1]

				str_ctxGauche = " ".join(ctxGauche)
				
				# DROIT
				ctxDroit=list()
				ctxDroit=row[7].split()

				# Isoler la ponctuation qui suit le pivot
				ponctDroite = list()
				while ctxDroit[0] in lstPonc:
					ponctDroite.append(ctxDroit[0])
					del ctxDroit[0]

				if not ponctDroite :
					ponctD = ""
				else:
					ponctD = " ".join(ponctDroite)

				premMot = ctxDroit[0]
				del ctxDroit[0]

				str_ctxDroit = " ".join(ctxDroit)
				
				myAjout.writerow([vb_lemme,row[0],row[1],row[2],intervalTps,row[3],row[4],str_ctxGauche,dernMot,ponctG,row[6],ponctD,premMot,str_ctxDroit])

		ajout_newFile.close()
