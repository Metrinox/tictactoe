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
	print(f'It is Player {player}\'s turn! ')
	'''Input = int( input('Choose a box:')) #check if input is valid (WORK ON THIS)
	if Input >= 0 and Input <= 8 and mem[Input] == '_':
		return Input'''
	return int(input('Choose a box:'))
	
#def update(turn, choice):	

mem = init()
render()
while isWon == False:
	mem[turn(1)] = 'X'
	render()
	#
	mem[turn(2)] = 'O'
	render()

