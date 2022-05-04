Feature: crear post

@user1 @web

Scenario: Como usuario administrador inicio sesion y creo un post

  Given I navigate to page "http://localhost:2368/ghost"

  And I wait for 5 seconds

  When I enter email "pruebas@ghost.com"

  And I wait for 2 seconds

  And I enter password "Pruebas12345"

  And I wait for 2 seconds

  And I click next

  And I wait for 5 seconds

  And I click posts

  And I wait for 5 seconds

  And I click new posts

  And I wait for 5 seconds

  And I enter post title "titulo de pruebas"

  And I wait for 2 seconds

  And I enter post body "cuerpo del post de prueba"
 
  And I wait for 2 seconds

  And I click publish menu

  And I wait for 2 seconds

  And I click publish
  
  And I wait for 2 seconds
  
  And I click publish confirm

  And I wait for 2 seconds