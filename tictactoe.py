#variables
mem = ['_', '_', '_', '_', '_', '_', '_', '_', '_'] #stores the values of the boxes
isWon = False

#functions
def init(): #resets mem
	print('Welcome to Tic-Tac-Toe!')
	return ['_', '_', '_', '_', '_', '_', '_', '_', '_']
def render(): #displays the board
	print(f'{mem[0]} | {mem[1]} | {mem[2]}			0 | 1 | 2')
	print(f'{mem[3]} | {mem[4]} | {mem[5]}			3 | 4 | 5')
	print(f'{mem[6]} | {mem[7]} | {mem[8]}			6 | 7 | 8')
def turn(player):
	Valid = False
	print(f'It is Player {player}\'s turn! ')
	play = input('Choose a box:')
	while Valid == False:
		if len(str(play)) != 1 or str(play) not in '012345678' or play == '':
			play = int(input('Out of Bounds! Try again:'))
			continue
		if mem[int(play)] != '_':
			play = int(input('Box already taken! Try again:'))
			continue
		else:
			Valid = True
	return int(play)
def checkWin():
	for i in range(3): 
		if mem[i] != '_' and mem[i] == mem[i+3] and mem[i+3] == mem[i+6]: #vertical 
			if mem[i] == 'X':
				return 1
			else:
				return 2
		if mem[3*i] != '_' and mem[3*i] == mem[3*i+1] and mem[3*i+1] == mem[3*i+2]: #horziontal
			if mem[3*i] == 'X':
				return 1
			else:
				return 2
		return 0

#def update(turn, choice):	

mem = init()
render()
while isWon == 0:
	mem[turn(1)] = 'X'
	render()
	isWon = checkWin()
	if isWon != 0:
		break
	mem[turn(2)] = 'O'
	render()
	isWon = checkWin()
	if isWon != 0:
		break
print(f"Player {isWon} has won the game!")