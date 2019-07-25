#Arquivo main.py
#############################################################################################
from googletrans import Translator
from textblob import TextBlob
from unidecode import unidecode
import csv
import mysql

#Contadores
numPos = 0
numNeg = 0
total = 0

lista=[]

with open('insreduc.txt') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        lista.append(row['nm_frase'])
        print(row['nm_frase'])
        
linhas = []
registro = []
registros= []
for text in lista:
    #pegando o texto
    textPTBR = unidecode(text)

    #traduzindo
    if textPTBR != None:
        textEN = Translator().translate(textPTBR)
    else:
        textEN = "embranco"

        
    #analisando o sentimento
    sentiment = TextBlob(textEN.text)

    # Exibindo...
    registro=[]
    registro=[textPTBR , textEN.text ,str(sentiment.polarity)]
    registros.append(registro)
    
    # print(textPTBR + "," + textEN.text + "," + str(sentiment.polarity) )

    total += 1
    if sentiment.polarity > 0:
        numPos += 1
    elif sentiment.polarity < 0:
        numNeg += 1

# Sentimento geral
mediaPos = numPos / total
mediaNeg = numNeg / total

nCont=0
nTotal= registros.count

with open('retorno.csv', 'w') as csvfile:
    fieldnames = ['nm_frase', 'nu_resultado']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()

    for percorre in registros:
        #print(percorre[0] + "," + percorre[2]) 
        writer.writerow({'nm_frase':registros[nCont][0],'nu_resultado':registros[nCont][2]})
        nCont=nCont + 1
                    
    
#print('Porcentagem de comentários positivos: ' + str(mediaPos))
#print('Porcentagem de comentários negativos: ' + str(mediaNeg))
