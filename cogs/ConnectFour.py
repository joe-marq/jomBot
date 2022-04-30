import discord
from discord.ext import commands

class ConnectFour(commands.Cog):
  def __init__(self, client):
    self.client = client

  
  global player1, player2, board, game_over, cp, piece, col_nos
  col_nos = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:"]
  game_over = True

  async def print_board(self, ctx, board):
    for i in reversed(range(6)):
      row = board[i]
      s = ""
      for cell in row:
        s = s + cell
      await ctx.send(s)

  def check_win_helper(self, board, player, row, col, d, num):
    if num == 4:
      return True
    piece = board[row][col]
    if not (player == 1 and piece == ":red_circle:") and not (player == 2 and piece == ":yellow_circle:"):
      return False
    if d == "up":
      return self.check_win_helper(board, player, row+1, col, d, num+1)
    elif d == "right":
      return self.check_win_helper(board, player, row, col+1, d, num+1)
    elif d == "ur":
      return self.check_win_helper(board, player, row+1, col+1, d, num+1)
    elif d == "dr":
      return self.check_win_helper(board, player, row-1, col+1, d, num+1)

  def check_for_win(self, board, cp):
    for i in range(6):
      for j in range(7):
        cell = board[i][j]
        if (cp == 1 and cell == ":red_circle:") or (cp == 2 and cell == ":yellow_circle:"):
          if i < 3 and j < 4 and self.check_win_helper(board, cp, i, j, "ur", 0):
              return True
          if i >=3 and j < 4 and self.check_win_helper(board, cp, i, j, "dr", 0):
              return True
          if i < 3 and self.check_win_helper(board, cp, i, j, "up", 0):
              return True
          if j < 4 and self.check_win_helper(board, cp, i, j, "right", 0):
              return True
    return False

  @commands.command(aliases=["connect4", "c4"])
  async def connectfour(self, ctx, p1: discord.Member, p2: discord.Member):
    global player1, player2, board, game_over, cp, piece, col_nos
    if game_over:
      board = [[":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:"], [":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:"], [":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:"], [":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:"], [":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:"], [":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:", ":black_circle:"]]   
      player1 = p1
      player2 = p2
      cp = p1
      piece = ":red_circle:"
      game_over = False
      s = ""
      for num in col_nos:
        s = s + num
      await ctx.send(s)
      await self.print_board(ctx, board)
    else:
      await ctx.send("THERE IS A GAME IN PROGRESS. YOU MAY NOT START A NEW ONE.")

  @commands.command(aliases=["pcf", "pc4"])
  async def playconnectfour(self, ctx, pos: int):
    return

def setup(client):
  client.add_cog(ConnectFour(client))