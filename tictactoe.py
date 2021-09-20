#variables
mem = ['_', '_', '_', '_', '_', '_', '_', '_', '_'] #stores the values of the boxes
isWon = False

#functions
def init(): #resets mem
	print('Welcome to Tic-Tac-Toe!')
	return ['_', '_', '_', '_', '_', '_', '_', '_', '_']
def render(): #displays the board
	print(f'{mem[0]} | {mem[1]} | {mem[2]}')
	print(f'{mem[3]} | {mem[4]} | {mem[5]}')
	print(f'{mem[6]} | {mem[7]} | {mem[8]}')
def turn(player):
	Valid = False
	print(f'It is Player {player}\'s turn! ')
	play = int(input('Choose a box:'))
	while Valid == False:
		if play < 0 and play >= 9:
			play = int(input('Out of Bounds! Try again:'))
			continue
		if mem[play] != '_':
			play = int(input('Box already taken! Try again:'))
			continue
		else:
			Valid = True
	return play
	
#def update(turn, choice):	

mem = init()
render()
while isWon == False:
	mem[turn(1)] = 'X'
	render()
	#
	mem[turn(2)] = 'O'
	render()

