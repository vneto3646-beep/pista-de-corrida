from datetime import date

class Pessoa: 
    def __init__(self, nome, telefone, data_nascimento):
        self.nome = nome
        self.telefone = telefone
        self.data_nascimento = data_nascimento

def Registro_Pessoa(self):
    obj1 = Pessoa("Jamille Cristiny Kurek Ferreira", "47 984831723", date(2009, 12, 09))
    obj2 = Pessoa("Manuella Sperotto", "47 981267434", date(2010, 02, 11))
    obj3 = Pessoa("Vicente Neto Fernandes Menezes", "47 908714364", date(2009, 03, 21))
    obj4 = Pessoa("Fabricio", "47 984010893", date(1989, 04, 02))
    obj5 = Pessoa("Luana", "47 998612794", date(1986, 12, 04))
    obj6 = Pessoa("Marcos", "47 998613141", date(1970, 08, 01))

class Cliente: 
    def __init__ (self, pessoa, email):
        self.pessoa = pessoa
        self.email = email

def Registro_Cliente(self):
    obj1 = Cliente("Jamille Cristiny Kurek Ferreira", "jamille@gmail.com")
    obj2 = Cliente("Manuella Sperotto", "manuella@gmail.com")
    obj3 = Cliente("Vicente Neto Fernandes Menezes", "vicente@gmail.com")

class Veiculo:
    def __init__ (self, tipo, placa, cor, tanque, rendimento, odometro, desenho):
        self.tipo = tipo
        self.placa = placa
        self.cor = cor
        self.tanque = tanque
        self.rendimento = rendimento
        self.odometro = 0
        self.desenho = desenho
    def andar(self):
        self.odometro += self.rendimento    
        self.tanque -= 1 # self.tanque = self.tanque - 1

def Registro_Veiculo(self):
    obj1 = Veiculo("carro", "bra2e19", "vermelho")
    obj2 = Veiculo("onibus", "hda5q94", "amarelo")

def __str__(self):
    return "Placa:"+self.placa+",cor:"+self.cor

class VeiculoComPassageiro(Veiculo):
    def __init__ (self,tipo, placa, cor, lugares):
        self.lugares = lugares
        super().__init__(tipo, placa, cor)

def Registro_VeiculoComPassageiro(self):
    obj1 = VeiculoComPassageiro("carro", "bra2e19", "vermelho", "5")
    obj2 = VeiculoComPassageiro("onibus", "hda5q94", "amarelo", "40")

def __str__(self):
    return f"Lugares:{self.lugares}{super().__str__()}"

class Carro(VeiculoComPassageiro):
    def __init__(self, placa, cor,portas):
        self.portas = portas
        super().__init__ (placa,cor)

def Registro_Carro(self):
    obj = Carro("bra2e19", "vermelho", "4")

def __str__(self):
    return f"Portas:{self.portas}{super().__str__()}"

class Onibus(VeiculoComPassageiro):
    def __init__(self, placa, cor,lugares):
        self.lugares = lugares
        super().__init__(placa,cor)

def Registro_Onibus(self):
    obj = Onibus("hda5q94", "amarel", "40")

def __str__(self):
    return f"Lugares:{self.lugares}{super().__str__()}"

class Moto(Veiculo):
    def __init__(self, placa, cor,lugares):
        self.lugares = lugares
        super().__init__ (placa,cor)

def Registro_Moto(self):
    obj = Moto("plq0j13", "preto", "2")

def __str__(self):
    return f"Lugares:{self.lugares}{super().__str__()}"

class Servico:
    def __init__(self, tipo, valor, nome_mecanico,placa):
        self.tipo = tipo
        self.valor = valor
        self.nome_mecanico = nome_mecanico
        self.placa = placa

def Registro_Servico(self):
    obj1 = Servico("Manutenção de suspensão", 3500, "Fabricio", "bra2e19")
    obj2 = Servico("Limpeza completa", 1000, "Luana", "hda5q94")
    obj3 = Servico("Troca de óleo", 300, "Marcos", "plq0j13")

class Mecanico:
    def __init__(self,pessoa) :
        self.pessoa = pessoa

def Registro_Mecanico(self):
    obj1 = Mecanico("Fabricio")
    obj2 = Mecanico("Luana")
    obj3 = Mecanico("Marcos")


class OrdemServico:
    def __init__ (self,data_entrada,veiculo,data_saida,cliente,desconto):
        self.data_entrada = data_entrada
        self.veiculo = veiculo
        self.data_saida = data_saida
        self.cliente = cliente
        self.desconto = desconto

def Registro_OrdemServico(self):
    obj1 = OrdemServico(date(2026, 08, 04), "bra2e19", date(2026, 10, 04), "Jamille Cristiny Kurek Ferreira", 0)
    obj2 = OrdemServico(date(2026, 01, 19), "hda5q94", date(2026, 01, 21), "Manuella Sperotto", 0)
    obj3 = OrdemServico(date(2026, 04, 22), "plq0j13", date(2026, 04, 23), "Vicente Neto Fernandes Menezes", 0)

class Pista:
    def __init__(self, extensao, veiculos):
        self.extensao = extensao
        self.veiculos = []

    def tick(self):
        for v in self.veiculos:
            if v.odometro <= self.extensao:
                v.andar() # anda, veículo :-)

    def pista_grafica(self):
        for v in self.veiculos:
            s = "." * int(v.odometro/10)
            print(v.modelo,"(",v.odometro,"):",s,v.desenho)            

fox = Veiculo("Fox", 42, 12, "o~W~o")
biz = Veiculo("Honda Biz", 5, 40, "o-o")

indianapolis = Pista (500)
indianapolis.veiculos.append(fox)
indianapolis.veiculos.append(biz)
while True:
    indianapolis.tick() 
    #print(indianapolis.veiculos[0].modelo, "andou", indianapolis.veiculos[0].odometro)
    #print(indianapolis.veiculos[1].modelo, "andou", indianapolis.veiculos[1].odometro)
    indianapolis.pista_grafica()
    
    time.sleep(1)

    if indianapolis.veiculos[0].odometro >= 500 and indianapolis.veiculos[1].odometro >= 500:
        break 
