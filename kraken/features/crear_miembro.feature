Feature: crear miembro

@user1 @web

Scenario: Como usuario administrador inicio sesion y creo un miembro

  Given I navigate to page "http://localhost:2368/ghost"

  And I wait for 5 seconds

  When I enter email "<USERNAME>"

  And I wait for 2 seconds

  And I enter password "<PASSWORD>"

  And I wait for 2 seconds

  And I click next

  And I wait for 5 seconds

  And I click members

  And I wait for 5 seconds

  And I click new member

  And I wait for 5 seconds

  And I enter member name "pruebas miembro"

  And I wait for 2 seconds

  And I enter member email "pruebas222@ghost.com"

  And I wait for 2 seconds

  And I enter member note "nota de prueba"

  And I wait for 2 seconds

  And I click save 
  
  And I wait for 2 seconds
  
  Then the member must be created