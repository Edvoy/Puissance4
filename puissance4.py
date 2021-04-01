import scipy as sp

class Board:

  def empty():
    global board
    global end_game
    end_game=0
    board=sp.zeros([7,7],str)
    board[0:6,0:7] = "_"
    board[6,0:7] = "█"
    return board
  
  def display():
    global board
    print(board)

  def place(token_color, y):
    global board
    count = 0
    while board[count,y] == "_" :
      count += 1
    else :
      board[count-1, y] = token_color

class Player:
  global end_game
  def play():
    token_color = str(input("Joueur ☺ tapez A // Joueur ☻ tapez B : "))
    if token_color == "A":
      token_color = "☺"
    elif token_color == "B":
      token_color = "☻"
    else:
      print("Joueur invalid")
    y = int(input("Dans quelle colonne veux tu jouer ?"))
    return token_color, y 
  
  def win():
    global board
    global end_game
    token_color = ["☻","☺"]
    
    for token in token_color:
      #vertical win
      for x in range(6,-1,-1):
        for y in range(5,2,-1):
          if board[x,y]==token and board[x,y-1]==token and board[x,y-2]==token and board[x,y-3]==token:
            print(f'le joueur {token} gagne')
            end_game = 1
            return end_game
          else:
            end_game = 0
      
      #horizontal win
      for x in range(6,2,-1):
        for y in range(5,-1,-1):
          if board[x,y]==token and board[x-1,y]==token and board[x-2,y]==token and board[x-3,y]==token:
            print(f'le joueur {token} gagne')
            end_game = 1
            return end_game
          else:
            end_game = 0
      
      #diagonal 1 win
      for x in range(4):
        for y in range(5,2,-1):
          if board[x,y]==token and board[x-1,y+1]==token and board[x-2,y+2]==token and board[x-3,y+3]==token:
            print(f'le joueur {token} gagne')
            end_game = 1
            return end_game
          else:
            end_game = 0
      
      #diagonal 2 win
      for x in range(5,2,-1):
        for y in range(4,0,-1):
          if board[x,y]==token and board[x-1,y+1]==token and board[x-2,y+2]==token and board[x-3,y+3]==token:
            print(f'le joueur {token} gagne')
            end_game = 1
            return end_game
          else:
            end_game = 0

Board.empty()
Board.display()
while end_game != 1:
  token, token_color = Player.play()
  Board.place(token, token_color)
  Board.display()
  Player.win()