# -*- coding: utf-8 -*-
import json
import random
import os.path
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import getopt


inputfile = ''
outputfile = ''
nbr = ''
argv = sys.argv[1:]
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

if inputfile =='' or outputfile == '':
    print '30_days_challenge.py -i <inputfile> -o <outputfile>'
    sys.exit()

# check si le fichier source existe
try:
    os.path.isfile(inputfile)
    with open(inputfile, 'r') as f:
        datas = json.load(f)
except:
    print("Fichier source introuvable !")
    sys.exit(0)

# demande a l utilisateur combien d elements il souhaite par defaut 30
if nbr == "" :
    nbr = raw_input("Combien de défis [30] ? ") or '30'
    nbr = int(nbr)

# selectionne un echantillon de n elements
challenge = random.sample(datas, nbr)

orig_stdout = sys.stdout
f = open(outputfile, "w")
sys.stdout = f
# affiche les n defis
count = 0

for i in challenge:
    count+=1
    line = str(count) + ". " + i['question']
    print line

sys.stdout = orig_stdout
f.close()
