"Name-Surname: Fatih YELBOĞA, Student ID: 270201028"
import random

def Main_Menu():
    print("\nHit 'v' To View The Status Of The Game.")
    print("Hit 't' To Spend a Tip.")
    print("Hit 's' To Try And Stack Your Card.")
    print("Hit 'd' To Discard Your Card And Earn a Tip.")
    print("Hit 'h' To View This Menu.")
    print("Hit 'q' To Quit.")
#Input: None
#Output: None
#Main Menu Is Dısplayed

class Game: #All Variables and Functions Of The Game Are In This Class
    def __init__(self):
        self.deck=[['b', 1], ['b', 1], ['b', 1], ['b', 2], ['b', 2], ['b', 3], ['b', 3], ['b', 4], ['w', 1], ['w', 1], ['w', 1],
         ['w', 2], ['w', 2], ['w', 3], ['w', 3], ['w', 4]]
        self.deck = self.Shuffle(self.deck)
        self.player_hand = self.deck[0:3]
        self.player_view = self.deck[0:3]
        #The Purpose Of This "player_view" List Is To Make The Computer Give a Different Tip Each Time
        self.computer_hand = self.deck[3:6]
        self.computer_view = [["!",-1],["!",-1],["!",-1]]
        #The Elements Of The "computer_view" List Are Updated According To The Tip Given By The User
        self.stack = [[],[]]
        self.trash = []
        del self.deck[0:6]
        self.tips=3
        self.lives=2
        self.turn=0
    #Input: None
    #Output: Consturctor Methods Do Not Give Output
    #With This Constructor Method, The Attributes Of The Object Of This Class Are Assigned

    def Player_Tip_Operations(self, tip):
        tip_list = tip.split(",")
        i = 0
        for element in tip_list: #For Example, For Tip "1,3,w" The "computer_view" List Would Be [["w",-1]["!",-1]["w",-1]]
            if not i == len(tip_list) - 1:
                if tip_list[len(tip_list) - 1].isnumeric():
                    self.computer_view[int(element) - 1][1] = int(tip_list[len(tip_list) - 1])
                else:
                    self.computer_view[int(element) - 1][0] = tip_list[len(tip_list) - 1]
            i += 1
        self.tips-=1
        self.turn=1
    #Input: The Tip Entered By The Player (parameter: tip)
    #Output: None
    #With This Function, The Elements Of The "self.computer_view" list Are Updated According To The Tip Given by The Player
    #Number Of Tips Decreases By 1 (self.tips-=1) and The Turn Of Game Goes To The Computer (self.turn=1)

    def Player_Stack_Operations(self,card_number):
        card = self.player_hand[card_number - 1]
        if card[0] == "b": #If The Color Of Card Is "black", Operations Are Done Here
            if len(self.stack[0]) == 0 and  card[1] == 1:
                self.Player_Stack_Insert(card_number)
            elif len(self.stack[0]) == 0 and not card[1] == 1:
                self.Player_Trash_Discard(card_number)
                self.lives-=1
            elif not len(self.stack[0]) == 0:
                if self.stack[0][len(self.stack[0])-1][1] == card[1] - 1:
                    self.Player_Trash_Discard(card_number)
                else:
                    self.Player_Trash_Discard(card_number)
                    self.lives-=1
        else: #If The Color Of Card Is "white", Operations Are Done Here
            if len(self.stack[1]) == 0 and card[1] == 1:
                self.Player_Stack_Insert(card_number)
            elif len(self.stack[1]) == 0 and not card[1] == 1:
                self.Player_Trash_Discard(card_number)
                self.lives-=1
            elif not len(self.stack[0]) == 0:
                if self.stack[1][len(self.stack[0])-1][1] == card[1] - 1:
                    self.Player_Stack_Insert(card_number)
                else:
                    self.Player_Trash_Discard(card_number)
                    self.lives-=1
        self.turn=1
    #Input: The Card Number Entered By The Player (parameter: card_number)
    #Output: None
    #With This Function, If The Card Number Received From The Player Is Suitable For The Stack, It Is Added To The "self.stack" List
    #Otherwise It Is Discarded To The "self.trash" List and Number Of Lives Decreases By 1 (self.lives-=1)
    #The Turn Of Game Goes To The Computer (self.turn=1)

    def Player_Stack_Insert(self,card_number):
        card = self.player_hand[card_number - 1]
        if card[0] == "b": #If Card Is "b", Operations Are Done Here
            self.stack[0].append(card)
            del self.player_hand[card_number-1]
            del self.player_view[card_number-1]
            if len(self.deck) > 0:
                self.player_hand.append(self.deck[0])
                self.player_view.append(self.deck[0])
                del self.deck[0]
        else: #If Card Is "w", Operations Are Done Here
            self.stack[1].append(card)
            del self.player_hand[card_number-1]
            del self.player_view[card_number-1]
            if len(self.deck) > 0:
                self.player_hand.append(self.deck[0])
                self.player_view.append(self.deck[0])
                del self.deck[0]
        self.turn=1
    #Input: The Card Number Entered By The Player (parameter: card_number)
    #Output: None
    #With This Function, According To The Card Number Entered By The Player, The Relevant Card Is Added To The "self.stack" List
    #The Relevant Card Is Deleted From The "self.player_hand" and "self.player_view" Lists, If There Is a Card In The "deck" List, The First Card Is Added To These Lists
    #The Turn Of Game Goes To The Computer (self.turn=1)

    def Player_Trash_Discard(self,card_number):
        card = self.player_hand[card_number-1]
        self.trash.append(card)
        self.player_hand.remove(self.player_hand[card_number-1])
        self.player_view.remove(self.player_view[card_number-1])
        if len(self.deck) > 0:
            self.player_hand.append(self.deck[0])
            self.player_view.append(self.deck[0])
            del self.deck[0]
        self.turn = 1
    #Input: The Card Number Entered By The Player (parameter: card_number)
    #Output: None
    #With This Function, According To The Card Number Entered By The Player, The Relevant Card Is Discarded To The "self.trash" List
    #The Relevant Card Is Deleted From The "self.player_hand" and "self.player_view" Lists, If There Is a Card In The "deck" List, The First Card Is Added To These Lists
    #The First Card In The "self.deck" List Is Deleted
    #The Turn Of Game Goes To The Computer (self.turn=1)

    def Computer_Tip_Operations(self):
        tips = []
        counter = 1
        tip_1, tip_2, tip_3, tip_4, tip_5, tip_6 = "", "", "", "", "", ""
        for i in self.player_view: #Computer Finds All Tips According To "self.playerview" list
            if str(i).__contains__("b"):
                tip_1 = tip_1 + f"{counter},"
            if str(i).__contains__("w"):
                tip_2 = tip_2 + f"{counter},"
            if str(i).__contains__("1"):
                tip_3 = tip_3 + f"{counter},"
            if str(i).__contains__("2"):
                tip_4 = tip_4 + f"{counter},"
            if str(i).__contains__("3"):
                tip_5 = tip_5 + f"{counter},"
            if str(i).__contains__("4"):
                tip_6 = tip_6 + f"{counter},"
            counter += 1
        if not len(tip_1) == 0:
            tip_1 += "b"
            tips.append(tip_1)
        if not len(tip_2) == 0:
            tip_2 += "w"
            tips.append(tip_2)
        if not len(tip_3) == 0:
            tip_3 += "1"
            tips.append(tip_3)
        if not len(tip_4) == 0:
            tip_4 += "2"
            tips.append(tip_4)
        if not len(tip_5) == 0:
            tip_5 += "3"
            tips.append(tip_5)
        if not len(tip_6) == 0:
            tip_6 += "4"
            tips.append(tip_6)
        #The Final Version Of The Tip Is Prepared By Adding The Relevant "b, w, 1,2,3,4" To The End Of The Tips
        tips_length = []
        for item in tips:
            tips_length.append(len(item))
        if len(tips) > 0:
            for item in tips:
                if len(item) == max(tips_length):
                    print(f"\nComputer Gives a Tip : {item}\n")
                    division = item.split(",")
                    i = 0
                    for element in division:
                        if not i == len(division) - 1:
                            if division[len(division) - 1].isnumeric():
                                self.player_view[int(element) - 1] = [self.player_view[int(element)-1][0],-1]
                            else:
                                self.player_view[int(element) - 1] = ["!",self.player_view[int(element)-1][1]]
                        i += 1
                    self.tips-=1
                    self.turn=0
                    break
        #If The Number Of Tips Is Greater Than 0 and There Are Tips In The "tips" List, The Computer Gives The Tip To The Player
        #The "self.player_view" List Is Updated After The Tip Given The Computer So The Computer Gives The updated Tip Each Time
        else:
            self.Computer_Trash_Operations()
    #Input: None
    #Output: None
    #With This Function, The Computer Adds All The Tip To The Tips List According To The "self.player_view" List and Tells The Player The Longest Tip In The List
    #Otherwise If There Is No Tip In The "tip" List, That Is, If The Player Knows All The Cards In His/Her Hand or Does Not Have Any Cards, The Computer Discards The Card To The "trash" List
    #If The Computer Gives Tip at the Player, The Number Of Tip Decreases By 1 (self.tips-=1) and The Turn Goes To The Player (self.turn=0). If Computer Discards The Card To The "self.trash" List, The Number Of Tips Increases By 1 and The Turn Goes To The Player

    def Computer_Stack_Available_Control(self):
        i=0
        for element in self.computer_view:
            if self.stack[0].__contains__(element): #If The Card Was Found In The First Element("black") Of The "self.stack" List, Computer Discards a Card.
                print(f"\nComputer Discards a Card : {element}\n")
                self.Computer_Trash_Discard(i)
                self.tips+=1
                return True
            elif self.stack[1].__contains__(element): #If The Card Was Found In The Second Element("white") Of The "self.stack" List, Computer Discards a Card.
                print(f"\nComputer Discards a Card : {element}\n")
                self.Computer_Trash_Discard(i)
                self.tips+=1
                return True
            i+=1
        return False
    #Input: None
    #Output: (True or False) If Card Is Found, The Function Return "True". If Not Found, The Function Return "False"
    #With This Function, If Any Of The Cards In The "self.computer_view" List Are Found In The "self.stack" List, The Computer Will Discard That Card Into The "self.trash" List
    #At The Same Time, If Computer Dıscards The Card To The "self.trash" List, The Number Of Tips Increases By 1 (self.tips+=1)

    def Computer_Stack_Operations(self):
        for card in self.computer_view:
            if not card[0]=="!" and not card[1]==-1: #If The Card In The "self.computer_view" List Is Not ["!", - 1], Continue
                if card[0] == "b": #The Operations For The Cards With Color "black" Will Be Done Here
                    if len(self.stack[0]) == 0 and card[1] == 1:
                        print(f"\nComputer Stacks a Card : {card}\n")
                        self.Computer_Stack_Insert(card)
                        return True
                    elif not len(self.stack[0])==0:
                        if self.stack[0][len(self.stack[0]) - 1][1] == card[1] - 1:
                            print(f"\nComputer Stacks a Card : {card}\n")
                            self.Computer_Stack_Insert(card)
                            return True
                else: #The Operations For The Cards With Color "white" Will Be Done Here
                    if len(self.stack[1]) == 0 and card[1] == 1:
                        print(f"\nComputer Stacks a Card : {card}\n")
                        self.Computer_Stack_Insert(card)
                        return True
                    elif not len(self.stack[1])==0:
                        if self.stack[1][len(self.stack[0]) - 1][1] == card[1] - 1:
                            print(f"\nComputer Stacks a Card : {card}\n")
                            self.Computer_Stack_Insert(card)
                            return True
        return False
    #Input: None
    #Output: (True or False)
    #True: If There Is The Appropriate Card For The "self.stack" List, The Function Returns "True"
    #False: Otherwise The Function Returns "False"
    #With This Function, If The Suitable Card Is Found For The "self.stack" List In The "self.computer_view" List, The Card Is Added To The Corresponding Place In The "self.stack" List

    def Computer_Stack_Insert(self,card):
        if card[0]=="b": #The Operations For The Cards With Color "black" Will Be Done Here
            self.stack[0].append(card)
            self.computer_hand.remove(card)
            self.computer_view.remove(card)
            if len(self.deck) > 0:
                self.computer_hand.append(self.deck[0])
                self.computer_view.append(["!",-1])
                del self.deck[0]
        else: #The Operations For The Cards With Color "white" Will Be Done Here
            self.stack[1].append(card)
            self.computer_hand.remove(card)
            self.computer_view.remove(card)
            if len(self.deck) > 0:
                self.computer_hand.append(self.deck[0])
                self.computer_view.append(["!",-1])
                del self.deck[0]
    #Input: The Card That Computer Will Add To The "self.stack" List (parameter: card)
    #Output: None
    #With This Function, The Card That The Computer Will Add To The "self.stack" List Is Added To The Relevant Place In The "self.stack" List.
    #The Relevant Card Is Deleted From The "self.computer_hand" and "self.computer_view" Lists, If There Is a Card In The "deck" List, The First Card Is Added To The "self.computer_hand" List
    #["!", - 1] Is Added To The "self.computer_view" list and The First Card In The "self.deck" List Is Deleted

    def Computer_Trash_Discard(self,card_number):
        self.trash.append(self.computer_hand[card_number])
        del self.computer_hand[card_number]
        del self.computer_view[card_number]
        if len(self.deck) > 0:
            self.computer_hand.append(self.deck[0])
            self.computer_view.append(["!",-1])
            del self.deck[0]
        self.tips += 1
        self.turn = 0
    #Input: The Index Of Card That Computer Will Deleted
    #Output: None
    #With This Function, That The Computer Will Discard To The "self.trash" List
    #The Relevant İndex Of Card Is Deleted From The "self.computer_hand" and "self.computer_view" Lists, If There Is a Card In The "self.deck" List, The First Card Is Added To The "self.computer_hand" List
    #["!", - 1] Is Added To The "self.computer_view" list and The First Card In The "self.deck" List Is Deleted
    #The Number Of Tips Increases By 1 (self.tips+=1) and The Turn Of Game Goes To The Player (self.turn=0)

    def Computer_Trash_Operations(self):
        control = 0
        i = 0
        for card in self.computer_view:
            if card == ["!", -1]: #If The Element Is ["!", - 1], Continue
                print(f"\nComputer Discards a Card : {self.computer_hand[i]}\n")
                self.Computer_Trash_Discard(i)
                control = 1
                i += 1
                break
        if not control == 1: #If "self.computer_view" List Does Not Have Element ["!", - 1], Continue
            print(f"\nComputer Discards a Card : {self.computer_hand[0]}\n")
            self.Computer_Trash_Discard(0)
    #Input: None
    #Output: None
    #With This Function, If The Computer Has an Element Of "self.computer_view" ["!", - 1], It Discards That Element To The "self.trash" List
    #Otherwise It Discards Its First Element To The "self.trash" List

    def Shuffle(self,deck):
        shuffled_deck = []
        control = 0
        numbers = list(range(0,16))
        while control < 16: #Since There Are 16 Cards, This Process Is Done 16 Times
            num = random.choice(numbers)
            shuffled_deck.append(deck[num])
            numbers.remove(num)
            control += 1
        return shuffled_deck
    #Input: The Deck List
    #Output: The Shuffled List ("shuffled_deck")
    #With This Function, The Elements Of The List Taken As Parameter Are Randomly Selected and Transferred To The "shuffled_deck" List and This List is Returned


print("Welcome! Let's Play!")
Main_Menu()
Game_Instance = Game()
while True:
    if Game_Instance.turn==0:
        choice = input("Please Enter Your Choice (v,t,s,d,h,q) : ")
        if choice=="v" or choice=="V": #If The Player Enters "v" or "V", Show Current Informations
            print(f"\nComputer's Hand : {Game_Instance.computer_hand}")
            print(f"Number Of Tips Left : {Game_Instance.tips}")
            print(f"Number Of Lives Left : {Game_Instance.lives}")
            print(f"Current Stacks => Black Stack : {Game_Instance.stack[0]}   White Stack : {Game_Instance.stack[1]}")
            print(f"Current Trash : {Game_Instance.trash}\n")
        elif choice=="t" or choice=="T":
            if Game_Instance.tips > 0 and len(Game_Instance.computer_hand) > 0: #If The Number Of Tips Is Greater Than 0, Tip Is Taken From The Player.
                player_tip = input("Please Enter TİP For COMPUTER : ").strip()
                Game_Instance.Player_Tip_Operations(player_tip)
            elif Game_Instance.tips > 0 and not len(Game_Instance.computer_hand) > 0:  #If The "computer_hand" Have Not a Card, The Turn Will Pass To The Computer With a Warning Message.
               print("Not Possible! No Computer's Card Left!")
               Game_Instance.turn=1
            else: #If The Number Of Tips Is 0 or Less, The Turn Will Pass To The Computer With a Warning Message.
                print("Not Possible! No tips left!")
                Game_Instance.turn=1
        elif choice=="s" or choice=="S":
            if len(Game_Instance.player_hand) > 0: #If Number Of "player_hand" Is Greater Than 0, Get Card Number From The Player For Stack Operations
                try:
                    stack_card_number = int(input("Please Enter The Number Of Card For STACK : "))
                    Game_Instance.Player_Stack_Operations(stack_card_number)
                except:
                    print("Invalid Card Number!")
                    Game_Instance.turn=1
            else: #If The Number Of "player_hand" Is 0 or Less, The Turn Will Pass To The Computer With a Warning Message.
                print("Not Possible! No Player's Card Left!")
                Game_Instance.turn=1
        elif choice=="d" or choice=="D":
            if len(Game_Instance.player_hand) > 0: #If Number Of "player_hand" Is Greater Than 0, Get Card Number From The Player For Trash Operations
                try:
                    trash_card_number = int(input("Please Enter The Number Of Card For TRASH : "))
                    Game_Instance.Player_Trash_Discard(trash_card_number)
                    Game_Instance.tips += 1  # The Number Of Tips Increases By 1
                except:
                    print("Invalid Card Number!")
                    Game_Instance.turn=1
            else: #If The Number Of "player_hand" Is Greater Than 0, The Turn Will Pass To The Computer With a Warning Message.
                print("Not Possible! No Player's Card Left!")
                Game_Instance.turn=1
        elif choice=="h" or choice=="H":
            Main_Menu()
        elif choice=="q" or choice=="Q":
            break
        else:
            print("Please Enter a Valid Choice (v,t,s,d,h,q)!")
    else:
        if len(Game_Instance.computer_hand) > 0: #If The Number Of "computer_hand" Is Greater Than 0, Continue
            if Game_Instance.Computer_Stack_Available_Control()==True: #If The Card Is Available In The "stack" List, The Function Returns "True"
                Game_Instance.turn=0 #The Turn Goes To Player
            elif Game_Instance.Computer_Stack_Operations()==True: #If The Card Is Suitable For The "stack" List, The Function Returns "True"
                Game_Instance.turn=0 #The Turn Goes To Player
            elif Game_Instance.tips>0: #If The Number Of Tips Is Greater Than 0, The "Computer_Tip_Operations" Will Run
                Game_Instance.Computer_Tip_Operations()
            else: #If The Number Of Tips Is 0 or Less, The "Computer_Trash_Operations" Will Run
                Game_Instance.Computer_Trash_Operations()
        else: #If The Number Of "computer_hand" Is 0 or Less, Continue
            if Game_Instance.tips>0: #If The Number Of Tips Is Greater Than 0, The "Computer_Tip_Operations" Will Run
                Game_Instance.Computer_Tip_Operations()
            else: #If The Number Of Tips Is 0 or Less, The Turn Goes To The Player
                Game_Instance.turn=0

    Game_Instance.trash.sort() #The "trash" Is Sorted After Each Hand
    Score = sum(len(element) for element in Game_Instance.stack) #Calculate The "Score" By Adding The Number Of Cards In The "self.stack"
    if Game_Instance.lives == 0: #Check Lives After Each Hand
        print("\nNo Lives Left! Game Over!")
        print(f"Your Score is : {Score}")
        break
    if len(Game_Instance.player_hand + Game_Instance.computer_hand) == 0: #Check The Number Of Cards In The "player_hand" and "computer_hand" After Each Hand
        print("\nNo Cards left! Game over!")
        print(f"Your Score is : {Score}")
        break
    if Score == 8: #If The "Score" Is 8, Print a Felicitation Message
        print("\nCongratulations! You Have Reached The Maximum Score!")
        break