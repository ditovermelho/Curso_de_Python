"""
Introdução ao módulo Unittest

Unittest -> Teste Unitários

O que são testes unitários?

Teste é a forma de se testar unidades individuais de código fonte.

Unidade individuais podem ser: funções, métodos, classes, módulos etc.

# OBS: Teste unitário não é específico da linguagem Python.

Para criar nossos testes, criamos classes que herdam de unidades.TestCase e a
partir de então ganhamos todos os 'assertions' presentes no módulo.

Para rodar os testes, utilizamos unittest.main()

TestCase -> Casos de teste para sua unidade

# Conhecendo as assertions
https://docs.python.org/3/library/unittest.html

Método                         Checa que
assertEqual(a, b)              a == b
assertNotEqual(a, b)           a != b
assertTrue(x)                  x é verdadeiro
assertFalse(x)                 x é false
assertIs(a, b)                 a é b
assertIsNot(a, b)              a não é b
assertIsNone(x)                x é None
assertIsNotNone(x)             x não é None
assertIn(a, b)                 a está em b
assertNotIn(a, b)              a não está em b
assertInstance(a, b)           a é instância de b
assertNotInstance(a, b)        a não é instância de b

Por convenção, todos os testes em um test case, devem ter seu nome iniciado com
tes_

Para executar os testes com unittest
python nome_do_modulo.py

Para executar os testes com unittest no modo verbose
python nome_do_modulo.py -v

# Docstrings nos testes

Podemos acrescentar (e é recomendado) docstrinds nos nossos testes.

# Unittest - Outros tipos de assertions

assertEqual(a, b)

assertNotEqual(a, b)

assertTrue(x)

assertFalse(x)
"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

# Prática - Utilizando a abordagem TDD
