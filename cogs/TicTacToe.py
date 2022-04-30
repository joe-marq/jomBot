import discord
from discord.ext import commands

class TicTacToe(commands.Cog):
  def __init__(self, client):
    self.client = client

  global player1, player2, board, game_over, cp, piece
  game_over = True

  async def print_board(self, ctx, board):
    line = ""
    for x in range(len(board)):
      if x == 2 or x == 5 or x == 8:
          line += " " + board[x]
          await ctx.send(line)
          line = ""
      else:
        line += " " + board[x]

  def check_for_win(self, board, current_player):
    global game_over
    if (board[0] == board[1] and board[1] == board[2] and board[2] != ":white_large_square:"
      or board[3] == board[4] and board[4] == board[5] and board[5] != ":white_large_square:"
      or board[6] == board[7] and board[7] == board[8] and board[8] != ":white_large_square:"
      or board[0] == board[3] and board[3] == board[6] and board[6] != ":white_large_square:"
      or board[1] == board[4] and board[4] == board[7] and board[7] != ":white_large_square:"
      or board[2] == board[5] and board[5] == board[8] and board[8] != ":white_large_square:"
      or board[0] == board[4] and board[4] == board[8] and board[8] != ":white_large_square:"
      or board[2] == board[4] and board[4] == board[6] and board[6] != ":white_large_square:"):
      game_over = True
      return True
    else:
      return False

  @commands.command(aliases=["ttt"])
  async def tictactoe(self, ctx, p1: discord.Member, p2: discord.Member):
    global player1, player2, board, game_over, cp, piece
    
    if game_over:
      board = [":white_large_square:", ":white_large_square:", ":white_large_square:", ":white_large_square:", ":white_large_square:", ":white_large_square:", ":white_large_square:", ":white_large_square:", ":white_large_square:"]   
      player1 = p1
      player2 = p2
      cp = p1
      piece = ":o2:"
      game_over = False
      await self.print_board(ctx, board)
    else:
      await ctx.send("THERE IS A GAME IN PROGRESS. YOU MAY NOT START A NEW ONE.")    

  @commands.command()
  async def place(self, ctx, pos: int):
    global player1, player2, board, game_over, cp, piece
    #check if there is a game
    if not game_over:
      #check if it is the author's turn
      if cp == ctx.author:
        #check if the turn is valid
        if 1 <= pos <= 9 and board[pos-1] == ":white_large_square:":
          #place piece in board
          board[pos-1] = piece
          #print board
          await self.print_board(ctx, board)
          #check if cp is the winner
          if self.check_for_win(board, cp):
            await ctx.send("<@" + str(cp.id) + "> YOU WIN!")
          #check if game is a tie
          elif ":white_large_square:" not in board:
            game_over = True
            await ctx.send("THE GAME IS A TIE. NOBODY WINS.")
          #switch players
          if cp == player1:
            cp = player2
            piece = ":regional_indicator_x:"
          else:
            cp = player1
            piece = ":o2:"
        else:
          await ctx.send("THAT IS AN INVALID MOVE. TRY AGAIN.")
      elif player1 != ctx.author and player2 != ctx.author:
        await ctx.send("YOU ARE NOT PART OF THIS GAME. GO AWAY.")
      else:
        await ctx.send("IT IS NOT YOUR MOVE.")
    else:
      await ctx.send("THERE IS NO GAME IN PROGRESS. START A GAME WITH THE *tictactoe COMMAND.")

def setup(client):
  client.add_cog(TicTacToe(client))