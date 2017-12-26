'''
Erika Fortune
Purpose: To convert currency
'''
def getCurrency1():
    currency1=input("Enter your current currency(US, EU, or CD): ")
    while(currency1!="US" and currency1!="EU" and currency1!="CD"):
        currency1=input("Enter your current currency: ")
    return(currency1)
def getCurrency2(currency1):
    currency2=input("Enter the currency you would like to convert to: ")
    while(currency2!="US" and currency2!="EU" and currency2!="CD" and currency1!=currency2):
        currency2=input("Enter your currency you would like to convert to: ")
    return(currency2)
def getAmount():
    amount=float(input("Enter the amount you would like to convert?"))
    while(amount<=0):
        amount=float(input("Enter the amount you would like to convert?"))
    return(amount)
def getPayment():
    payment=input("How will you be paying? (cash or check?)")
    while(payment!="cash" and payment!="Cash" and payment!="CASH" and payment!="check" and payment!="Check" and payment!="CHECK"):
        payment=input("How will you be paying? (cash or check?)")
    return(payment)
def main():
    again="y"
    while(again=="y"):
        currency1=getCurrency1()
        currency2=getCurrency2(currency1)
        amount=getAmount()
        payment=getPayment()
        if(currency1=="US" and amount>0):
            if (currency2=="CD" and amount>0 and (payment=="cash"or"Cash"or"CASH")):
                fee=amount*.01
                total=amount*1.29
                total=total+fee
                num="US to CD"
                num1="the amount you started with: "
                num2="1 US=1.29CD"
                num3="your new amount: "
                num4="you converted from "
                num5="Fee= "
                print(num4+num)
                print(num2)
                print(num1+(str(amount)))
                print(num3+str(total))
                print(num5+str(fee))
            elif (currency2=="CD" and amount>0 and (payment=="check"or"Check"or"CHECK")):
                fee=amount*.05
                total=amount*1.29
                total=total+fee
                num="US to CD"
                num1="the amount you started with: "
                num2="1 US=1.29CD"
                num3="your new amount: "
                num4="you converted from "
                num5="Fee= "
                print(num4+num)
                print(num2)
                print(num1+(str(amount)))
                print(num3+str(total))
                print(num5+str(fee))
            elif (currency2=="EU" and amount>0 and (payment=="cash"or"Cash"or"CASH")):
                fee=amount*.01
                total=amount*.88
                total=total+fee
                num="US to EU"
                num1="the amount you started with: "
                num2="1 US=.88 EU"
                num3="your new amount: "
                num4="you converted from "
                num5="Fee= "
                print(num4+num)
                print(num2)
                print(num1+(str(amount)))
                print(num3+str(total))
                print(num5+str(fee))
            elif ((currency2=="EU") and (amount>0) and (payment=="check"or"Check"or"CHECK")):
                fee=amount*.05
                total=amount*.88
                total=total+fee
                num="US to EU"
                num1="the amount you started with: "
                num2="1 US= .88 EU"
                num3="your new amount: "
                num4="you converted from "
                num5="Fee= "
                print(num4+num)
                print(num2)
                print(num1+(str(amount)))
                print(num3+str(total))
                print(num5+str(fee))
        elif(currency1=="CD"and amount>0):
            if((currency2=="EU") and (amount>0) and (payment=="cash"or"Cash"or"CASH")):
                fee=amount*.01
                total=amount*.69
                total=total+fee
                num="CD to EU"
                num1="the amount you started with: "
                num2="1 CD=.69 EU"
                num3="your new amount: "
                num4="you converted from "
                num5="Fee= "
                print(num4+num)
                print(num2)
                print(num1+(str(amount)))
                print(num3+str(total))
                print(num5+str(fee))
            elif ((currency2=="EU") and (amount>0) and (payment=="check"or"Check"or"CHECK")):
                fee=amount*.05
                total=amount*.69
                total=total+fee
                num="CD to EU"
                num1="the amount you started with: "
                num2="1 CD= .69 EU"
                num3="your new amount: "
                num4="you converted from "
                num5="Fee= "
                print(num4+num)
                print(num2)
                print(num1+(str(amount)))
                print(num3+str(total))
                print(num5+str(fee))
            elif ((currency2=="US") and (amount>0) and (payment=="cash"or"Cash"or"CASH")):
                fee=amount*.01
                total=amount*.78
                total=total+fee
                num="CD to US"
                num1="the amount you started with: "
                num2="1 CD=.78 US"
                num3="your new amount: "
                num4="you converted from "
                num5="Fee= "
                print(num4+num)
                print(num2)
                print(num1+(str(amount)))
                print(num3+str(total))
                print(num5+str(fee))
            elif ((currency2=="US") and (amount>0) and (payment=="check"or"Check"or"CHECK")):
                fee=amount*.05
                total=amount*.78
                total=total+fee
                num="CD to US"
                num1="the amount you started with: "
                num2="1 CD= .78 US"
                num3="your new amount: "
                num4="you converted from "
                num5="Fee= "
                print(num4+num)
                print(num2)
                print(num1+(str(amount)))
                print(num3+str(total))
                print(num5+str(fee))
        elif(currency1=="EU"and amount>0):
            if ((currency2=="US") and (amount>0) and (payment=="cash"or"Cash"or"CASH")):
                fee=amount*.01
                total=amount*1.13
                total=total+fee
                num="EU to US"
                num1="the amount you started with: "
                num2="1 EU= 1.13 US"
                num3="your new amount: "
                num4="you converted from "
                num5="Fee= "
                print(num4+num)
                print(num2)
                print(num1+(str(amount)))
                print(num3+str(total))
                print(num5+str(fee))
            elif ((currency2=="US") and (amount>0) and (payment=="check"or"Check"or"CHECK")):
                fee=amount*.05
                total=amount*1.13
                total=total+fee
                num="EU to US"
                num1="the amount you started with: "
                num2="1 EU= 1.13 US"
                num3="your new amount: "
                num4="you converted from "
                num5="Fee= "
                print(num4+num)
                print(num2)
                print(num1+(str(amount)))
                print(num3+str(total))
                print(num5+str(fee))
            elif ((currency2=="CD") and (amount>0) and (payment=="cash"or"Cash"or"CASH")):
                fee=amount*.01
                total=amount*1.46
                total=total+fee
                num="EU to CD"
                num1="the amount you started with: "
                num2="1 EU=.1.46 CD"
                num3="your new amount: "
                num4="you converted from "
                num5="Fee= "
                print(num4+num)
                print(num2)
                print(num1+(str(amount)))
                print(num3+str(total))
                print(num5+str(fee))
            elif ((currency2=="CD") and (amount>0) and (payment=="check"or"Check"or"CHECK")):
                fee=amount*.05
                total=amount*1.46
                total=total+fee
                num="EU to CD"
                num1="the amount you started with: "
                num2="1 EU= 1.46 CD"
                num3="your new amount: "
                num4="you converted from "
                num5="Fee= "
                print(num4+num)
                print(num2)
                print(num1+(str(amount)))
                print(num3+str(total))
                print(num5+str(fee))
        again=input("Would you like to perform another conversion?(y/quit)")
    
main()
