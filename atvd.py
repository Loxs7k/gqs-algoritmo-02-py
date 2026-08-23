class CurrencyConverter:
    iof = 1.06
    dolla = 3.10
 
    def calc(quantity):
        return (quantity * CurrencyConverter.dolla) * CurrencyConverter.iof
 
 
def main():
    print(f"What is the dollar price? {CurrencyConverter.dolla:.2f}")
    print("How many dollars will be bought? ")
    quantity = float(input())
 
    amount = CurrencyConverter.calc(quantity)
    print(f"Amount to be paid in reais = {amount:.2f}")
 
 
if __name__ == "__main__":
    main()