def canWinNim(n):
  return n % 4 != 0

canWinNim(4) # False, the number is already a multiple of 4
canWinNim(1) # True, you can remove 1 stone to win
canWinNim(2) # True, you can remove 1 stone to leave 1
canWinNim(3) # True, you can remove 1 stone to leave 2  
