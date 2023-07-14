import requests
from behave import given, when, then

@given('que a API de usuários está disponível')
def step_given_api_available(context):
    context.api_url = "https://serverest.dev/usuarios"

@when('eu envio uma requisição GET')
def step_when_send_get_request(context):
    url = context.api_url
    context.response = requests.get(url)

@then('o status code deve ser 200')
def step_then_check_status_code(context):
    assert context.response.status_code == 200

@then('a resposta deve conter uma lista de usuários')
def step_then_check_user_list(context):
    response_data = context.response.json()
    assert 'usuarios' in response_data
    users = response_data['usuarios']
    assert isinstance(users, list)
    assert len(users) > 0
    for user in users:
        assert 'nome' in user
        assert 'email' in user
        assert 'idade' in user
