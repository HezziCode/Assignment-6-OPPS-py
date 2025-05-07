class Bank:
    bank_name = "\nHBL Bank"

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

b1 = Bank()
print(b1.bank_name)
print("\nNow changing bank name")
Bank.change_bank_name("\nFinical secure Bank")
print(b1.bank_name)