import random
MAXL = 3
MAXB=100
MINB=1
ROWS=3
COLS=3
symbol_counts={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}
def check(columns,lines,bet,values):
    winnings=0
    winnings_lines=[]

    for line in range (lines):
        symbol=columns[0][lines]
        for column in columns:
            symbol_to_check=column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings+=values[symbol] * bet
                winnings_lines.append(lines+1)

    return winnings,winnings_lines

def getslotspin(rows,cols,symbols):
    allsymbols=[]
    for symbol,symbolcounts in symbols.items():
        for _ in range(symbolcounts) :
            allsymbols.append(symbol)
    columns=[]
    for _ in range(cols):
        column=[]
        currentsymbols=allsymbols[:]
        for _ in range(rows):
            value=random.choice(currentsymbols)
            currentsymbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
def print_slot_machine(columns):
    for row in range(len(columns[0])) :

        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
        print()






def deposite():
    while True:

        amount = input("please enter amount of deposite?")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("please enter amount greater than zero ")
        else:
            print("enter a  valid digit ")

    return amount


def getnumberoflines():
    while True:

        lines = input("please enter number of linesTO BET ON (1-"+str(MAXL)+" )?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAXL:
                break
            else:
                print("please enter a valid number of lines ")
        else:
            print("enter a  valid digit ")

    return lines
def get_bet():
    while True:

        amount = input("what would you like to bet on each line?")
        if amount.isdigit():
            amount = int(amount)
            if MINB<= amount <=MAXB:
                break
            else:
                print(f"AMOUNT MUST BE BETWEEN{MAXB} - {MINB} ")
        else:
            print("enter a  valid digit ")

    return amount
def game(balance):
    lines = getnumberoflines()
    while True:

        bet = get_bet()
        totalbet = lines * bet
        if totalbet > balance:
            print("you do not have sufficent balance to bet that amount your current balance is ${balance} ")
        else:
            break
    print(f"you are betting {bet}$ on {lines} the total bet is {totalbet}")
    slot = getslotspin(ROWS, COLS, symbol_counts)
    print_slot_machine(slot)
    winnings, winnings_lines = check(slot, lines, bet, symbol_value)
    print(f"you won ${winnings}")
    print(f"you won on lines: ", *winnings_lines)
    return winnings-totalbet


def main():
    balance = deposite()
    while True:
        print(f"current balance is {balance}")
        spin=input("press enter to spin (q to quit)")
        if spin== "q":
            break
        balance+=game(balance)
    print("you left with ${balance}")



main()
