# -*- coding: utf-8 -*-
import json
import random
import os.path
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import getopt

# definition des variables
inputfile = ''
outputfile = ''
nbr = ''
argv = sys.argv[1:]
# recupere les argements passes au script
try:
    opts, args = getopt.getopt(argv,"hqi:o:",["ifile=","ofile=","quiet"])
except getopt.GetoptError:
    print '30_days_challenge.py -i <inputfile> -o <outputfile>'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print '30_days_challenge.py -i <inputfile> -o <outputfile>'
        sys.exit()
    elif opt in ("-q", "--quiet"):
        nbr = 30
    elif opt in ("-i", "--ifile"):
        inputfile = arg
    elif opt in ("-o", "--ofile"):
        outputfile = arg

# check si les noms de fichiers d entree et de sortie ne soient pas vide
if inputfile =='' or outputfile == '':
    print '30_days_challenge.py -i <inputfile> -o <outputfile>'
    sys.exit()

# check si le fichier d entree existe
try:
    os.path.isfile(inputfile)
    with open(inputfile, 'r') as f:
        datas = json.load(f)
    f.close()
except:
    print("Fichier source introuvable !")
    sys.exit(0)

# demande a l utilisateur combien d elements il souhaite par defaut 30
# si non défini en argument
if nbr == "" :
    nbr = raw_input("Combien de défis [30] ? ") or '30'
    nbr = int(nbr)

# selectionne un echantillon de n elements
challenge = random.sample(datas, nbr)

# ouvre le fichier de sortie et redirige la sortie standard
orig_stdout = sys.stdout
f = open(outputfile, "w")
sys.stdout = f
# ecrit le fichier de sortie
count = 0
for i in challenge:
    count+=1
    line = str(count) + ". " + i['question']
    print line

# reset la sortie standard et ferme le fichier de sortie
sys.stdout = orig_stdout
f.close()
