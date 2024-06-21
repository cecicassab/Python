class Data:
    def to_str(self):
        return f'{self.dia}/{self.mes}/{self.ano}'
    
    
d1 = Data()
d1.dia = 3
d1.mes = 12
d1.ano = 2024

print(d1.to_str())