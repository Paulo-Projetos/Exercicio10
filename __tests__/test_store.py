# 1- Bibliotecas - Framework
import json
import pytest
import requests                           

# 2.1- Atributos ou variaveis para utilização no item: USER/pet
id = 9          
petId = 184409099
quantity = 1       
shipDate = '2025-06-04T13:26:21.291+0000'  
status = 'placed'
complete = True

url = 'https://petstore.swagger.io/v2/store/order'      
headers = {'Content-Type': 'application/json'}

# 2.2- Funções / Metodo
def test_post_store():                                
    pet = open('./fixtures/json/store.json')         
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
    assert response_body['id'] == id
    assert response_body['petId'] == petId
    assert response_body['quantity'] == quantity
    assert response_body['shipDate'] == shipDate
    assert response_body['status'] == status
    assert response_body['complete'] == complete


def test_get_store():                                
    response = requests.get(
        url = f'{url}/{id}',            
        headers = headers,                 
    )                                       
    
    response_body = response.json()
    
    assert response.status_code == 200 
    assert response_body['id'] == id
    assert response_body['petId'] == petId
    assert response_body['quantity'] == quantity
    assert response_body['shipDate'] == shipDate
    assert response_body['status'] == status
    assert response_body['complete'] == complete
    
def test_delete_store():                                          
    
    response = requests.delete(
        url = f'{url}/{id}',                                  
        headers = headers,  
    )
    response_body = response.json()
    
    assert response.status_code == 200                              
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] ==  str(id)
    
    
