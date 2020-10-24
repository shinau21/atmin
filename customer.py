import pymysql
from atm_card import ATMCard

class Customer(ATMCard):
    def __init__(self, card=0, custPin=0, name='', jk='', desa='', kec='', kab='', tml='', tl='', umur='', ibu='', jenis='', nik='', kk='', BalanceIDR=0, BalanceUSD=0, BalanceKWD=0):
        super().__init__(card, custPin, BalanceIDR, BalanceUSD, BalanceKWD)

        db = pymysql.connect('localhost', 'root', '', 'atmin')
        cursor = db.cursor()
        sql = "SELECT * FROM nasabah WHERE rekening='%d'" % self.card
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            self.card = int(row[0])
            self.custPin = int(row[1])
            self.name = row[2]
            self.jk = row[3]
            self.desa = row[4]
            self.kec = row[5]
            self.kab = row[6]
            self.tml = row[7]
            self.tl = row[8]
            self.umur = row[9]
            self.ibu = row[10]
            self.jenis = row[11]
            self.nik = row[12]
            self.kk = row[13]
            self.BalanceIDR = int(row[14])
            self.BalanceUSD = float(row[15])
            self.BalanceKWD = float(row[16])

    def checkName(self):
        return self.name
    
    def checkGender(self):
        return self.jk

    def checkAlamat(self):
        return self.desa + ' ' + self.kec + ' ' + self.kab
    
    def checkUmur(self):
        return self.umur
    
    def checkJenis(self):
        return self.jenis

    def checkCard(self):
        return self.card
    
    def checkPin(self):
        return self.custPin

    def changePin(self, new):
        db = pymysql.connect('localhost', 'root', '', 'atmin')
        cursor = db.cursor()
        sql = "UPDATE nasabah SET pin='%d' WHERE rekening='%d'" % (new, self.card)
        cursor.execute(sql)
        db.commit()
    
    def checkIbu(self):
        return self.ibu

    def checkIDR(self):
        return self.BalanceIDR

    def checkUSD(self):
        return self.BalanceUSD

    def checkKWD(self):
        return self.BalanceKWD

    def witdrawIDR(self, nominal):
        self.BalanceIDR -= nominal
        db = pymysql.connect('localhost', 'root', '', 'atmin')
        cursor = db.cursor()
        sql = "UPDATE nasabah SET saldo_idr='%d' WHERE rekening='%d'" % (self.BalanceIDR, self.card)
        cursor.execute(sql)
        db.commit()

    def witdrawUSD(self, nominal):
        self.BalanceUSD -= nominal
        db = pymysql.connect('localhost', 'root', '', 'atmin')
        cursor = db.cursor()
        sql = "UPDATE nasabah SET saldo_usd='%d' WHERE rekening='%d'" % (self.BalanceUSD, self.card)
        cursor.execute(sql)
        db.commit()

    def witdrawKWD(self, nominal):
        self.BalanceKWD -= nominal
        db = pymysql.connect('localhost', 'root', '', 'atmin')
        cursor = db.cursor()
        sql = "UPDATE nasabah SET saldo_kwd='%d' WHERE rekening='%d'" % (self.BalanceKWD, self.card)
        cursor.execute(sql)
        db.commit()

    def depositIDR(self, nominal):
        self.BalanceIDR += nominal
        db = pymysql.connect('localhost', 'root', '', 'atmin')
        cursor = db.cursor()
        sql = "UPDATE nasabah SET saldo_kwd='%d' WHERE rekening='%d'" % (self.BalanceIDR, self.card)
        cursor.execute(sql)
        db.commit()

    def depositUSD(self, nominal):
        self.BalanceUSD += nominal
        db = pymysql.connect('localhost', 'root', '', 'atmin')
        cursor = db.cursor()
        sql = "UPDATE nasabah SET saldo_kwd='%d' WHERE rekening='%d'" % (self.BalanceUSD, self.card)
        cursor.execute(sql)
        db.commit()

    def depositKWD(self, nominal):
        self.BalanceKWD += nominal
        db = pymysql.connect('localhost', 'root', '', 'atmin')
        cursor = db.cursor()
        sql = "UPDATE nasabah SET saldo_kwd='%d' WHERE rekening='%d'" % (self.BalanceKWD, self.card)
        cursor.execute(sql)
        db.commit()