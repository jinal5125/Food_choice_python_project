menu="""
    Menu

vadapav     Rs.40
dabeli      Rs.30
bhel        Rs.60
sandwich    Rs.120

"""
cart={}     #main dictinary
total=0

print(menu)
status=True
while status:
    sub_dic={}
    p_name=input("enter product name:").upper()
    qty=int(input("enter quntity:"))
    
    if p_name == "VADAPAV":
        price=40
    elif p_name == "DABELI":
        price=30
    elif p_name == "BHEL":
        price=60
    elif p_name == "SANDWICH":
        price=120
    
    total=qty*price
    print(f"item name:{p_name} Qty:{qty} = total price:{total}")

    if p_name in cart.keys():
        sub_dic["qty"]=cart [p_name]["qty"]+qty
        sub_dic["price"]=price

        cart[p_name]=sub_dic
    else:
        sub_dic["qty"]=qty
        sub_dic["price"]=price

        cart[p_name]=sub_dic

    print(cart)
    sum=0
    choice=input("do you want to continue?")
    if choice == 'n' or choice == "no":
        status=False

        for k in cart.keys():
            print(f"{k} qty. {cart[k]["qty"]} price : Rs.{cart[k]["qty"] * cart[k]["price"]}")
            sum += cart[k]["qty"] * cart[k]["price"]

            print("------------------------------")
            print("NET AMOUNT ",sum)
