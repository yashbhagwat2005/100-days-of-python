import random
bet = 1000
deck = {
    "Ace of clubs": 11, "2 of clubs": 2, "3 of clubs": 3, "4 of clubs": 4,
    "5 of clubs": 5, "6 of clubs": 6, "7 of clubs": 7, "8 of clubs": 8,
    "9 of clubs": 9, "10 of clubs": 10, "Jack of clubs": 10, "Queen of clubs": 10,
    "King of clubs": 10, "Ace of diamonds": 11, "2 of diamonds": 2, "3 of diamonds": 3,
    "4 of diamonds": 4, "5 of diamonds": 5, "6 of diamonds": 6, "7 of diamonds": 7,
    "8 of diamonds": 8, "9 of diamonds": 9, "10 of diamonds": 10, "Jack of diamonds": 10,
    "Queen of diamonds": 10, "King of diamonds": 10, "Ace of hearts": 1, "2 of hearts": 2,
    "3 of hearts": 3, "4 of hearts": 4, "5 of hearts": 5, "6 of hearts": 6, "7 of hearts": 7,
    "8 of hearts": 8, "9 of hearts": 9, "10 of hearts": 10, "Jack of hearts": 10,
    "Queen of hearts": 10, "King of hearts": 10, "Ace of spades": 1, "2 of spades": 2,
    "3 of spades": 3, "4 of spades": 4, "5 of spades": 5, "6 of spades": 6, "7 of spades": 7,
    "8 of spades": 8, "9 of spades": 9, "10 of spades": 10, "Jack of spades": 10,
    "Queen of spades": 10, "King of spades": 10
}


#random card
def random_card_deal(cards):
    random_card = random.choice(list(deck.keys()))
    cards[random_card] =deck[random_card]


    

def total_score(cards):
    '''To calculate the total score of the cards dealt. Only 1 argument is taken'''
    score = 0
    ace_count =0
    for key in cards.keys():
        score+=cards[key]
        if "Ace" in key:
            ace_count+=1
    while score>21 and ace_count:
        score-=10
        ace_count-=1
    return score
    
while True:
    player_1_cards = {}
    dealer_cards = {}
    #Rules and bet
    print('''Welcome to the game of Black Jack!
          
          ''')
    print('''You will be given 1000 tokens to start of the game and place 
          some bets
          
          
          ''')
    print ('''Enter the number of bets you want to place remember each 
              time you win you will get the double amout of tokens that 
              you placed on and if you loose all the tokens that you 
              put on the bet will be taken away
           
           
           
               ''')
    while True:
        bet = float(input('''Enter the bet: '''))
        if bet>1000:
            print("Please enter an amount less than or equal to 1000")
        if bet<=1000:
            break
        
    #Cards dealt to both the player and the dealer
    random_card_deal(player_1_cards)
    random_card_deal(player_1_cards)
    print("Your cards are: ")
    for key in player_1_cards.keys():
        print(key)
    print(f'''Your points are {total_score(player_1_cards)}
                                     
           ''')

    
    random_card_deal(dealer_cards)
    random_card_deal(dealer_cards)
    print("The dealer's cards")
    print(list(dealer_cards.items())[0][0])
    print("The second card of the dealer is faced down")

    if total_score(player_1_cards)==21:
        print("BUST!")
        print("Congratulations you have won")
        break

    #the player has to choose to Stand or Hit
    ch = input('''If you want to hit enter h or if you want to stand enter s: ''')
    while ch in "hH" and total_score(player_1_cards)<21 : 
        random_card_deal(player_1_cards)
        print('''Your cards are: ''')
        for i in player_1_cards:
            print(i)
        print(f"Your points are {total_score(player_1_cards)}")
        print(list(dealer_cards.items())[0][0])
        print('''The second card of the dealer is faced down
              
                   ''')
        if total_score(player_1_cards)>=21:
            break
        ch = input('''If you want to hit enter h or if you want to stand enter s: ''')
        if ch in "sS": 
            break

    #if player1 busts or the score is more than 21
    if total_score(player_1_cards)==21:
        print("BUST!")
        print("Congratulations you have won")
        break

    


    #if the score of the dealer's card is less than 17
    dealer_total_score = total_score(dealer_cards)
    while dealer_total_score<17:
        random_card_deal(dealer_cards)
        dealer_total_score = total_score(dealer_cards)
    print("The dealer's cards are")
    for key in dealer_cards.keys():
        print(key)
    print(f"The total score of the dealer is{total_score(dealer_cards)}")
    #if player 1's score is more than 21 or dealer's score is more than 21 , and if both it is a tie

    if total_score(player_1_cards)>21 and dealer_total_score<21:
        ("Your score is more than 21 thus you lose ")

    elif total_score(player_1_cards)<21 and dealer_total_score>21:
        print("Player 1 wins")

    #has the player1 won or lost 
    elif total_score(player_1_cards)>dealer_total_score:
        print("You have won!")
        print("Now you have a total of",bet*2,"tokens.")
    elif total_score(player_1_cards)<dealer_total_score:
        print("You have lost!")
        print("Now you have a total of",bet*0.5,"tokens.")
    elif total_score(player_1_cards)==dealer_total_score:
        print("It's a tie")




    print("That was an intresting game ")
    play_again = input('''If you want to continue to play the game enter y or if you want to exit the game enter n: ''')
    if play_again in 'nN':
        break
    
    
    
    
    
        
        
        
        





        
        
        

        
    


    
    

    
    
        
    




