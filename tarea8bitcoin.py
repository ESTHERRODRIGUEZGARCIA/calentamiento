bitcoin_amount = 1.2 #cuanto tengo en bitcoin
bitcoin_value_euros = 25000 #el valor de bitcoin en euros

def bitcoinToEuros(bitcoin_amount, bitcoin_value_euros):
    euros_value = bitcoin_amount * bitcoin_value_euros
    return euros_value

investment_in_euros = bitcoinToEuros(bitcoin_amount, bitcoin_value_euros)

if bitcoin_value_euros <= 30000:
    print("investment below 30.000€! SELL!")
else:
    print("Investment above 30.000€")