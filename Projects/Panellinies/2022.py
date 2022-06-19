L1 = ['ΕΠΤΑΝΗΣΑ', 'ΚΥΚΛΑΔΕΣ', 'ΔΩΔΕΚΑΝΗΣΑ', 'ΣΠΟΡΑΔΕΣ']
L2 = ['ΣΚΟΠΕΛΟΣ', 'ΝΑΞΟΣ', 'ΙΘΑΚΗ', 'ΚΑΡΠΑΘΟΣ']

print(L1[2])
print(L2[-3])
print(L1[1] + L2[1])
print(len(L2))


class Mathitis:
    def __init__(self, am, onoma, vathmos):
        self.am = am
        self.onoma = onoma
        self.vathmos = vathmos
        vathmos = 25

    def tipose(self):
        if self.vathmos >= 10:
            print("Προάγεται")
        else:
            print("Παραπέμπεται")


mathitis1 = Mathitis(103, "Νικολάου", 19)
mathitis2 = Mathitis(105, "Γεωργίου", 9)
mathitis1.tipose()
mo = (mathitis1.vathmos + mathitis2.vathmos) / 2

print(mo)
