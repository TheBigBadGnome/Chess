#Release Left Mouse Button
if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
	#If movingPiece, (turned on by if dragging statement)
	if movingPiece:
		pos = pygame.mouse.get_pos()
		#Loop through gameboard to check if released on a square
		for newIndex in range(len(board)):
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
