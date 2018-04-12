import datetime

class User():
   def __init__(self, name, age):
       self.name = name
       self.age = age
       self.dateJoined = datetime.datetime.now()
       self.wins = 0
       self.losses = 0
   def __repr__(self):
       return("Name:\t%s" % (self.name))
       return("age:\t%d" % (self.age))
       return("Date Joined:\t%d" % (self.dateJoined))
       return("Wins: %d Losses: %d" % (self.wins,self.losses))
   def increment_wins(self):
       self.wins += 1
   def increment_losses(self):
       self.losses += 1
