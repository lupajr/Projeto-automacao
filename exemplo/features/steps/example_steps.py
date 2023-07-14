import requests
from behave import given, when, then

@given('uma URL de API')                                    # Define a URL que sera usada
def step_given_api_url(context):
    context.api_url = "https://reqres.in/api/users/2"   

@when('eu mando uma requisição GET para a URL da API')      # Manda a requisiçao pra URL
def step_when_send_get_request(context):    
    url = context.api_url
    context.response = requests.get(url)

@then('o status code deverá ser 200')                       # Verifica o status code
def step_then_check_status_code(context):
    assert context.response.status_code == 200

@then('o response deverá conter dados do usuário')          # Valida a existencia dos dados do usuario
def step_then_check_user_data(context):
    response_data = context.response.json()
    assert 'data' in response_data
    user_data = response_data['data']
    assert 'id' in user_data
    assert 'email' in user_data
    assert 'first_name' in user_data
    assert 'last_name' in user_data

    assert user_data['first_name'] == 'Janet'               # Valida os dados em si
    assert user_data['last_name'] == 'Weaver'    
    assert user_data['email'] == 'janet.weaver@reqres.in'           
