#grocery billing system
items = ["milk","bread","egg"] 
prices = [40,25,5]
bill = 0
l=[]
ql=[]
print("Items that are available: ")
for i,t in enumerate(items,start=1):
    print(i,t)
while True:
    
    it=input("Enter the item : ")
    if it == "done":
        print("Thank you here's the bill \n")
        break
    if it in items:
        
        q = int(input(f"Enter the quantity of {it} : "))
        ind = items.index(it)
        cost = prices[ind]*q
        bill += cost
        l.append(it)
        ql.append(q)

    else:
        print("Item is not available...")


cur_bill=bill

if bill > 500:
    dis =10
    bill = bill*(1-dis/100)
elif bill > 1000:
    dis=20
    bill = bill*(1-dis/100)
print(f"Billing details: \n")
print(f"Cart items:\n")
for i in range(len(l)):
    print(f"{l[i]} X {ql[i]}")

print(f"\nCurrent bill: {cur_bill}\n")
print(f"Discounted bill: {bill}")
