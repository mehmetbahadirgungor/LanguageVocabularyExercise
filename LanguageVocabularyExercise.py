import random
from dictionary import dictionary

class App:
    
    def __init__(self):
        print(" Menü ".center(50,"*"))
        self.chosen = int(input("1- Do exercise\n2- Çıkış\nSeçim: "))
        while True:
            if self.chosen == 1:
                self.doExercise()
            elif self.chosen == 2:
                quit()
            else:
                print("Hatalı seçim yaptınız tekrar deneyiniz.")
                continue

    def doExercise(self):
        self.dictionary = dictionary
        
        self.dictionaryKey = []
        self.dictionaryValue = []

        for key, value in self.dictionary.items():
            self.dictionaryKey.append(key)
            self.dictionaryValue.append(value)

        self.randomChosen = random.randint(0, len(self.dictionaryKey)-1)

        if input(f"{self.dictionaryKey[self.randomChosen]}: ") == self.dictionaryValue[self.randomChosen]:
            print("Doğru")
        else:
            print(f"Yanlış\nDoğru Cevap: {self.dictionaryValue[self.randomChosen]}")

App()