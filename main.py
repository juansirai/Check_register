import pandas as pd

# starter cash, as 2d array
cid = [['PENNY', 'NICKEL', 'DIME', 'QUARTER',  'ONE', 'FIVE', 'TEN', 'TWENTY', 'ONE HUNDRED'],
       [0,           0,         0,    0,         0,     0,     0,        0,         0]
       ]


def initialize_cid(c):
    print('Initializing cash machine, please enter the number of each coins that you have: ')
    for i in range(len(c[0])):
        c[1][i] = int(input(f"{c[0][i]}: "))
    print('Congrats! CID initialized ;)')


def check_cash_register(price, cash, c) -> dict:
    # Function which accepts the purchase price as the first argument (price),
    # the amount paid as the second argument (cash), and the cash in the
    # box (cid) as the third argument.
    result = {
        # initial status of the return of our function
        'status': 'INSUFFICIENT_FUNDS',
        'change': []
    }

    # equivalences of coins, as 2d array
    equivalences = [['PENNY', 'NICKEL', 'DIME', 'QUARTER', 'ONE', 'FIVE', 'TEN', 'TWENTY', 'ONE HUNDRED'],
                    [0.01,     0.05,      0.1,     0.25,      1,     5,    10,      20,        100]
                    ]

    # change that we need to give, as 2d array
    change = [['PENNY', 'NICKEL', 'DIME', 'QUARTER',  'ONE', 'FIVE', 'TEN', 'TWENTY', 'ONE HUNDRED'],
              [0,      0,         0,      0,         0,     0,       0,     0,       0]]

    def total_cash(c, eq):
        # function which returns the total cash of our machine.
        # receives cid and coin equivalences as params.
        total = 0
        for i in range(len(c[0])):
            total = total + c[1][i] * eq[1][i]
        return total

    to_give_back = cash - price
    total_effective = total_cash(c, equivalences)  # how much effective we have

    if total_effective >= to_give_back:  # checks if we have enough money to give back
        move = True
        # index 'i' in -1 to start slicing the array from tail to head, since we  want to finish with
        # larger coins first.
        i = -1
        while move:
            if c[1][i] > 0:  # checks if we have coins in that position of the cid array.
                coin = equivalences[1][i]  # in cash how much we are giving
                if coin <= to_give_back:  # checks if what we are trying to give is according to the amount to give back
                    to_give_back = to_give_back - coin  # update the amount to give back
                    c[1][i] -= 1  # updates the cid array, to show the coins that I have.
                    change[1][i] += 1  # updates the array of change that I will give.
                else:
                    i -= 1  # if the coin is greater than the amount to give back, It needs to try with a lower coin.
            else:
                i -= 1 # if it doesn't have coins in this position of the array, It needs to try with a lower coin.
            if to_give_back == 0:  # Checks if it could give back all the amount.
                # creates a list to display the result from higher to lower coins.
                final_list = [f"{change[1][-i-1]}  {change[0][-i-1]}" for i in range(len(change[0]))]
                if total_cash(c, equivalences) == 0:
                    # checks if the cash on the machine was equal to the change that must be delivered.
                    result['status'] = 'Closed'
                    result['change'] = final_list
                else:
                    # if not is because it stills have money in the machine.
                    result['status'] = 'Open'
                    result['change'] = final_list
                move = False  # stops the bucle
            elif abs(i) == len(c[0]):
                # checks if it sliced for all the array. In that case is because it couldn't give the exact change.
                move = False
    # If I didn't enter the controls, is because the machine didn't have enough money to give back. So the result
    # will be 'INSUFFICIENT_FUNDS', the initial status.
    return result


'''
--------------------------------------------------------------
                HERE STARTS THE MAIN PROGRAM
-------------------------------------------------------------
'''


initialize_cid(cid)

go = True

while go:
    user_decision = input('Welcome to the cash machine, do you want to start? (y/n): ').upper()
    if user_decision == 'F':
        go = False
    else:
        price = float(input('Please enter the price of your product: '))
        cash = float(input('How much are you going to pay? '))
        result = check_cash_register(price, cash, cid)
        print(result)
        if result['status'] != 'Open':
            go = False

