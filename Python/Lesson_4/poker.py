import random
import re

class Deck_of_cards:
	def __init__(self):
		self.allcards = {'Ace of Spades': 14, 'Ace of Hearts': 14, 'Ace of Diamonds': 14, 'Ace of Clubs': 14,
					'Two of Spades': 2, 'Two of Hearts': 2, 'Two of Diamonds': 2, 'Two of Clubs': 2,
					'Three of Spades': 3, 'Three of Hearts': 3, 'Three of Diamonds': 3, 'Three of Clubs': 3,
					'Four of Spades': 4, 'Four of Hearts': 4, 'Four of Diamonds': 4, 'Four of Clubs': 4,
					'Five of Spades': 5, 'Five of Hearts': 5, 'Five of Diamonds': 5, 'Five of Clubs': 5,
					'Six of Spades': 6, 'Six of Hearts': 6, 'Six of Diamonds': 6, 'Six of Clubs': 6,
					'Seven of Spades': 7, 'Seven of Hearts': 7, 'Seven of Diamonds': 7, 'Seven of Clubs': 7,
					'Eight of Spades': 8, 'Eight of Hearts': 8, 'Eight of Diamonds': 8, 'Eight of Clubs': 8,
					'Nine of Spades': 9, 'Nine of Hearts': 9, 'Nine of Diamonds': 9, 'Nine of Clubs': 9,
					'Ten of Spades': 10, 'Ten of Hearts': 10, 'Ten of Diamonds': 10, 'Ten of Clubs': 10,
					'Jack of Spades': 11, 'Jack of Hearts': 11, 'Jack of Diamonds': 11, 'Jack of Clubs': 11,
					'Queen of Spades': 12, 'Queen of Hearts': 12, 'Queen of Diamonds': 12, 'Queen of Clubs': 12,
					'King of Spades': 13, 'King of Hearts': 13, 'King of Diamonds': 13, 'King of Clubs': 13}

class Game:
	def __init__(self):
		self.pot = 0
		self.blind_small = 10
		self.blind_big = 20
		self.status = 'game is started'
		self.table_cards = {}
		self.deck = Deck_of_cards()
	def __call__(self):
		if self.status == 'game is started':
			Game.begin(self)
		elif self.status == 'after begin' or self.status == 'after flop' or self.status == 'after preflop' or self.status == 'after tern' or self.status == 'after river':
			print('You should bet or fold')
		elif self.status == 'after begin, bets are doned':
			Game.preflop(self)
		elif self.status == 'after preflop, bets are doned':
			Game.flop(self)
		elif self.status == 'after flop, bets are doned':
			Game.tern(self)
		elif self.status == 'after tern, bets are doned':
			Game.river(self)
		elif self.status == 'after river, bets are doned':
			Game.finish(self)
		elif self.status == 'after river, bets are doned':
			Game.finish(self)

	def table_movement_forward(self):
		global last_index
		if (player_count - 1) > last_index:
			last_index += 1
		else:
			self.player_index = 0
	def table_movement_backward(self):
		global last_index
		if 0 < last_index:
			last_index -= 1
		else:
			last_index = (player_count - 1)

	def begin(self):
		player_list.append(user)
		player_list[last_index].points -= self.blind_small
		Game.table_movement_forward(self)
		player_list[last_index].points -= self.blind_big
		Game.table_movement_backward(self)
		self.pot = self.blind_big + self.blind_small
		print('Allright, blinds are doned.')
		max_cards_hand = 2
		for i in player_list:    #clearing cards from last game
			i.cards.clear()
		for i in range(max_cards_hand):			#giving new cards
			for a in range(player_count):		
				card = random.choice(list(self.deck.allcards))
				value = self.deck.allcards[card]
				player_list[a].cards[card] = value
				del self.deck.allcards[card]
		player_list.pop(-1)
		Bot.bots_choice(self)
		print('Now show your cards and print what do you want to do: ')
		self.status = 'after begin'

	def preflop(self):   
		cards_for_table = 3
		for i in range(cards_for_table): #Razda4a kart
			card = random.choice(list(self.deck.allcards))
			value = self.deck.allcards[card]
			self.table_cards[card] = value
			del self.deck.allcards[card]
		print('The cards on the table are:')
		print(self.table_cards.keys())
		Bot.bots_choice(self)
		print('Now bet or fold')
		self.status = 'after preflop'

	def flop(self):
		cards_for_flop = 1
		for i in range(cards_for_flop):#Razda4a kart
			card = random.choice(list(self.deck.allcards))
			value = self.deck.allcards[card]
			self.table_cards[card] = value
			del self.deck.allcards[card]
		print(self.table_cards.keys())
		Bot.bots_choice(self)
		print('Show the cards on the table and say what you think: ')
		self.status = 'after flop'

	def tern(self):
		cards_for_tern = 1
		for i in range(cards_for_tern):#Razda4a kart
			card = random.choice(list(self.deck.allcards))
			value = self.deck.allcards[card]
			self.table_cards[card] = value
			del self.deck.allcards[card]
		print('The cards on the table are:')
		print(self.table_cards.keys())
		Bot.bots_choice(self)	
		print('What do you want to do now: ')
		self.status = 'after tern'
		
	def river(self):
		Bot.bots_choice(self)	
		print('Now you can bet last time')	
		self.status = 'after river'

	def finish(self):          
		max_val = [0]  #who wons?
		for i in player_list:
			if len(i.cards) > 0:
				value_list = list(i.cards.values())
				result_val = value_list[0] + value_list[1]
				if result_val > max_val[0]:
					max_val[0] = result_val
					max_val.append(i)
		print(max_val[1].name, 'wons')
		max_val[1].points += game.pot 
		global last_index 
		Game.table_movement_forward   #The next game begin with the next player
		User.fold(self)  #starts a new round
		print('Now You can start a new round')

class Player:
	def __init__(self):
		self.name = ""
		self.points = 1000  #All player have 1000 points when the game begin
		self.cards = {}
		
class User(Player):
	def __init__(self):
		Player.__init__(self)
	def bet(self):
		if game.status == 'after begin' or game.status == 'after flop' or game.status == 'after preflop' or game.status == 'after tern' or game.status == 'after river':
			game.status = game.status + ', bets are doned'
			game.pot += 10
			self.points -= 10
			game()
		else: 
			print('You can\'t bet now. Run a new round first')
	def fold(self):
		global game
		game = Game()
	def show(self):
		print(user.cards.keys())
	def round(self):
		if game.status == 'game is started':
			game()
		else:
			print('You should finish current game first')
	def help(self):
		print(Commands.keys())
	def state(self):
		print("You have {} points".format(self.points))
	def pot(self):
		print(game.pot)

	def quit(self):
		print("Potra4eno")
		self.points = 0
	def users_command(self):
		while user.points > 0:
			user_says = input('>')
			command_found = False
			for i in Commands.keys():
				if user_says == i:
					Commands[i](user)
					command_found = True
					break
			if not command_found:
				print("Enter a right command please")


class Bot(Player):
	def __init__(self, user):
		Player.__init__(self)
		if user.name != bot_names[0]: 				#User and the other player must have difference names.
			self.name = bot_names.pop(0)
		else: 
			self.name = bot_names.pop(1)
	def bots_choice(self):		#has a bot cards?
		for i in (player_list):
			if len(i.cards) > 0:
				i.choice()
			
	def choice(self):
		if len(game.table_cards) == 0:
			result_value = 0
			for a in range(len(self.cards)):		#middle value of cards in hand
				result_value = result_value + list(self.cards.values())[a]
			result_value = result_value / len(self.cards)
			suit_checker = re.split('(\W+)', str(list(self.cards))) 
			if suit_checker[-3] == suit_checker[-9]: #is suits of cards the same? -3 and -9 is position of suits when its splitted
				result_value * 1.5
			if result_value > 8: #middle value of all cards is 8. If bot have a bigger one, he bets 
				self.bet()
			else:
				self.fold()
		else:
			self.bet()    #its to difficult to write another logic of choice  

	def bet(self):
		print('{} has betted'.format(self.name))
		game.pot += 10
		self.points -= 10

	def fold(self):
		print('{} has folded'.format(self.name))
		self.cards.clear()

Commands = {'help' : User.help, 'state': User.state, 'bet': User.bet, 'fold': User.fold,
			'quit': User.quit, 'show': User.show, 'round': User.round, 'pot': User.pot}  

bot_names = ['Alex', 'Igor', 'Max', 'Ray', 'Sergej', 'Markus']  	#System names of bots

user = User()													#create a new user(Person)
game = Game()													#new game
user.name = input("Enter your Player-Name please: ")
print("Thank you {}.".format(user.name))
last_index = 0 #this index is for player movement at the table. Show String 46

player_list = []						#List to make all operations with player
player_count = 6   							#only to enter into loop
while player_count >= 6 or player_count < 1:
	inp = input("Now enter please how many player you wish to have(max 5): ")
	if inp.isdigit():
		player_count = int(inp)
		if 0 < player_count <= 5:
			for i in range(player_count):
				bot = Bot(user)  #by creating a bot we must know users name, to select a different one for the bot
				player_list.append(bot)
			player_count = player_count + 1  #plus user
			break
		else: 
			print("The table has 6 places. You can have max. 5 other player. Enter right count of players")	
	else:
		print('This is not a digit. Enter a digit please')

player_names = []					#We must know the names of all the players to show them in the next sentence
for i in range (len(player_list)):
	player_names.append(player_list[i].name)   

print("Great. At the table are:", player_names)
print("Allright {}. To see all actions you can make type 'help'".format(user.name))
user.users_command()