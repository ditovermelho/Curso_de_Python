"""
Por que testar nosso código?

Testes Automatizado!

       Aplicação web
--------------------------------
|                              |
|     frontend e backend       |
--------------------------------
|     testes automatizados     |
--------------------------------

Por que testar nosso código?
    - Reduzir bugs (problemas) no código;
    - Testes garantem que novos recursos da sua aplicação não quebrem (alterem)
    recurso antigos;
    - Testes garantem que bugs (problemas) que foram corrigidos anteriormente
    continuam corrigidos;
    - Testes garantem que a refatoração que costumamos a fazer não tragam novo
    bugs (problemas);

TDD - Test Driven Development (Desenvolvimento Guiado por Testes)

Com TDD é utilizado estágio de desenvolvimento:
    - Você escreve seu teste primeiro;
    - Então você escreve o código mínimo suficiente para fazer o passar (ou
    seja, executar com sucesso);
    - Então refatora o código para realizar a funcionalidade e testa novamente;
    - Uma vez que o teste passe, o recurso é considerado completo;

Estes estágios de desenvolvimento do TDD são quase como um mantra que os
desenvolvedores seguem, conhecidos como:
    - Red;
    - Green;
    - Refactor;


"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


class Animal:

    def __init__(self, nome) -> None:
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


class Gato(Animal):
    def __init__(self, nome) -> None:
        super().__init__(nome)

    def miar(self):
        return f'{self.nome} está miando...'


felix = Gato('Felix')
print(felix.nome)
print(felix.miar())
print()
