# Cash Register
*An algorithm Challenge*

**checkRegister()** is a function that accepts the purchase price as the first argument (price), the amount paid as the second argument (cash), 
and the amount of cash in the box (cid) as the third argument, and returns the change to be delivered, if possible.


## Definitions

* **cid** is a 2D array that lists the available coins.
* **equivalences** is a 2D array which contains the equivalences of coins
* **change** is a 2D array with the change to give back

**Coin equivalences:** <br>
Penny : $0.01 (PENNY) <br>
Nickel : $0.05 (NICKEL) <br>
Dime : $0.1 (DIME) <br>
Quarter : $0.25 (QUARTER) <br>
Dollar : $1 (ONE) <br>
Five Dollars: $5 (FIVE) <br>
Ten Dollars: $10 (TEN) <br>
Twenty Dollars : $20 (TWENTY) <br>
One-hundred Dollars : $100 (ONE HUNDRED)

## Usage

```python
import pandas

initialize_cid(cid)  # to initialize the amount of money which has the cash machine

go = True  # sets a boolean variable to start operating with the function

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
```


## License
n/a
