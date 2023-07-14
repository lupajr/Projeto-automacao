Feature: Exemplo de teste de API

  Scenario: Pegar dados de um usuário específico
    Given uma URL de API
    When eu mando uma requisição GET para a URL da API
    Then o status code deverá ser 200 
    And o response deverá conter dados do usuário
