Feature: revocar staff

@user1 @web

Scenario: Como usuario puedo revocar la invitacion de miembros del staff

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

  And I click invite people  

  And I wait for 2 seconds

  And I enter invite email "invite2@ghost.com"
  
  And I wait for 2 seconds

  And I click send invitation  

  And I wait for 5 seconds

  And I click close invite 

  And I wait for 2 seconds

  And I click setting

  And I wait for 5 seconds

  And I click staff

  And I wait for 2 seconds

  And I click revoke staff

  And I wait for 2 seconds


