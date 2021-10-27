bitcoin_amount = 1 #cuanto tengo en bitcoin
bitcoin_value_euros = 25000 #el valor de bitcoin en euros

def bitcoinToEuros(bitcoin_amount, bitcoin_value_euros):
    euros_value = bitcoin_amount * bitcoin_value_euros
    return euros_value

euros_value = bitcoinToEuros(bitcoin_amount, bitcoin_value_euros)

if euros_value <= 30000:
    print("Investment below 30.000€! SELL!")
else:
    print("Investment above 30.000€")
