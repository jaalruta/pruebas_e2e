Feature: editar etiqueta

@user1 @web

Scenario: "Como usuario administrador inicio sesion y edito una etiqueta"

  Given I navigate to page "http://localhost:2368/ghost"
  And I wait for 5 seconds
  When I enter email "<USERNAME>"
  And I wait for 2 seconds
  And I enter password "<PASSWORD>"
  And I wait for 2 seconds
  And I click next
  And I wait for 5 seconds
  And I click tags
  And I wait for 5 seconds
  And I click new tag
  And I wait for 5 seconds
  And I enter tag name "segundo tag"
  And I wait for 5 seconds
  And I enter tag description "Descripcion para el segundo tag"
  And I wait for 2 seconds
  And I click save 
  And I wait for 2 seconds
  And I click tags
  And I wait for 2 seconds
  And I select a tag edicion
  And I wait for 2 seconds
  And I enter tag name "prueba tag edicion"
  And I wait for 2 seconds
  And I enter tag description "descripcion de prueba edicion"
  And I wait for 2 seconds
  And I click save 
  And I wait for 2 seconds
  Then the tag name must be "prueba tag edicion"