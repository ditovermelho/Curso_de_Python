"""
Estruturas condicionais
if (Se), else (Se não), elif
"""

idade = 6
"""
# Estrutura condicional if, else em c

if(idade < 18){
    print("Menor de idade");
}else if(idade == 18){
    print("Tem 18 anos");
}else{
    print("Tem mais de 18 anos");
}

# Estrutura condicional if, else em Java

if(idade < 18){
    System.out.println("Menor de idade");
}else if(idade == 18){
    System.out.println("Tem 18 anos");
}else{
    System.out.println("Tem mais de 18 anos");
}
"""
if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print("Tem 18 anos")
elif idade == 26:
    print('Tem 26 anos')
else:
    print("Tem mais de 18 anos")