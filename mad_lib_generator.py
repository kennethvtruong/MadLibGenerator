class Mad_Lib_Generator:
    def __init__(self, story=str, word1=str, word2=str, word3=str, word4=str, word5=str, word6=str, word7=str,
                 word8=str, word9=str, word10=str, word11=str, word12=str):
        self.story = story
        self.word1 = word1
        self.word2 = word2
        self.word3 = word3
        self.word4 = word4
        self.word5 = word5
        self.word6 = word6
        self.word7 = word7
        self.word8 = word8
        self.word9 = word9
        self.word10 = word10
        self.word11 = word11
        self.word12 = word12

    def get_input(self):
        self.word1 = input("Type an adjective: ")
        self.word2 = input("Type a noun: ")
        self.word3 = input("Type a verb in the past tense: ")
        self.word4 = input("Type an adverb: ")
        self.word5 = input("Type an adjective: ")
        self.word6 = input("Type a noun: ")
        self.word7 = input("Type another noun: ")
        self.word8 = input("Type an adjective: ")
        self.word9 = input("Type a verb: ")
        self.word10 = input("Type an adverb: ")
        self.word11 = input("Type a verb in the past tense: ")
        self.word12 = input("Type an adjective: ")
        print("Today I went to the zoo. I saw a(n) %s %s jumping up and down in its tree. \n"
              "He %s %s through the large tunnel that led to its %s %s \n"
              "I got some peanuts and passed them through the cage to a gigantic gray %s towering above my head. \n"
              "Feeding that animal made me hungry. I went to get a %s scoop of ice cream. It filled my stomach.\n"
              "Afterwards I had to %s %s to catch our bus. When I got home I %s my mom for a %s day at the zoo." %
              (self.word1, self.word2, self.word3, self.word4, self.word5, self.word6, self.word7, self.word8,
               self.word9, self.word10, self.word11, self.word12))


my_lib = Mad_Lib_Generator("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
my_lib.get_input()
