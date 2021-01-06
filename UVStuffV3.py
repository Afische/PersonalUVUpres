import os, sys, stat, re
from shutil import copy
import time

subjectDir = os.path.dirname(os.path.realpath(__file__))
pythonDir = sys.executable

#-----PASTE AND RENAME MASKS TO EXPRESSION FOLDER-----

masks = []
maskDirectory = subjectDir+'\\masks'
expressionDirectory = subjectDir+'\\expressions'
for expressionFolder in os.listdir(expressionDirectory):
	for maskFile in os.listdir(maskDirectory):
		if maskFile.endswith(".obj") or maskFile.endswith(".OBJ"):
			maskNumber = re.sub('[^0-9]','', maskFile)
			if expressionFolder == maskNumber:
				if os.path.exists(subjectDir+'\\expressions\\'+expressionFolder+'\\UV.OBJ'):
					print('A UV Already exists at: '+subjectDir+'\\expressions\\'+expressionFolder)
				else:
					#os.chmod(subjectDir+'\\expressions\\'+expressionFolder, stat.S_IRWXU)
					copy(subjectDir+'\\masks\\'+maskFile, subjectDir+'\\expressions\\'+expressionFolder)
					os.rename(subjectDir+'\\expressions\\'+expressionFolder+'\\'+maskFile, subjectDir+'\\expressions\\'+expressionFolder+'\\UV.obj')
					print('Copied UV to: '+subjectDir+'\\expressions\\'+expressionFolder+'\\UV.obj')


#-----WRITE TO DOTHESE, CREATE TEMP EXPS FILES-----

integers = open(subjectDir+'\\dothese.txt', 'r')

ints = []
a = 0
for line in integers:
	ints.append(line.strip())
	if len(ints[a]) < 2:
		ints[a] = '0'+str(line)
	else:
		ints[a] = str(line)
	a+=1

newInts = []
for line in ints:
	newInts.append(int(line.strip()))
	
b = ""
newList = b.join(ints)
integers.close()

integers = open(subjectDir+'\\dothese.txt', 'w+')
integers.write(newList)
integers.close()

for x in newInts:
	if x < 10:
		x = '0'+str(x)
		exp = open(subjectDir+'\\tempExps\\exp'+str(x)+'.txt', "w+")
		exp.write(str(x))
		exp.write("\n")
		exp.close()
	else:
		exp = open(subjectDir+'\\tempExps\\exp'+str(x)+'.txt', "w+")
		exp.write(str(x))
		exp.write("\n")
		exp.close()

#-----REMOVE WHITESPACE FROM DOTHESE.TXT AND CONFIG.TXT-----

with open(subjectDir+'\\dothese.txt', "r") as dothese:
	lines = dothese.readlines()
lines = [line.replace(' ', '') for line in lines]
with open(subjectDir+'\\dothese.txt', "w") as dothese:
	dothese.writelines(lines)

with open(subjectDir+'\\config.txt', "r") as config:
	lines = config.readlines()
lines = [line.replace(' ', '') for line in lines]
with open(subjectDir+'\\config.txt', "w") as config:
	config.writelines(lines)

#-----FIND SMALLEST AND LARGEST EXPRESSION-----

#smallestInt = min(ints)
#largestInt = max(ints)
#if smallestInt < 10:
#	smallestInt = '0'+str(smallestInt)
#if largestInt < 10:
#	largestInt = '0'+str(largestInt)
#tempSmall = open(subjectDir+'\\tempSmall', "w+")
#tempSmall.write(str(smallestInt))
#tempSmall.close()
#tempLarge = open(subjectDir+'\\tempLarge', "w+")
#empLarge.write(str(largestInt))
#tempLarge.close()