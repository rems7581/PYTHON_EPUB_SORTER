import csv
import os
import unicodedata

baseDir = "./reverse_test/"


ct = 0

for root, dirs, files in os.walk(baseDir, topdown=True):
    for dir in dirs:
        ct = 0
        words = dir.split()
        firstName_no_accents = ''.join((c for c in unicodedata.normalize('NFD', words[0]) if unicodedata.category(c) != 'Mn'))
        #print(words[0])
        with open('firstnames.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                if firstName_no_accents == row[0]:
                    ct += 1
        if ct == 0:
            print("Dir: " + dir)
            print("    \"" + words[0] + "\" is not in file")
            print("1 - Let it be")
            print("2 - Reverse")
            print("3 - New name")
            choose = input("Choose ? ")
            while True:
                if choose == "1" or choose == "2" or choose == "3":
                    break
                else:
                    choose = input("Wrong choose, try again ? ")
            choose = int(choose)
            if choose == 1:
                print("Let...")
                print("")
            elif choose == 2:
                print("Rev...")
                newDirName = words[1] + " " + words[0]
                os.rename(baseDir + dir, baseDir + newDirName)
                for root, dirs, files in os.walk(baseDir + newDirName, topdown=True):
                    for file in files:
                        index = file.find("[")
                        newFileName = newDirName + " " + file[index:]
                        os.rename(baseDir + newDirName + "/" + file, baseDir + newDirName + "/" + newFileName)
            elif choose == 3:
                print("new")
