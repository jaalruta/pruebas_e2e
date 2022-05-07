Feature: crear post

@user1 @web

Scenario: Como usuario administrador inicio sesion, creo un post y lo elimino 

  Given I navigate to page "http://localhost:2368/ghost"

  And I wait for 5 seconds

  When I enter email "<USERNAME>"

  And I wait for 2 seconds

  And I enter password "<PASSWORD>"

  And I wait for 2 seconds

  And I click next

  And I wait for 5 seconds

  And I click post publish 

  And I wait for 5 seconds

  And I enter post title "titulo de pruebas borrar"

  And I wait for 2 seconds

  And I enter post body "cuerpo del post de prueba"
 
  And I wait for 2 seconds

  And I click publish menu

  And I wait for 2 seconds

  And I click publish
  
  And I wait for 2 seconds
  
  And I click publish confirm

  And I wait for 2 seconds

  And I click post menu 

  And I wait for 2 seconds

  And I click posts edit

  And I wait for 2 seconds

  And I click post settings

  And I wait for 2 seconds

  And I click delete post 

  And I wait for 2 seconds

  And I click confirm delete post 

  And I wait for 2 seconds
 