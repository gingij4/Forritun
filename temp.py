loan = int(input("Input the cost of the item in $:"))
minna1000 = float(0.015)
meira1000 = float(0.02)
month = 0
afborgun = 50.0
vextir = 0.0
eftir = 0.0
for i in range(1,60,1):
    while vextir >= 0:    
        if loan <= 1000:
            while eftir > 50:
                vextir = (loan * minna1000)
                afborgun = 50
                payment_interest = afborgun - vextir
                loan = loan - payment_interest
                eftir = loan
                month += i
            else:    
                vextir = (loan * minna1000)
                afborgun = eftir + vextir
                payment_interest = afborgun - vextir
                loan = loan - payment_interest
                eftir = loan
                month += i
    
        
            print("Month: ", month,"Payment: ", round(afborgun, 2),"Interest paid: ", round(vextir, 2), "Remaining debt: ", round(eftir, 2))
            
    