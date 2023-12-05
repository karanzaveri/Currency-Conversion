#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Defining exchange rates
exchange_rates = {
    'USD': 1.0,
    'EUR': 0.88,  
    'GBP': 0.78,
    'JPY': 112.25,
    'CAD': 1.31,
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency in exchange_rates and to_currency in exchange_rates:
        conversion_rate = exchange_rates[to_currency] / exchange_rates[from_currency]
        converted_amount = amount * conversion_rate
        return converted_amount
    else:
        return None  # Invalid currencies provided

if __name__ == "__main__":
    from_currency = input("Enter the source currency: (USD, EUR, GBP, JPY, CAD) ").upper()
    to_currency = input("Enter the target currency: (USD, EUR, GBP, JPY, CAD) ").upper()
    
    if from_currency == to_currency:
        print("ERROR! Both currencies are same, cannot convert!")

    elif from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("Invalid currency codes. Make sure they are in the exchange_rates dictionary.")
    else:
        amount = float(input("Enter the amount: "))
        converted_amount = convert_currency(amount, from_currency, to_currency)

        if converted_amount is not None:
            print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
        else:
            print("Invalid currency codes. Make sure they are in the exchange_rates dictionary.")


# In[ ]:




