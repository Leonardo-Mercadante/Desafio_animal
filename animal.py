# Recebendo as três palavras nas variáveis globais:
palavra1 = input()
palavra2 = input()
palavra3 = input()

# Criando um dicionário com os animais e suas características
animais = {
    'vertebrado': {
        'ave': {
            'carnivoro': 'aguia',
            'onivoro': 'pomba'
        },
        'mamifero': {
            'onivoro': 'homem',
            'herbivoro': 'vaca'
        }
    },
    'invertebrado': {
        'inseto': {
            'hematofago': 'pulga',
            'herbivoro': 'lagarta'
        },
        'anelideo': {
            'hematofago': 'sanguessuga',
            'onivoro': 'minhoca'
        }
    }
}

# Buscando o animal correspondente
animal = animais.get(palavra1, {}).get(palavra2, {}).get(palavra3)

# Imprimindo o resultado
print(animal)
