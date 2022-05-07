Feature: Crear etiqueta

@user1 @web
Scenario: "Como usuario administrador inicio sesion y creo una etiqueta"

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
  And I enter tag name "primer tag"
  And I wait for 5 seconds
  And I enter tag description "Esta es una descripción"
  And I wait for 2 seconds
  And I click save 
  And I wait for 2 seconds
  And I click tags
  And I wait for 2 seconds
  Then the tag must be created
 
  
