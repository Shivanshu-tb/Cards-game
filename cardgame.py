import random
import tkinter as tk
from tkinter import messagebox

suits = ('hearts','diamonds','spades','clubs')
ranks = ('Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King')

class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        
    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit

    def __str__(self):
        return self.rank + " of " + self.suit
  
class Deck:
    def __init__(self):
        self.deck = []
        for rank in ranks:
            for suit in suits:
                card = Card(rank,suit)
                self.deck.append(card)
            
    def shuffle(self):
        random.shuffle(self.deck)
        
    def dealCard(self):
        return self.deck.pop(0)

def deal(n):
    deck = Deck()
    deck.shuffle()
    cards = []
    for i in range(n):
        card = deck.dealCard()
        cards.append(card)
    return cards

def evaluate(hand):
    handRank = [card.getRank() for card in hand]
    occurence = {}
    unqranks = set(handRank)
    for rank in unqranks:
        occurence[rank] = handRank.count(rank)
  
    points = 0
    for rank in occurence:
        if occurence[rank] == 4:
            points += 100
        elif occurence[rank] == 3:
            points += 10
        elif occurence[rank] == 2:
            points += 1

    return points

def main():
    totalScore = 0
    window = tk.Tk(className = "Cards")
    label = tk.Label(text="Enter the Number of cards:")
    entry = tk.Entry()
    label.pack()
    entry.pack()
    text = tk.StringVar()
    text.set("{} {}".format("Score= ", totalScore))
    scorelabel = tk.Label(textvariable=text)
    buttons = []
    
    def clear():
        for l in buttons:
            l.destroy()
            
    def handle_click(event):
        clear()
        totalScore = 0
        scorelabel.pack()
        
        n = entry.get()
        if not n.isdigit():
            messagebox.showerror("Error", "Not a number, Please try Again!")
            return
        
        n = int(n)
        if (n>52) or (n<0):
            messagebox.showerror("Error","Deck size out of bound!")
            return
        
        cards = deal(n)
        for card in cards:
            button = tk.Button(text = str(card),width = 15)
            button.pack(side=tk.BOTTOM)
            buttons.append(button)
            score = evaluate(cards)
            totalScore = score

        text.set("{} {}".format("Score= ", totalScore))

    button = tk.Button(text="Deal")
    button.bind("<Button-1>", handle_click)
    button.pack()
    window.mainloop()
  
main()