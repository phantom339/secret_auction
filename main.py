#importing modules 
from art import logo
import os
#displaying the logo:
print(logo)
#asking the user what kind of auction is it ? maximum bidding or contract bidding 
Auction_type=int(input("What kind of Auction is it:\n  1-Contract Bidding\n  2-Purchase Bidding \n"))
#creating an empty dictionary:
winner=""
Bidders={}
should_continue=True
#creating a loop:
while should_continue:
    #asking for the inputs :
    key=input("What is the name of the Bidder? ")
    value=int(input("What is your Bid : $"))
    Bidders[key]=value
    more_bidder=input("Are there any other biddr : Y/N : ").lower()
    if more_bidder=="n":
        should_continue=False
    #clear scr to be used :
    os.system("clear")
if Auction_type==1:
    winner=min(Bidders)
    print(f"The Contract goes to the lowest bidder {winner} with a bid of ${Bidders[winner]} ")
else:
    winner=max(Bidders)
    print(f"The winner of this Auction is {winner} with a bid of ${Bidders[winner]}")


