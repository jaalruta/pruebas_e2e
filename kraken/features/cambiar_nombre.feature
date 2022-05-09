Feature: cambiar lenguaje publicacion

@user1 @web

Scenario: Como usuario puedo cambiar el nombre de publicacion de ghost

  Given I navigate to page "http://localhost:2368/ghost"

  And I wait for 5 seconds

  When I enter email "<USERNAME>"

  And I wait for 2 seconds

  And I enter password "<PASSWORD>"

  And I wait for 2 seconds

  And I click next

  And I wait for 5 seconds

  And I click setting

  And I wait for 2 seconds

  And I click general

  And I wait for 2 seconds

  And I expand title option

  And I wait for 2 seconds

  And I enter title body " MISO"

  And I wait for 2 seconds
  
  And I click save

  And I wait for 2 seconds



  

