import requests

def main():
    print('#################')
    print('##Consulta CEP')
    print('#################')



    cep_input = input('Digite o CEP para consulta: ')

    if len(cep_input) != 8:
        print('quantidade de digitos invalida')
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    #print(request.json())

    address_data = request.json()

    if 'erro' not in address_data:
        print('===>Informações de CEP encontrado são: ')
        print(request.json())
        print('===>O logradouro é: {}'.format(address_data['logradouro']))

    else:
        print('Cep Invalido')
        print('----------------------')


    option = int(input('Deseja realizar uma nova consulta ?\n 1. Sim\n 2.Sair'))

    if option == 1:
        main()
    else:
        print('Saindo.... ')
        print('----------------------')



if __name__ == '__main__':
    main()



