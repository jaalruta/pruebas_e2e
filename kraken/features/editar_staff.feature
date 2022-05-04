Feature: revocar staff

@user1 @web

Scenario: Como usuario puedo editar la informacion de miembros del staff

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

  And I click staff

  And I wait for 2 seconds

  And I click over a staff member

  And I wait for 2 seconds

  And I enter staff name "Pruebas modificacion staff"

  And I wait for 2 seconds

  And I enter staff bio "Pruebas modificacion bio staff"

  And I wait for 2 seconds

  And I click save

  And I wait for 2 seconds

