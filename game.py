import random

MAX_NUMBER_OF_LINES = 3
MIN_AMOUNT = 1
MAX_AMOUNT = 1000

ROWS = 3
COLS = 3

SYMBOLS_NUM = {
    "A": 1, 
    "B": 2, 
    "C": 4, 
    "D": 8
    }

SYMBOLS_VAL = {
    "A": 10, 
    "B": 5, 
    "C": 3, 
    "D": 1
    }


def check_win(columns, lines, betted, values):
  winnings = 0
  winning_lines = []
  if random.randint(1, 100) == 1:
    print("JACKPOT! You win $1000!")
    winnings += 1000
  
  
  for line in range(lines):
    symbol = columns[0][line]
    for column in columns:
      symbol_check = column[line]
      if symbol != symbol_check:
        break
    else:
      winnings+= values[symbol] * betted
      winning_lines.append(line+1)

  
  return winnings, winning_lines


def get_spin(rows, cols, symbols):
  all_symbols = []
  for symbol, symbol_count in symbols.items():
    for _ in range(symbol_count):
      all_symbols.append(symbol)

  columns = []
  for _ in range(cols):
    column = []
    current_symbols = all_symbols[:]
    for _ in range(rows):
      value = random.choice(current_symbols)
      current_symbols.remove(value)
      column.append(value)

    columns.append(column)
  
  return columns


def print_slot_machine(columns):
  for row in range(len(columns[0])):
    for i, column in enumerate(columns):
      if i!= len(columns)-1:
        print(column[row],  end =" | ")
      else:
        print(column[row], end="")
    print("\n")

def deposit():
    while True:
        amount = input("What would you like to deposit?")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
          print("Please enter a number.")
    
    return amount

def get_line_number():
    while True:
        line_num = input("How many number of lines do you want to bet on? (1-" + str(MAX_NUMBER_OF_LINES) + ")")
        if line_num.isdigit():
            line_num = int(line_num)
            if 1 <= line_num <= MAX_NUMBER_OF_LINES:
                break
            else:
                print("Please enter a valid number of lines ( in the range [1 to" + str(MAX_NUMBER_OF_LINES) + "])")
        else:
          print("Please enter the number of lines.")
    
    return line_num

def get_bet():
    while True:
        bet = input("What would you like to bet on each line?")
        if bet.isdigit():
            bet = int(bet)
            if MIN_AMOUNT <= bet <= MAX_AMOUNT:
                break
            else:
                print(f"Amount must be in the range ${MIN_AMOUNT} and ${MAX_AMOUNT}.")
        else:
          print("Please enter a number.")
    
    return bet
    
    

def ui(balance):
    lines = get_line_number()

    while True:
      betted = get_bet()
      total_betted = betted * lines
      if total_betted > balance:
        print(f"Dont have enough balance to bet ${betted} on {lines} lines.")
      else:
        break
    
    print(f"You have chosen to bet ${betted} on {lines}. Total bet is equal to: ${total_betted}")
    
    slot = get_spin(ROWS, COLS, SYMBOLS_NUM)
    print_slot_machine(slot)
    winnings, winning_lines = check_win(slot, lines, betted, SYMBOLS_VAL)
    print(f"You won ${winnings}")
    print(f"You won on lines:", *winning_lines)

    return winnings - total_betted

def main():
  balance = deposit()
  while True:
    print(f"Current balance is ${balance}")
    spin = input("Press enter to play (q to exit).")
    if spin == "q":
      break
    balance += ui(balance)

  print(f"You exited with ${balance}.")


  main()