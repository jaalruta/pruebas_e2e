Feature: eliminar miembro

@user1 @web

Scenario: Como usuario administrador inicio sesion y elimino un miembro

  Given I navigate to page "http://localhost:2368/ghost"

  And I wait for 5 seconds

  When I enter email "<USERNAME>"

  And I wait for 2 seconds

  And I enter password "<PASSWORD>"

  And I wait for 2 seconds

  And I click next

  And I wait for 5 seconds

  And I click members

  And I wait for 2 seconds

  And I click new member

  And I wait for 5 seconds

  And I enter member name "pruebas miembro borrado"

  And I wait for 2 seconds

  And I enter member email "pruebas222333@ghost.com"

  And I wait for 2 seconds

  And I enter member note "nota de prueba borrado"

  And I wait for 2 seconds

  And I click save 
  
  And I wait for 2 seconds

  And I click members

  And I wait for 2 seconds
  
  And I select a member

  And I wait for 2 seconds

  And I click config member

  And I wait for 2 seconds

  And I click delete member
  
  And I wait for 2 seconds

  And I click confirm delete

  And I wait for 2 seconds

  Then the member "pruebas miembro borrado" must be delete