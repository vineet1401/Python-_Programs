
# Black Jack Game
import random


# Cards of different number depends on face value
# King Queen Jack has value 10
# Ace value is 11 but it differ in sum
def Card_Deck():
    '''Take a random Card from the card deck and return that card'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    x = random.choice(cards)
    return x

# Adding 2 Card is User list and making it global


def Give_User_Card():
    '''Add 2 card in the User card list'''
    global user_card
    user_card = [Card_Deck() for i in range(2)]

# Adding 2 card to computer list and making it global


def Give_Comp_Card():
    '''Add 2 card in the Computer card list'''
    global comp_card
    comp_card = [Card_Deck() for i in range(2)]

# Taking sum of user card list of 2 card and making sum global


def User_Card_Sum(card_list):
    '''User card sum if user dont want to take extra card'''
    global user_sum
    user_sum = sum(card_list)

# Taking sum of computer card list of 2 card and making sum global


def Comp_Card_Sum(card_list):
    '''Computer card sum if computer dont want to take extra card'''
    global comp_sum
    comp_sum = sum(card_list)

# what is user want extra card if he/she is not satiesfied with thier sum
# Defining function for that using global card list of user and sum of card list


def User_Card_Extra_Sum():
    '''User Card sum if user want to take extra card'''
    '''Also this Function adjust the value of sum if extra card is ACE'''
    global user_card
    global user_sum

    # calling function to choose one card from deck
    extra_card = Card_Deck()
    # if the new card is ACE some rules are changed of summing
    if (extra_card == 11):
        user_card.append(11)
        user_sum = sum(user_card)
        # if user sum is exceeding 20 after adding ACE then Consider ACE as 1
        if (user_sum > 20):
            user_card.remove(11)
            user_card.append(1)
            user_sum = sum(user_card)
    # If the user draw random card then just add the card to user sum
    else:
        user_card.append(extra_card)
        user_sum = sum(user_card)

# what is Computer want extra card if comp has less sum means less than 16
# Defining function for that using global card list of comp and sum of card list


def Comp_Card_Extra_Sum():
    '''Computer Card sum if Computer want to take extra card'''
    '''Also this Function adjust the value of sum if extra card is ACE'''
    global comp_card
    global comp_sum

    # calling function to choose one card from deck
    extra_card = Card_Deck()
    # if the new card is ACE some rules are changed of summing
    if (11 == extra_card):
        comp_card.append(11)
        comp_sum = sum(comp_card)
        # if computer sum is exceeding 20 after adding ACE then Consider ACE as 1
        if (comp_sum > 20):
            comp_card.remove(11)
            comp_card.append(1)
            comp_sum = sum(comp_card)
    # If the computer draw random card then just add the card to computer sum
    else:
        comp_card.append(extra_card)
        comp_sum = sum(user_card)


# Take a loop if the user want to retry
cond = True
while (cond):
    # Taken a loop to continue the game until we find a winner
    while (True):
        # Calling function at the first stage for sum and card list of user and computer
        Give_Comp_Card()
        Give_User_Card()
        User_Card_Sum(user_card)
        Comp_Card_Sum(comp_card)

    # Displaying User card
        print("<-------------| Your Cards |--------------->")
        print(f"| | \t\t {user_card} \t\t | |")
        print("<------------------------------------------>")

        print()

    # Now its user chance to do what he wants.....
        print("<-------------------User------------------------------>")
    # if user want to add extra card or not
        choice = input("Do you want extra card? (y / n): ")
        # If user want extra card then calling extra card function  and display extra card and sum
        if (choice.lower() == "y"):
            User_Card_Extra_Sum()
            print("<-------------| Your Cards |--------------->")
            print(f"||              {user_card}              ||")
            print("<------------------------------------------>")
            print(f"Your sum of your card after new card is {user_sum}")
            # if the sum exceed 20 then user loose
            if (user_sum > 20):
                print("<----------RESULT---------->")
                print("Busted! You loose the round")
                print("Computer wins!")
                break
    # else Display the sum and User chance ends
        else:
            print(f"Your sum of your card is {user_sum}")
        print("-*"*10 + " User Chance Ends " + "-*"*10)

        print()

        print("<-------------------Computer------------------------------>")
    # if computer sum is less than 16 then computer need extra card
        if (comp_sum < 16):
            # If computer want extra card then calling function and display extra card and sum
            Comp_Card_Extra_Sum()
            print("<-------------| Computer Cards |--------------->")
            print(f"||              {comp_card}              ||")
            print("<------------------------------------------>")
            print(f"Sum of computer card is {comp_sum}")
            # if the sum exceed 20 then Computer loose
            if (comp_sum > 20):
                print("<----------RESULT---------->")
                print("Busted! You loose the round")
                print("User wins!")
                break
    # else Display the sum and Computer chance ends
        else:
            print("<-------------| Computer Cards |--------------->")
            print(f"||              {comp_card}              ||")
            print("<------------------------------------------>")
            print(f"Sum of computer card is {comp_sum}")
        print("-*"*10 + " Computer Chance Ends " + "-*"*10)

        print()

    #  if none of the above happen ....compare he sum and declare winner
        print("<----------RESULT---------->")
        if (user_sum > comp_sum):
            print("User won the round!")
            print("Computer Losse.")
            break
        elif (user_sum == comp_sum):
            print("DRAW...")
        else:
            print("Computer won the round")
            print("User loose.")
            break
    print("<---------------------------------------------------------------------->")
    # get choice of user if he wants to retry or not
    retry = input("Restart or End the game? (R , E): ")
    if (retry.lower() == "r"):
        cond = True
    else:
        cond = False
    print()
    print()
    print("<----------------------------------------------------------------------------->")
