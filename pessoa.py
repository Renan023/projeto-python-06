import character,number,datetime

at = datetime.datetime.today().year
class Pessoa:

    def __init__(self):
        character.principal('Cadastro')
        self.nome = character.char('Nome ')
        self.nasc = number.leiaint('Nasc ')
        self.sexo = character.char('Sexo [M/F] ').strip().upper()[0]
        while self.sexo not in 'MmFf':
            print('\033[31mValor inserido incorreto\033[m')
            self.sexo = character.char('Sexo [M/F] ').strip().upper()[0]
        self.rg = character.char('Informe seu R.G(somente números) ')
        while len(self.rg) != 9:
            print('\033[31mInforme um R.G válido\033[m')
            self.rg = character.char('Informe seu R.G(somente números) ')
        self.cpf = character.char('Informe seu CPF(somente números) ')
        while len(self.cpf) != 11:
                print('\033[31mInforme o formato do CPF correto de 11 dígitos\033[m ')
                self.cpf = character.char('Informe seu CPF(somente números) ')
        s = 0
        r = 11
        for c in range(0,9):
            r-=1
            s+= int(self.cpf[c])*r
            mod = s % 11
            if mod == 0:
                dig = mod
            else:
                dig = 11- mod
                if dig >=10:
                    fdig = 0
                else:
                    fdig = dig
        r1=12
        s1=0
        for c in range(0,10):
            r1 -=1
            s1+= int(self.cpf[c])*r1
            mod1 = s1 % 11
            if mod1 == 0:
                dig1 = mod1
            else:
                dig1 = 11 - mod1
                if dig1 >=10:
                    sdig = 0
                else:
                    sdig = mod1
        if int(self.cpf[9:10]) == fdig or int(self.cpf[10:11]) == sdig:
            print('CPF válido')
        else:
           print('\033[31mCPF inválido\033[m')
           breakpoint()
        self.email = character.char('Informe seu e-mail ')
        email = character.char('Confirme seu e-mail ')
        while self.email != email:
            print('\033[31mErro na confirmação do email\033[m')
            self.email = character.char('Informe seu email ')
            email = character.char('Confirme seu e-mail ')
        self.tel = number.leiaint('Telefone/Whatsapp ')

    def dados(self):
        character.principal('Confirmação de cadastro')
        print(f'Nome {self.nome}')
        print(f'Nasc {self.nasc}')
        self.idade =  at - self.nasc
        print(f'Idade {self.idade} anos ')
        if self.idade > 18:
            print('Maior de idade')
        else:
            print('Menor de idade')
        if self.sexo not in 'Mm':
            print('Sexo Feminino')
        else:
            print('Sexo Masculino')
        print(f'R.G {self.rg} válido')
        print(f'CPF {self.cpf} válido')
        print(f'E-mail {self.email}')
        print(f'Tel {self.tel}')

