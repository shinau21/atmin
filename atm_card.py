class ATMCard:
    def __init__(self, card, custPin, BalanceIDR, BalanceUSD, BalanceKWD):
        self.card = card
        self.custPin = custPin
        self.BalanceIDR = BalanceIDR
        self.BalanceUSD = BalanceUSD
        self.BalanceKWD = BalanceKWD

    def pin(self):
        return self.custPin
    
    def balanceidr(self):
        return self.BalanceIDR
    
    def balanceusd(self):
        return self.BalanceUSD
    
    def balancekwd(self):
        return self.BalanceKWD