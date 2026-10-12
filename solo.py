#Mini project about vegetable shop


#inventary
veg = ['brinjal','tomato','onion','potato','greenonions','carrot','beetroot']
quantity = [15,20,10,10,5,5,5]
cost_price = [40,15,10,10,5,20,25]
price = [65,20,18,15,10,25,30]
sales_profit = [0,0,0,0,0,0,0]
sales_qty = [0,0,0,0,0,0,0]
item_profit = [0,0,0,0,0,0,0]
for i in range(len(veg)):
    item_profit[i] = price[i] - cost_price[i]
#Customer Management
while True:
    cart_items = []
    cart_qty = []
    cart_amt = []
    while True:
        item = input('What do you want: ')
        if item == 'done':
            print('='*30)
            for it in zip(cart_items,cart_qty,cart_amt):
                print(f'{it[0]: <17}{it[1]: <10}{it[2]: <5}')
            print('='*30)
            print('total',' '*19,sum(cart_amt))
            break
        if item in veg:
            qty = float(input('How much do you want: '))
            idx = veg.index(item)
            if qty <= quantity[idx]:
                amt = qty*price[idx]
                cart_items.append(item)
                cart_qty.append(qty)
                cart_amt.append(amt)
                quantity[idx] = quantity[idx] - qty
                cost = qty*cost_price[idx]
                profit = amt-cost
                sales_profit[idx] += profit
                sales_qty[idx] += qty
                print(item,'is added to cart')
            else:
                print(item,'is out of stock')

        else:
            print(item ,'is not available')
    ch = input("Do you want to close the shop(yes/no): ")
    if ch == 'yes':
        print('='*50)
        print('Veg Report')
        print('='*50)
        for i in zip(veg,quantity):
            print(f'{i[0]: <15}{i[1]: <10}')
        print('='*110)
        print('Itemized profit')
        print('='*110)
        print('vegitables',' '*6,'costprice/kg',' '*6,'Sellingprice/kg',' '*6,'profit/kg',' '*7,'Profit/day',' '*6,'sales/Day(kg)')
        for j in zip(veg,cost_price,price,item_profit,sales_profit,sales_qty):
            print(f'{j[0]: <25}{j[1]: <17}{j[2]: <20}{j[3]: <18}{j[4]: <15}{j[5]: <10}')
        print('='*110)
        break
            






























 
    
