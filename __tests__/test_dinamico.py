# 1- Bibliotecas - Framework
import json
import pytest
import requests                      

from utils.utils import ler_csv 

# Atributos ou variaveis para utilização no item: USER/pet
id = 184409097          
username = 'Tom'     
firstName = 'Tomaz'       
lastName = 'Santos'  
email = 'santos@bol.com.br'
password = 'SantosII'
phone = 2138221653
userStatus = 34542
url = 'https://petstore.swagger.io/v2/user'      
headers = {'Content-Type': 'application/json'}

# Efetuando teste dinamico utilizando um arquivo CSV.
@pytest.mark.parametrize('id,username,firstName,lastName,email,password,phone,userStatus',
                        ler_csv('./fixtures/csv/pet.csv'))
def test_post_user_dinamico(id,username,firstName,lastName,email,password,phone,userStatus):
    
    # Configura
    pet = {}                                    # cria uma lista vazia chamada user
    pet['id'] = id
    pet['username'] = username
    pet['firtName'] = firstName
    pet['lastName'] = lastName
    pet['email'] = email
    pet['password'] = password
    pet['phone'] = phone
    pet['userStatus'] = userStatus
    
    pet = json.dumps(obj=pet, indent=4)         #  carrega e adequa a estrutura de linhas e colunas do arquivo json      
    print('\n' + pet)                           # visualiza como ficou a estrutura json criado dinamicamente
    
    #Executa
    response = requests.post(
        url = url,
        headers = headers,
        data = pet,
        timeout = 5
    )
    # Compara
    response_body = response.json()
    
    assert response.status_code == 200     
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(id)
    
def test_delete_user_dinamico():  
                                            
    response = requests.delete(
        url = f'{url}/{username}',                                  
        headers = headers,
        timeout = 5
    )
    response_body = response.json()
    
    assert response.status_code == 200                              
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] ==  username
    
    
