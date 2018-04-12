import datetime

class User():
   def __init__(self, name, age):
       self.name = name
       self.age = age
       self.dateJoined = datetime.datetime.now()
       self.wins = 0
       self.losses = 0
   def __repr__(self):
       print("Name:\t{}".format(self.name))
       print("age:\t{}".format(self.age))
       print("Date Joined:\t{}".format(self.dateJoined))
       print("Wins: {} Losses: {}".format(self.wins,self.losses))
   def increment_wins(self):
       self.wins += 1
   def increment_losses(self):
       self.losses += 1
