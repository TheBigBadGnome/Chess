import pygame
import math

#Intialize pygame
pygame.init()
#Create screen
screen = pygame.display.set_mode((1000,640))
#Title and Icon
pygame.display.set_caption("Chess")
icon = pygame.image.load('images/chessIcon.ico')
pygame.display.set_icon(icon)

#Images
whitePawnImg = pygame.image.load('images/WhitePieces/Pawn.png')
whitePawnOffset = (whitePawnImg.get_width(),whitePawnImg.get_height())
whiteRookImg = pygame.image.load('images/WhitePieces/Rook.png')
whiteRookOffset = (whiteRookImg.get_width(),whiteRookImg.get_height())
whiteKnightImg = pygame.image.load('images/WhitePieces/Knight.png')
whiteKnightOffset = (whiteKnightImg.get_width(),whiteKnightImg.get_height())
whiteBishopImg = pygame.image.load('images/WhitePieces/Bishop.png')
whiteBishopOffset = (whiteBishopImg.get_width(),whiteBishopImg.get_height())
whiteQueenImg = pygame.image.load('images/WhitePieces/Queen.png')
whiteQueenOffset = (whiteQueenImg.get_width(),whiteQueenImg.get_height())
whiteKingImg = pygame.image.load('images/WhitePieces/King.png')
whiteKingOffset = (whiteKingImg.get_width(),whiteKingImg.get_height())
blackPawnImg = pygame.image.load('images/BlackPieces/Pawn.png')
blackPawnOffset = (blackPawnImg.get_width(),blackPawnImg.get_height())
blackRookImg = pygame.image.load('images/BlackPieces/Rook.png')
blackRookOffset = (blackRookImg.get_width(),blackRookImg.get_height())
blackKnightImg = pygame.image.load('images/BlackPieces/Knight.png')
blackKnightOffset = (blackKnightImg.get_width(),blackKnightImg.get_height())
blackBishopImg = pygame.image.load('images/BlackPieces/Bishop.png')
blackBishopOffset = (blackBishopImg.get_width(),blackBishopImg.get_height())
blackQueenImg = pygame.image.load('images/BlackPieces/Queen.png')
blackQueenOffset = (blackQueenImg.get_width(),blackQueenImg.get_height())
blackKingImg = pygame.image.load('images/BlackPieces/King.png')
blackKingOffset = (blackKingImg.get_width(),blackKingImg.get_height())

#Functions

#Draw piece using index location
def drawPiece(indexLocation):
	#Returns 0: Img Variable 1: Img Offset
	pieceInfo = getPieceInfo(indexLocation)
	#Moves img to current mouse pos, (Piece doesnt actually move until mouse let go in MouseButtonUp function)
	if dragging and currentIndex == indexLocation:
		pos = pygame.mouse.get_pos()
		X = pos[0] - int(pieceInfo[1][0]/2)
		Y = pos[1] - int(pieceInfo[1][1]/2)
	#If not dragging piece, draw in square
	else:	
		X = invisBoard[indexLocation][0] + ((80-pieceInfo[1][0])/2)
		Y = invisBoard[indexLocation][1] + 2.5
	#Draw
	screen.blit(pieceInfo[0],(X,Y))

#Returns Piece variables, (Img,Offset)
# 2 is piece 3 is color
def getPieceInfo(indexLocation):
	#Pawn
	if invisBoard[indexLocation][2] == "pawn":
		if invisBoard[indexLocation][3] == "White":
			return (whitePawnImg, whitePawnOffset)
		elif invisBoard[indexLocation][3] == "Black":
			return (blackPawnImg, blackPawnOffset)
	#Rook
	if invisBoard[indexLocation][2] == "rook":
		if invisBoard[indexLocation][3] == "White":
			return (whiteRookImg, whiteRookOffset)
		elif invisBoard[indexLocation][3] == "Black":
			return (blackRookImg, blackRookOffset)
	#Knight
	if invisBoard[indexLocation][2] == "knight":
		if invisBoard[indexLocation][3] == "White":
			return (whiteKnightImg, whiteKnightOffset)
		elif invisBoard[indexLocation][3] == "Black":
			return (blackKnightImg, blackKnightOffset)
	#Bishop
	if invisBoard[indexLocation][2] == "bishop":
		if invisBoard[indexLocation][3] == "White":
			return (whiteBishopImg, whiteBishopOffset)
		elif invisBoard[indexLocation][3] == "Black":
			return (blackBishopImg, blackBishopOffset)
	#Queen
	if invisBoard[indexLocation][2] == "queen":
		if invisBoard[indexLocation][3] == "White":
			return (whiteQueenImg, whiteQueenOffset)
		elif invisBoard[indexLocation][3] == "Black":
			return (blackQueenImg, blackQueenOffset)
	#King
	if invisBoard[indexLocation][2] == "king":
		if invisBoard[indexLocation][3] == "White":
			return (whiteKingImg, whiteKingOffset)
		elif invisBoard[indexLocation][3] == "Black":
			return (blackKingImg, blackKingOffset)

#Draws gameboard with alternating shades
def drawGameBoard():
	color = 0
	for square in board:
		color += 1
		if color % 9 == 0:
			color += 1
		if color % 2:
			c = (123, 75, 0)
		else:
			c = (89, 34, 0)
		pygame.draw.rect(screen,c,square)

#Main Game Loop (Window)
running = True
while running:
	#Global Variables
	inGame = True
	dragging = False
	movingPiece = False
	#Game Setup
	#Create and Draw Board
	board = []
	invisBoard = []
	rows, cols = (8, 8)
	for i in range(cols):
		for j in range(rows):
			board.append(pygame.Rect(i*80,j*80,80,80))
			#				    Col  Row PType Color
			invisBoard.append([i*80,j*80,None,None])
	#Add pieces to board
		#Pawns
	for i in range(8):
		if i < 2:
			#Rooks
			invisBoard[56*i+7][2:] = ["rook", "White"]
			invisBoard[56*i][2:] = ["rook", "Black"]
		#Knights
			invisBoard[40*i+15][2:] = ["knight", "White"]
			invisBoard[40*i+8][2:] = ["knight", "Black"]
		#Bishops
			invisBoard[24*i+23][2:] = ["bishop", "White"]
			invisBoard[24*i+16][2:] = ["bishop", "Black"]
		#Pawns
		invisBoard[8*i+6][2:] = ["pawn", "White"]
		invisBoard[8*i+1][2:] = ["pawn", "Black"]
	
	#Queens
	invisBoard[31][2:] = ["queen", "White"]
	invisBoard[24][2:] = ["queen", "Black"]
	#Kings
	invisBoard[39][2:] = ["king", "White"]
	invisBoard[32][2:] = ["king", "Black"]

	#Game Loop (Game)
	while inGame:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				inGame = False
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				dragging = True
			if event.type == pygame.KEYDOWN:#Restarts current loop, resetting game
				if event.key == pygame.K_r:
					inGame = False
			if event.type == pygame.MOUSEBUTTONUP and event.button == 1: #Release Left Mouse Button
				if movingPiece: #If movingPiece, (turned on by if dragging statement)
					pos = pygame.mouse.get_pos()
					for newIndex in range(len(board)): #Loop through gameboard to check if released on a square
						if board[newIndex].collidepoint(pos) and not newIndex == currentIndex:
							row = currentIndex % 8 
							col = math.floor(currentIndex/8)
							step = 1
							RowBlocked = False
							ColBlocked = False
							#Pawns, Only piece that color matters for direction that it can move
							if (invisBoard[currentIndex][2] == "pawn" and invisBoard[currentIndex][3] == "White" 
							and not invisBoard[newIndex][3] == invisBoard[currentIndex][3]):
									if (newIndex == currentIndex - 1 and invisBoard[newIndex][2] == None # Move 1 foward
									or (currentIndex-6) % 8 == 0 and newIndex == currentIndex - 2 and invisBoard[newIndex][2] == None #Move 2 if first move
									or newIndex == currentIndex + 7 and not invisBoard[newIndex][2] == None # Move Diagonal Right 
									or newIndex == currentIndex - 9 and not invisBoard[newIndex][2] == None): #Move Diagonal Left
										#Move to new Index
										invisBoard[newIndex][2:] = invisBoard[currentIndex][2:]
										invisBoard[currentIndex][2:] = [None,None]
							elif (invisBoard[currentIndex][2] == "pawn" and invisBoard[currentIndex][3] == "Black" 
							and not invisBoard[newIndex][3] ==invisBoard[currentIndex][3]):
									if ( newIndex == currentIndex + 1 and not invisBoard[newIndex][2]  # Move 1 foward
									or (currentIndex-1) % 8 == 0 and newIndex == currentIndex + 2 and not invisBoard[newIndex][2] #Move 2 if first move
									or newIndex == currentIndex + 9 and invisBoard[newIndex][2] # Move Diagonal Right 
									or newIndex == currentIndex - 7 and invisBoard[newIndex][2] ): #Move Diagonal Left
										#Move to new Index
										invisBoard[newIndex][2:] = invisBoard[currentIndex][2:]
										invisBoard[currentIndex][2:] = [None,None]
							#Rooks
							elif invisBoard[currentIndex][2] == "rook" and not invisBoard[newIndex][3] ==invisBoard[currentIndex][3]:
								if(newIndex - currentIndex) % 8 == 0: #Move Horizontally
									if currentIndex > newIndex:
										step = -8
									else:
										step = 8
									for betweenIndex in range(currentIndex+step, newIndex,step):
										if invisBoard[betweenIndex][2] is not None:
											RowBlocked = True
									if not RowBlocked and not invisBoard[newIndex][3] == invisBoard[currentIndex][3]:			
										invisBoard[newIndex][2:] = invisBoard[currentIndex][2:]
										invisBoard[currentIndex][2:] = [None,None]
								elif newIndex <= (currentIndex + 7 - row) and newIndex >= col*8: #Move Vertically
									#Checks for step direction
									if currentIndex > newIndex:
										step = -1
									for betweenIndex in range(currentIndex+step,newIndex,step): #Checking to see if a piece is in the way 
										if invisBoard[betweenIndex][2] is not None:
											ColBlocked = True
										if not ColBlocked and not invisBoard[newIndex][3] == invisBoard[currentIndex][3]:
											#Move piece
											invisBoard[newIndex][2:] = invisBoard[currentIndex][2:]
											invisBoard[currentIndex][2:] = [None,None]
				#Reset variables no matter what after mouse comes up							
				currentIndex = None			
				dragging = False
				movingPiece = False

		if dragging:
			#Release Left Mouse Button
			pos = pygame.mouse.get_pos()
			for i in range(len(board)):
				if board[i].collidepoint(pos) and invisBoard[i][2] and not movingPiece:
					movingPiece = True
					currentIndex = i
		else:
			currentIndex = None			
			movingPiece = False

				
		screen.fill((255,255,255))
		drawGameBoard()
		for index in range(len(board)):
			if invisBoard[index][2]:
				drawPiece(index)

		pygame.display.update()




	#Board Colors: L:(123, 75, 0) D:(89, 34, 0)
	#Chess board is 8x8, 80x80

	# **** = Can be optimized