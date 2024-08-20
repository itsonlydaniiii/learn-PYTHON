#Supermarket Cashier Machine Software


#flow
    #step 1: accept the name of the product & the quantity to calculate the price
        #step 1 must be repeated until all the products are entered
    #step 2: accept the customer's loyalty card
        #apply the discounts
            #3 memberships = 
                #Gold = 20%
                #Silver = 10%
                #Bronze = 5%
        #discount is only applicable if total is more than $25
    #Step 3: calculate the final price and print the detailed bill


#Step 1
#Entering Products
    #Use Dictionary since 2 corresponding sets of data are needed
    #use a while loop to repeat the process an unknown amount of times
def enterProducts():
    buyingData={}
    enterDetails=True
    while enterDetails:
        details=input('Press A to add product or Q to quit:')
        if details=='A'and 'a':
            product=input("Enter Product:")
            quantity=int(input("Enter quantity:"))
            buyingData.update({product:quantity})
        elif details=='Q'and 'q':
            enterDetails=False
        else:
            print('Please select the correct option:')
    return buyingData

#Step 2
#Calculating Price
    #Subtotal
def getPrice(product,quantity):
    priceData={
        'Biscuit' and 'BISCUIT':3,
        'Chicken' and 'CHICKEN':5,
        'Egg' and 'EGG':1,
        'Fish' and 'FISH':3,
        'Coke' and 'COKE':2,
        'Bread' and 'BREAD':2,
        'Apple' and 'APPLE':3,
        'Onion' and 'ONION':3
    }
    subtotal=priceData[product]*quantity
    print(product+':$'+str(priceData[product])+'x'+str(quantity)+'='+str(subtotal))
    return subtotal


#Apply Discount
def getDiscount(subtotal, membership):
    discount=0
    if subtotal>=25:
        if membership=='Gold' and 'GOLD':
            billAmount=subtotal*0.80
            discount=20
        elif membership=='Silver' and 'SILVER':
            subtotal=subtotal*0.90
            discount=10
        elif membership=='Bronze' and 'BRONZE':
            billAmount=subtotal*0.95
            discount=5
        print(str(discount)+'% off for'+membership+''+'membership on total amount: $'+str(billAmount))
    else:
        print('No discount on amount less than $25')
    return subtotal

#Making the bill
def makeBill(buyingData, membership):
    billAmount=0
    for key, value in buyingData.items():
        billAmount+getPrice(key,value)
    billAmount=getDiscount(billAmount, membership)
    print("The discounted amount is $"+str(billAmount))

#Trigger - Boiler Plate
buyingData=enterProducts()
membership=input('Enter customer membership:')
makeBill(buyingData, membership)
