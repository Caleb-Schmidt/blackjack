import os
import random
class Program():
    def __init__(self):
        self.starting_money = 1000
        self.pot = 0
        self.deck = ["AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
        self.user_hand = []
        self.dealer_hand = []

    def game_results(self):
        user_count = 0
        dealer_count = 0
        for item in self.user_hand:
            if item[0].lower() == "j" or item[0].lower() == "q" or item[0].lower() == "k":
                user_count += 10
            elif item[0] == "9":
                user_count += 9
            elif item[0] == "8":
                user_count += 8
            elif item[0] == "7":
                user_count += 7
            elif item[0] == "6":
                user_count += 6
            elif item[0] == "5":
                user_count += 5
            elif item[0] == "4":
                user_count += 4
            elif item[0] == "3":
                user_count += 3
            elif item[0] == "2":
                user_count += 2
            if item[0] == "a":
                choice = input(f"Do yu want {item} to count for 1 or 11? : ")
                if choice == "11":
                    user_count += 11
                elif choice == "1":
                    user_count += 1
                else:
                    print("Invalid input")
        
        for item in self.dealer_hand:
            if item[0].lower() == "j" or item[0].lower() == "q" or item[0].lower() == "k":
                dealer_count += 10
            elif item[0] == "9":
                dealer_count += 9
            elif item[0] == "8":
                dealer_count += 8
            elif item[0] == "7":
                dealer_count += 7
            elif item[0] == "6":
                dealer_count += 6
            elif item[0] == "5":
                dealer_count += 5
            elif item[0] == "4":
                dealer_count += 4
            elif item[0] == "3":
                dealer_count += 3
            elif item[0] == "2":
                dealer_count += 2
            if item[0] == "a":
                choice = input(f"Do yu want {item} to count for 1 or 11? : ")
                if choice == "11":
                    dealer_count += 11
                elif choice == "1":
                    dealer_count += 1
                else:
                    print("Invalid input")

        if dealer_count > 21:
            print("Dealer had a bust!")
        
        if user_count > 21:
            print("Your hand was a bust!")

        if dealer_count <= 21 and dealer_count > user_count:
            print("Dealer has won!")
            self.pot = 0
        elif user_count <= 21 and user_count > dealer_count:
            print("You won!")
            self.starting_money += self.pot
            self.pot = 0
        elif dealer_count == user_count and dealer_count <= 21 and user_count <= 21:
            print("Push has been called!") 
            self.pot = 0
        elif dealer_count > 21 and user_count > 21:
            print("Both Players busted!")
            self.pot = 0

    def user_turn(self):
        while True:
            choice = input("What would you like to do? : Hit/Stay : ")
            if choice[0].lower() == "h":
                Program.user_hit()
            elif choice[0].lower() == "s":
                break
            else:
                print("Invalid Input")

    def user_bet(self):
        while True:
            bet = input(f"You currently have {self.starting_money}. What would you like to bet? : ")
            bet = int(bet)
            if bet >= 0:
                if bet > self.starting_money:
                    print("You don't have enough money to place that bet.")
                    continue
                else:
                    print(f"The pot is now at {self.pot + bet}")
                    print(f"You now have {self.starting_money - bet}.")
                    break
            elif bet < 0:
                if self.pot < 0:
                    print("You didn't bet that much money, so we can't give you back that amount.")
                elif self.pot >= 0:
                    self.pot -= bet
                    print(f"The pot is now at {self.pot - bet}")
                    self.starting_money += bet
                    print(f"You now have {self.starting_money + bet}.")
                    break
                else:
                    print("Invalid Input")
            else:
                print("Invalid Input")
        while True:
            end_of_betting = input("Anything else? : Raise/Lower/Deal : ")
            if end_of_betting[0].lower() == "r":
                adding = input("What would you like to add? : (add amount)/Back : ")
                if adding[0].lower() == "b":
                    continue
                elif int(adding) >= 0:
                    if bet > self.starting_money:
                        print("You don't have enough money to place that bet.")
                        continue
                    self.pot += bet
                    print(f"The pot is now at {self.pot + bet}")
                    self.starting_money -= bet
                    print(f"You now have {self.starting_money - bet}.")
                    continue
            if end_of_betting[0].lower == "l":
                if self.pot < 0:
                    print("You didn't bet that much money, so we can't give you back that amount.")
                    continue
                elif self.pot >= 0:
                    self.pot -= bet
                    print(f"The pot is now at {self.pot - bet}")
                    self.starting_money += bet
                    print(f"You now have {self.starting_money + bet}.")
            else:
                break

    def user_hit(self):
        self.user_hand.append(self.deck[random.randint(0,len(self.deck) - 1)])
        print("Your Hand : ")
        for item in range(len(self.user_hand)):
            print(self.user_hand[item])
        

    def shuffle_deck(self):
        pass

    def deal_starting_hand(self):
        for i in range(2):
            self.user_hand.append(self.deck[random.randint(0,len(self.deck) - 1)])
            self.dealer_hand.append(self.deck[random.randint(0,len(self.deck) - 1)])
        self.pot *= 2
        print(f"Dealer's Hand : * {self.dealer_hand[-1]}")
        print("\n")
        print(f"Pot : {self.pot}")
        print("\n")
        print("Your Hand : ")
        for item in range(len(self.user_hand)):
            print(self.user_hand[item])

    def dealer_turn(self):
        choice = random.randint(1,2)
        if choice == 2:
            self.dealer_hand.append(self.deck[random.randint(0,len(self.deck) - 1)])
        print("Dealer's Hand : ")
        for item in range(len(self.dealer_hand)):
            print(self.dealer_hand[item])

    def user_choice(self):
        pass

    
program = Program()
def main():
        # start game / quit game
        while True:
            start = input("Welcome to BlackJack! : Start/Leave : ")
            if start[0].lower() == "s":
                program.user_bet()
                program.deal_starting_hand()
                program.user_turn()
                program.dealer_turn()
                program.game_results()
                choice = input("Would you like to play again or cash out? : P/C : ")
                if choice[0].lower() == "p":
                    continue
                elif choice[0].lower() == "c":
                    print(f"You earned {program.starting_money}. Have a nice day!")
                    break
                else:
                    print("Invalid Input")
            elif start[0].lower() == "l":
                print("Have a good day!")
                break
            else:
                print("Invalid Input. Try Again.")

            # user can place any bet that doesn't exceed current money
            # once user has placed bet, hand will be dealt
        # deal hands
            # user and dealer get two cards from deck
            # if user has 10 or face, and ace, blackjack is called
        # user's turn:
            # hit
                # user can take another card
                # is user goes over 21, dealer wins
            # stay
                # user can keep current cards and pass turn
            # double down
        # dealer's turn:
            # show hand
            # hit
                # dealer will hit based on differing chance
            # stay
                # dealer will stay based on differing chance
        # results
            # if user has higher card count than dealer, user wins
            # if user has lower card count than dealer, dealer wins
            # if user has the same card count as dealer, push is called
        # empty pot
            # if user won, money goes to user
            # if dealer won, pot goes back to 0
            # if push, user gets back what he bet
        # deck check
            # if deck count is low enough, put dealt cards back in deck
        # next round / cash out
            # option to play another round or cash out and exit the game
            # if next round. start next round
            # if cash out, displayed what user won and exit game

main()