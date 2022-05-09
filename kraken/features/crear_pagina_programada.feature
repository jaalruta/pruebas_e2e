Feature: crear pagina programada

@user1 @web

Scenario: Como usuario administrador inicio sesion y creo un post

  Given I navigate to page "http://localhost:2368/ghost"

  And I wait for 5 seconds

  When I enter email "<USERNAME>"

  And I wait for 2 seconds

  And I enter password "<PASSWORD>"

  And I wait for 2 seconds

  And I click next

  And I wait for 5 seconds

  And I click pages

  And I wait for 5 seconds

  And I click new pages

  And I wait for 5 seconds

  And I enter pages title "titulo de pagina"

  And I wait for 2 seconds

  And I enter pages body "cuerpo de la pagina de prueba"
 
  And I wait for 2 seconds

  And I click publish menu

  And I wait for 2 seconds

  And I click Schedule it for later

  And I wait for 2 seconds

  And I click publish
  
  And I wait for 2 seconds
  
  And I click pages menu 

  And I wait for 2 seconds