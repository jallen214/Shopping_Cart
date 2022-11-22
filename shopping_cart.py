from IPython.display import clear_output

# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

cart = {}

def addToCart(ka, va):
    if ka in cart.keys():
        cart[ka] += va
    else:
        cart[ka] = va
        
def removeFromCart(kr, vr):
    if kr not in cart.keys():
        print(f'{kr} does not appeaer to be in the cart currently.')
    else:
        cart[kr] -= vr
        if kr in cart and cart[kr] <=0:
            del cart[kr]

def groceries():
    applicationRunning = True
    while applicationRunning:
        action = input('\nwhat would you like to do? (Add Item/Remove Item/View cart) ').lower()
        
        if action == 'view' or action == 'cart' or action == 'view cart':
            print(f'Here is youtncart:\n {cart}')
            
        elif action == 'add' or action == 'add item' or action == 'add to cart':
            itemAdd == input('What item would  you like to add to cart? ').lower()
            quantAdd == int(input('How many/how much would you like to add to cart? '))
            addToCart(itemAdd, quantAdd)
            
        elif action == 'remove' or action == 'remove item' or aciton == 'remove from cart':
            itemRem = input('What item you like to remove from cart? ').lower()
            quantRem = int(input('How many/how much would you like to remove from cart? '))
            removeFromCart(itemRem, quantRem)
            
        else:
            print(f'"{action}" is not a valid option, please try again.')
            
        while True:
            quit = input('would you lik to keep going? (Y/N ').lower()
            
            if quit == 'n' or quit == 'no' or quit == 'nah' or quit == 'na' or quit == 'nay' or quit == 'negative':
                print(f'\nYou are ready for check-out. here is your final cart:\n {cart}')
                applicationRunning = Flase
                break
            elif quit == 'y' or quit == 'yes' or quit == 'yeah' or quit == 'yea' or quit == 'yah' or quit == 'ye' or quit =='ya':
                break
            
            else:
                print(f'"{quit}" is not a vaild option, please try again.')
                
    groceries()