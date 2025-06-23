from tabulate import tabulate

class PacCommerce:
    def __init__ (self, monthly_expense, monthly_income):
        self.monthly_expense = monthly_expense
        self.monthly_income = monthly_income
        self.tier_benefits = [
                {"Membership": "Platinum", "Discount": "15%", "Another Benefits": "Benefit Silver + Voucher Liburan + Cashback max. 30%"},
                {"Membership": "Gold", "Discount": "10%", "Another Benefits": "Benefit Silver + Voucher Ojek Online"},
                {"Membership": "Silver", "Discount": "8%", "Another Benefits": "Voucher Makanan"}
        ]

        self.tier_req = [
            {"Membership": "Platinum", "Monthly Expense": 8_000_000, "Monthly Income": 15_000_000},
            {"Membership": "Gold", "Monthly Expense": 6_000_000, "Monthly Income": 10_000_000},
            {"Membership": "Silver", "Monthly Expense": 5_000_000, "Monthly Income": 7_000_000}
        ]
    
    def show_benefit (self):
        return tabulate(self.tier_benefits, headers="keys", tablefmt="grid")


    def show_requirements (self):
        return tabulate(self.tier_req, headers="keys", tablefmt="grid")


    def predict_membership (self):
        r_square_list = []
        for mytier in self.tier_req:
            r_square_suku_1 = (self.monthly_expense - mytier["Monthly Expense"])**2
            r_square_suku_2 = (self.monthly_income - mytier["Monthly Income"])**2
            r_square = (r_square_suku_1 + r_square_suku_2)**(1/2)
            r_square_list.append(r_square)
        
        acuan_nilai_terdekat = min(r_square_list)
        index_r_square_terkecil = r_square_list.index(acuan_nilai_terdekat)
        self.tier_user = self.tier_benefits[index_r_square_terkecil]["Membership"]
        return f"\nanda tergolong kategori membership {self.tier_user}"
    
    def calculate_price (self, list_harga_barang, membership):
        self.total = sum(list_harga_barang)

        if membership.capitalize() == self.tier_benefits[0]["Membership"]:
            harga_setelah_diskon = self.total - (self.total*0.15)
            cashback = harga_setelah_diskon*0.3
            harga_final = harga_setelah_diskon - cashback
            return f"anda mendapatkan benefit sebagai member {membership} dengan benefit {self.tier_benefits[0]["Another Benefits"]}, sehingga anda hanya perlu membayar {harga_final} dengan menghemat {cashback}."
        
        elif membership.capitalize() == self.tier_benefits[1]["Membership"]:
            harga_setelah_diskon = self.total - (self.total*0.1)
            cashback = 0
            harga_final = harga_setelah_diskon - cashback
            return f"anda mendapatkan benefit sebagai member {membership} dengan benefit {self.tier_benefits[1]["Another Benefits"]}, sehingga anda hanya perlu membayar {harga_final}."
        
        elif membership.capitalize() == self.tier_benefits[2]["Membership"]:
            harga_setelah_diskon = self.total - (self.total*0.08)
            cashback = 0
            harga_final = harga_setelah_diskon - cashback
            return f"anda mendapatkan benefit sebagai member {membership} dengan benefit {self.tier_benefits[2]["Another Benefits"]}, sehingga anda hanya perlu membayar {harga_final}."
        
        else:
            return "masukkan nama membership dengan benar"
        
    
# nama = input("masukkan nama anda: ")
# expense = int(input("masukkan "))
user_1 = PacCommerce(7_000_000, 12_000_000)
print(user_1.predict_membership())
print(user_1.show_benefit())
print(user_1.show_requirements())
print(user_1.calculate_price([200_000, 700_000, 150_000], "gold"))

