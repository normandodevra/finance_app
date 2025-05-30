import json,copy

class Item:
    def __init__(self,
                 name=None, price=None, 
                 type=None, category=None, 
                 subcategory=None, date=None, 
                 date_payment=None, account=None,
                 parcelas=None,n_parcelas=None):
        self.name = name
        self.price = price
        self.type = type
        self.category = category
        self.subcategory = subcategory
        self.date = date
        self.date_payment = date_payment
        self.account = account
        self.parcelas = parcelas
        self.n_parcelas = n_parcelas

    def assign(self, **kwargs):
        """
        Atribui valores aos atributos da classe com base nos argumentos fornecidos.
        :param kwargs: Dicionário de atributos e valores.
        """
        for key, value in kwargs.items():
            if hasattr(self, key):  # Verifica se o atributo existe na classe
                setattr(self, key, value)
            else:
                raise AttributeError(f"Atributo '{key}' não existe na classe Item.")

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_type(self):
        return self.type

    def get_category(self):
        return self.category

    def get_subcategory(self):
        return self.subcategory

    def get_date(self):
        return self.date

    def get_date_payment(self):
        return self.date_payment

    def get_account(self):
        return self.account

    def get_parcelas(self):
        return self.parcelas

    def get_n_parcelas(self):
        return self.n_parcelas

    def copy(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f'{self.name} - {self.price}'

    def __repr__(self):
        return f'{self.name} - {self.price}'
    
    def to_dict(self):
        return {
            'DATA COMPETÊNCIA': self.date,
            'DATA CAIXA': self.date_payment,
            'DESCRIÇÃO': self.name,
            'VALOR': self.price,
            'CONTA': self.account,
            'POTE': self.type,
            'CATEGORIA': self.category,
            'SUBCATEGORIA': self.subcategory,
            'OBSERVAÇÃO': "-",
            'PARCELAS': self.parcelas,
            'N PARCELA': self.n_parcelas,
            'NATUREZA': '-',
            'AUTOMÁTICO': '-'
        }
    
    def to_json(self):
        return json.dumps(self.to_dict())
    
    def from_dict(self, data):
        self.name = data['DESCRIÇÃO']
        self.price = data['VALOR']
        self.type = data['POTE']
        self.category = data['CATEGORIA']
        self.subcategory = data['SUBCATEGORIA']
        self.date = data['DATA COMPETÊNCIA']
        self.date_payment = data['DATA CAIXA']
        self.account = data['CONTA']
        self.parcelas = data['PARCELAS']
        self.n_parcelas = data['N PARCELA']

    def __eq__(self, value):
        if isinstance(value, Item):
            return (self.name == value.get_name() and self.price == value.get_price() and self.type == value.get_type() and self.category == value.get_category() and self.subcategory == value.get_subcategory() and self.date == value.get_date() and self.date_payment == value.get_date_payment() and self.account == value.get_account())
        return False

    def from_json(self, data):
        self.from_dict(json.loads(data))

    def set_type(self, type):
        self.type = type
    
    def set_category(self, category):
        self.category = category

    def set_subcategory(self, subcategory):
        self.subcategory = subcategory
    
    def set_date(self, date):
        self.date = date
    
    def set_date_payment(self, date_payment):
        self.date_payment = date_payment

    def set_account(self, account):
        self.account = account

    def set_price(self,price):
        self.price = price

    def set_name(self,name):
        self.name = name   

    def set_nparcelas(self,nparcelas):
        self.n_parcelas = nparcelas
    
    def set_parcelas(self,parcelas):
        self.parcelas = parcelas

    def get_all(self):
        return {
            'name': self.name,
            'price': self.price,
            'type': self.type,
            'category': self.category,
            'subcategory': self.subcategory,
            'date': self.date,
            'date_payment': self.date_payment,
            'account': self.account
        }
    def print(self):
        print("name: ", self.name)
        print("price: ", self.price)
        print("type: ", self.type)
        print("category: ", self.category)
        print("subcategory: ", self.subcategory)
        print("date: ", self.date)
        print("data_payment: ", self.date_payment)
        print("account: ", self.account)
    
class Itens:
    def __init__(self):
        self.itens = []

    def __eq__(self, value):
        if isinstance(value, Itens):
            return self.itens == value.itens
        return False
    
    def add(self, item):
        self.itens.append(item)
    
    def remove(self, item):
        self.itens.remove(item)
    
    def get(self, index):
        return self.itens[index]
    
    def get_by_name(self, name):
        for item in self.itens:
            if item.get_name() == name:
                return item
        return None

    def get_all(self):
        return self.itens
    
    def clear(self):
        self.itens.clear()
        self.itens = []
    
    def to_dict(self):
        return [item.to_dict() for item in self.itens]
    
    def to_json(self):
        return json.dumps(self.to_dict())
    
    def from_dict(self, data):
        self.clear()
        for item in data['itens']:
            i = item()
            i.from_dict(item)
            self.add(i)
    
    def from_json(self, data):
        self.from_dict(json.loads(data))
    
    def __str__(self):
        return f'{self.itens}'
    
    def __repr__(self):
        return f'{self.itens}'
    
    def __len__(self):
        return len(self.itens)
    
    def __iter__(self):
        return iter(self.itens)
    
    def __getitem__(self, index):
        return self.itens[index]
    
    def __setitem__(self, index, value):
        self.itens[index] = value

    def from_csv(self, file_path):
        import csv
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                i = Item()
                i.from_dict(row)
                self.add(i)

    def from_excel(self, file_path,salvar=False):
        import pandas as pd
        lancamentos = pd.read_excel(
            file_path,
            sheet_name="Pandas",
            usecols="A:O",
            header=0
        )
        
        lancamentos.rename(columns={
            'DATA COMPETÊNCIA': 'DATA_COMPETÊNCIA',
            'DATA CAIXA': 'DATA_CAIXA',
            'VALOR': 'VALOR',
            'DESCRIÇÃO': 'DESCRICAO',
            'CONTA': 'CONTA',
            'POTE': 'POTE',
            'CATEGORIA': 'CATEGORIA',
            'SUBCATEGORIA': 'SUBCATEGORIA'
        }, inplace=True)
        

        lancamentos['DATA_CAIXA'] = pd.to_datetime(lancamentos['DATA_CAIXA'], dayfirst=True, errors='coerce')
        lancamentos['DATA_COMPETÊNCIA'] = pd.to_datetime(lancamentos['DATA_COMPETÊNCIA'], dayfirst=True, errors='coerce')

        lancamentos['VALOR'] = pd.to_numeric(lancamentos["VALOR"], errors='coerce')

        lancamentos['DATA_COMPETÊNCIA'] = lancamentos['DATA_COMPETÊNCIA'].ffill()

        # Sort by date (newest first)
        lancamentos = lancamentos.sort_values('DATA_COMPETÊNCIA', ascending=False)

        # Reset index
        lancamentos = lancamentos.reset_index(drop=True)

        for row in lancamentos.itertuples(index=False):  # index=False para evitar o índice como parte da tupla
            if row.VALOR is not None:
                item = Item()
                item.set_account(row.CONTA)
                item.set_date(row.DATA_COMPETÊNCIA.strftime("%d/%m/%Y"))
                item.set_date_payment(row.DATA_CAIXA.strftime("%d/%m/%Y"))
                item.set_name(row.DESCRICAO)
                item.set_price(row.VALOR)
                item.set_type(row.POTE)
                item.set_category(row.CATEGORIA)
                item.set_subcategory(row.SUBCATEGORIA)
                self.add(item.to_dict())

        if(salvar):
            import outs        
            outs.to_csv(self.itens, './database/export.csv')

    def print(self):
        for i in self.itens:
            print(i)

    def extend(self, itens):
        #Verifique os repetidos:
        for i in itens:
            if i not in self.itens:
                self.itens.append(i)
    
    def reset(self):
        self.itens.clear()
        self.itens = []
        return self.itens

    def empty(self):
        if len(self.itens) == 0:
            return True
        else:
            return False

    def add_lancamento(self,lancamentos,conta):
                item = Item()
                for row in lancamentos.itertuples():
                    if row.valor is not None:
                        item.set_account(conta)
                        item.set_date(row.data.strftime("%d/%m/%Y"))
                        try:
                            item.set_date_payment(row.data_payment.strftime("%d/%m/%Y"))
                        except:
                            item.set_date_payment(item.date)
                        item.set_name(row.lancamento)
                        item.set_price(row.valor)
                        self.add(item.to_dict())
                return True
    
    def gerar_auto(self):
        df = Itens()
        auto = Itens()

        df.from_csv('./database/lancamento.csv')
        auto.from_csv('./database/auto.csv')

        repetido = False
        #Testa se já existe um item com o mesmo nome e valor
        if not(auto.empty()):
            for i in range(len(df)):
                try:
                    for j in range(len(auto)):
                        if df.get(i) == auto.get(j):
                            repetido = True
                            break
                except Exception as e:
                    print("Erro ao comparar os itens. Erro: ",e,"\n")
                    repetido = True
                    break
        if repetido:
            return
        
        import outs as o
        o.to_csv(df.to_dict(), './database/auto.csv')

class Dados:
    def __init__(self):
        self.categorias = {
            "Despesas Básicas": {
                "Alimentação": ["Mercado", "Restaurante", "Lanches", "Suplementação"],
                "Assinaturas": ["Telefone", "Icloud", "Stream"],
                "Despesas Bancarias": ["Juros e IOF", "Taxas"],
                "Transporte": ["Aplicativo", "Carro manutenção", "Carro melhorias", "Estacionamento", "Combustível"],
                "Casa": ["Diarista Alimentação", "Diarista Limpeza", "Água", "Energia", "Jardineiro", "Manutenção Casa", "Material de limpeza"],
                "Cuidado pessoal": ["Academia", "Cabeleireiro", "Estética", "Saúde", "Fisioterapia"],
                "Vestuário": ["Roupas", "Calçados", "Acessórios"],
                "Estudos": ["Cursos", "Livros"],
                "Seguro": ["Carro", "Pessoal", "Residencial"],
                "Esporte": ["Academia", "Surf", "Tennis"],
                "Férias": ["Passagem", "Hospedagem", "Alimentação", "Ticket e Ingressos", "Presentes"]
            },
            "Conciliação": {
                "Cartão de Credito": ["CC Bradesco Infinity"]
            },
            "Despesa Empresa": {
                "Parcelamento de impostos": ["Harmonia Locações", "Esgmax", "Soul Eventos"]
            },
            "Despesas Profissionais": {
                "Taxa": ["Corretor"],
                "Gestor": ["Dennis"],
                "Estagiario": ["App","Projetos"],
                "Assinatura Software": ["Microsoft"],
                "Assinatura Email": ["GSUITE"]
            },
            "Despesas Projetos": {
                "Cadastro Mobiliario Anual": ["Showme"],
                "Proponente Parceito": ["Geovane"]
            },
            "Doação": {
                "Presentes": ["Aniversário", "Natal"],
                "UDV": ["Dízimo"]
            },
            "Investimento": {
                "Bens Materias": ["Equipamento","Eletrônicos"],
                "Férias": ["Fundo Férias"],
                "Casa": ["Fundo Casa"],
                "Kite": ["Material"],
                "Escritório": ["Material"]
            },
            "Emprestimos": {
                "Bloqueio de conta": ["Bloqueio Judicial"], 
                "Capital de giro": ["Mercedes","TonTon"],
                "Dharma": ["Natal Experience"],
                "Euro": ["Kite"],
                "Financeamento":["Parcelamento Compass", "Parcelamento Mercedes"], 
                "Juros":["Conta Corrente", "Cartão de Credito"], 
                "Fundo Abreu":["RA Mall", "Impostos"], 
                "Miguel":["RA Mall", "Holding"],
                "Ingrid":["Ingrid"], 
                "RA Mall":["Condomínio"],
                "Terceiros":["Terceiros"], 
                "Saque":["Saque"]
            },
            "Receitas": {
                "Salário": ["Bonor"],
                "Malca": ["Eventos", "Empréstimo"],
                "Dharma": ["Showme", "Natal Experience", "Pé no Samba 2023", "Natal Beats 2023"],
                "AirBnB": ["AirBnB"],
                "Pai": ["Extra", "Empréstimo"],
                "Harmonia": ["RA Mall"]
            },
            "Fundo": {
                "Curto Prazo": ["Harmonia", "Eletrônicos", "Férias", "Escritório", "Kite"],
                "Giro": ["Ingrid"],
                "Liberdade Financeira": ["Liberdade Financeira"],
                "Longo Prazo": ["Nova Casa", "Novo Carro"]
            },
            "Investimentos": {
                "Kite": ["Kite"]
            },
            None:{
                None:[None]
            }
        }
        self.cartoes = {"CC Nubank":1,"CC Bradesco":5,
                    "CC Itaú Black":17,"CC Itaú Master":6,
                    "CC MercadoPago":7,"CC SAMS":1,
                    "CC NovoBanco":2}
        
        self.contas = ["Itau","BRADESCO","BB","C6","Neon","Nubank","NovoBanco"]
        
    def get_categorias(self):
        return self.categorias
    
    def get_pote_values(self):
        return list(self.categorias.keys())

    def get_categorias_values(self):
        subcategorias = []
        for categoria in self.categorias.values():
            subcategorias.extend(categoria)
        return subcategorias
    
    def get_subcategorias_values(self):
        subcategorias = []
        for categoria in self.categorias.values():
            for subcategoria in categoria.values():
                subcategorias.extend(subcategoria)
        return subcategorias
    
    def get_cartoes(self):
        return self.cartoes
    
    def get_contas(self):
        return self.contas