# 1- Bibliotecas - Framework
import json
import pytest
import requests                           

# 2.1- Atributos ou variaveis para utilização no item: USER/pet
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

# 2.2- Funções / Metodo
def test_post_user():                                
    pet = open('./fixtures/json/user1.json')         
    data = json.loads(pet.read())                  
# Executa
    response = requests.post(               
        url = url,                          
        headers = headers,                  
        data = json.dumps(data),            
        timeout = 5                         
    )
# Valida
    response_body = response.json()       
    
    assert response.status_code == 200     
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(id)


def test_get_user():                                
    response = requests.get(
        url = f'{url}/{username}',            
        headers = headers,                 
    )                                       
    
    response_body = response.json()
    
    assert response.status_code == 200 
    assert response_body['id'] == id
    assert response_body['username'] == username
    assert response_body['firstName'] == firstName
    assert response_body['lastName'] == lastName
    assert response_body['password'] == password
    assert response_body['phone'] == str(phone)
    assert response_body['userStatus'] == userStatus
    
def test_put_user():
    pet = open('./fixtures/json/user2.json') 
    data = json.loads(pet.read())
    
    response = requests.put(
        url = f'{url}/{username}',                       
        headers = headers,
        data = json.dumps(data),           
        timeout = 5
    )
    response_body = response.json()
    
    assert response.status_code == 200                              
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(id)

def test_delete_user():                                          
    
    response = requests.delete(
        url = f'{url}/{username}',                                  
        headers = headers,  
    )
    response_body = response.json()
    
    assert response.status_code == 200                              
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] ==  'Tom'   
    