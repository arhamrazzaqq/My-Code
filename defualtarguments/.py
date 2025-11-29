def net_price(price, tax=0.05, discount=0):
    return price * (1 - discount) * (1 + tax)

print(net_price(500, 1)) #the value after comma is the second 
                         #argument to add additional dicount/tax when there is 
                         #no discount/tax.
