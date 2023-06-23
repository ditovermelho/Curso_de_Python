"""
Decoradores (Decorators)

O que são decorators?

- Decorators são Funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando "@" (Syntax Sugar / Açúcar
Sintático)


|----------------------------------------------|
|            Function Decorator                |
------------------------------------------------

--------------------------------------------------
| |--------------------------------------------| |
| |             Função Decorada                | |
| |--------------------------------------------| |
| ---------------------------------------------- |

# Decorators como funções (Sintaxe não Recomendada / Sem Açúcar Sintático)


def seja_educado(funcao):
    def sendo():
        return ('Foi um prazer conhecer você!\n' + funcao() +
                '\nTenha um ótimo dia')
    return sendo


def saudação():
    return 'Seja Bem-Vindo(a) à Geek University'


# Testando 1
teste = seja_educado(saudação)
print(teste())
print()

# Testando 2


def raiva():
    return 'EU TE ODEIO!'


teste = seja_educado(raiva)
print(teste())
print()

# Decorators como Syntax Sugar (Açúcar Sintático)


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        return ('Foi um prazer conhecer você!\n' + funcao() +
                '\nTenha um excelente dia')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    return 'Meu nome é Pedro'


@seja_educado_mesmo
def dormir():
    return 'Quero dormir....'

# Testando 1


print(apresentando())
print()
print(dormir())
print()

|-----------------------------------------------------|
|  Home  |  Serviços  |  Produtos  |  Administrativo  |
|-----------------------------------------------------|

http://www.suaempresa.com.br/home
http://www.suaempresa.com.br/servicos
http://www.suaempresa.com.br/produtos
http://www.suaempresa.com.br/admin

OBS: Não é código funcional (Que funcione) é apenas exemplo

def checa_login(usuario):
    if not request.usuario:
        redirect('http://www.suaempresa.com.br/login')

def home(request):
    return 'Pode acessar home'

def servicos(request):
    return 'Pode acessar serviços'

def produtos(request):
    return 'Pode acessar produtos'

@checa_login
def admin(request):
    return 'Pode acessar admin'

# OBS: Não confunda Decorator com Decorator Function
"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None
