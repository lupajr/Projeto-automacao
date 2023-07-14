Feature: Teste de API - GET /usuarios

  Scenario: Obter lista de usuários
    Given que a API de usuários está disponível
    When eu envio uma requisição GET
    Then o status code deve ser 200
    And a resposta deve conter uma lista de usuários
