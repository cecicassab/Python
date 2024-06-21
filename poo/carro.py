class Carro:
    vel_atual=0
    
    def __init__(self, vel_max):
        self.vel_max = vel_max
        
    def acelerar(self,velocidade=5):
        if self.vel_atual + velocidade > self.vel_max:
            self.vel_atual = self.vel_max
            return self.vel_atual 
        else:
            self.vel_atual = self.vel_atual + velocidade
            return self.vel_atual
        
    
    def freiar(self,delta=5):
        if self.vel_atual - delta < 0:
            self.vel_atual = 0
            return self.vel_atual 
        else:
            self.vel_atual = self.vel_atual - delta
            return self.vel_atual


if __name__ == '__main__':
    c1 = Carro(180)
    
    for _ in range(25):
        print(c1.acelerar(8))
        
    for _ in range(10):
        print(c1.freiar(delta=20))