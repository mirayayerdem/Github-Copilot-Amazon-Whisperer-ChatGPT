def decimal_to_binary(decimal):
    binary = bin(decimal)[2:] # remove the "0b" prefix added by the bin() function
    return "db" + binary + "db"
