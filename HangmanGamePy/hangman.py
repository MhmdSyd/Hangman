import os
import random
os.chdir(os.path.dirname(__file__))


class GenerateWord():

    def setLevel(self, filename):
        self.filename = filename

    def getWord(self):
        self.file = open(self.filename, "r")
        self.word = self.file.readlines()
        self.file.close()
        self.index = random.randint(0, len(self.word) - 1)
        return self.word[self.index]


class CreateHistory():
    def setFile(self, filename):
        self.filename = filename

    def addHistoryLine(self, user, score):
        self.myfile = open(self.filename, "a")
        strline = str(user + "-" + score + "\n")
        self.myfile.write(strline)
        self.myfile.close()


guessObj = GenerateWord()
createHis = CreateHistory()

while True:
    print("1- Enter your account\n2- show top 10 score\n3- show my History")
    mychoice = int(input("Enter your Choice: "))
    if mychoice == 1:
        userFile = open("userNames.txt", "r")
        userName = str(input("Enter user Name: "))
        pWord = str(input("Enter passWord: "))
        userList = list(userFile.readlines())
        for i in userList:
            user, pw = i.split("-")
            if user == userName and pw.strip("\n") == pWord:
                print(f"welcome {user} !")
                userFile.close()
                userFile = open("difficultyLevel.txt", "r")
                print("1-easy\n2-medium\n3-advance")
                leveList = userFile.readlines()
                print(leveList)
                defLevel = int(input("Enter Difficulty level:"))
                if defLevel in [1, 2, 3]:
                    fileStr = str(
                        leveList[defLevel - 1].strip("\n"))+"Word.txt"
                    userFile.close()
                    guessObj.setLevel(fileStr)
                    wordCheck = list(guessObj.getWord().strip("\n"))
                    print(wordCheck)
                    hiddenWord = list("_" * (len(wordCheck)))
                    print("".join(hiddenWord))
                    tryNum = 0
                    while hiddenWord.count("_") > 0 and tryNum < 10:
                        tryNum += 1
                        guessLetter = str(input("Enter geuss letter: "))
                        if guessLetter in wordCheck:
                            hiddenWord[wordCheck.index(
                                guessLetter)] = guessLetter
                            print("".join(hiddenWord))
                        else:
                            print("incorrect guess")
                            print("".join(hiddenWord))
                    if tryNum >= 10:
                        print("bad luck!")
                        createHis.setFile("history.txt")
                        createHis.addHistoryLine(userName, "0")
                    else:
                        print("good job!", tryNum)
                        createHis.setFile("history.txt")
                        createHis.addHistoryLine(
                            userName, str((10 - tryNum) * 15))

                        myfile = open("hight10Score.txt", "r")
                        hight10Score = myfile.readlines()

                        minScore = hight10Score[-1].strip("\n").split("-")[-1]

                        print(minScore)
                        myfile.close()
                        if int(minScore) < int((10 - tryNum) * 15):
                            hight10Score[-1] = str(userName +
                                                   "-" + str((10 - tryNum) * 15) + "\n")
                            myfile = open("hight10Score.txt", "w")
                            myfile.write(",".join(hight10Score))

                        else:
                            print("not new score!")

    elif mychoice == 2:
        myfile = open("hight10Score.txt", "r")
        print(myfile.read())
        myfile.close()
    elif mychoice == 3:
        myuser = str(input("Enter userName: "))
        myfile = open("history.txt", "r")
        historyList = myfile.readlines()
        for i in historyList:
            if i.split("-")[0] == myuser:
                print(i.strip("\n"))
        myfile.close()

    else:
        print("invalid input!")
    print("=" * 30)
