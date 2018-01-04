board = [ ['-' for _ in xrange(3)] for _ in xrange(3) ]

def showBoard():
	for row in board:
		print "\n"
		for col in row:
			print "\t" + col, 
	print "\n\n"
	
def changeBoardCell(coordinate,s):
	board[coordinate[0]-1][coordinate[1]-1] = s

def getBoardCell(coordinate):
	return board[coordinate[0]-1][coordinate[1]-1]
	
def checkBoard():
	c = [ 
			[(1,3),(2,2),(3,1)], # Cross - 1
			[(1,1),(2,2),(3,3)], # Cross - 2
			[(1,1),(2,1),(3,1)], # Vertical - 1
			[(1,2),(2,2),(3,2)], # Vertical - 2
			[(1,3),(2,3),(3,3)], # Vertical - 3
			[(1,1),(1,2),(1,3)], # Horizontal - 1
			[(2,1),(2,2),(2,3)], # Horizontal - 2
			[(3,1),(3,2),(3,3)], # Horizontal - 3
		]
	for comb in c:
		combinations = []
		for coordinate in comb:
			combinations.append(getBoardCell(coordinate))
		if combinations[1:] == combinations[:-1] and combinations[0] != "-":
			return True, combinations[0]
	return False, []
	
if __name__ == "__main__":
	print "Welcome to TicTacToe!\n"
	
	showBoard()
	
	for i in xrange(18):
		r,c = input("Enter the Row: "), input("Enter the Column: ")
		s = 'X' if i % 2 == 0 else 'O'
		changeBoardCell((r,c),s)
		showBoard()
		status, sign = checkBoard()
		if status:
			print "Game Over!"
			print "Player with", sign, "wins!" 
			break