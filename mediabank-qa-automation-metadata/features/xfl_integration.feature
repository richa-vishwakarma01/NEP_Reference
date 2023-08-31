Feature: xfl_integration.feature

  @xfl_integration_Error_wrong_credentials
  Scenario: First import for competition and matches in a season
     Given I do the docker compose for xfl run
     Then Run importData request to import competition with Matcheswith bad user and password
     Then I verify the HTTP response 401

  @xfl_integration_import_data
  Scenario: Importing data for competition and matches
#      Given I do the docker compose for xfl run
      Then Run importData request to import competition with Matches
      Then The response contains the text '"Triggered command to start import of XFL competitions with matches."'
      Then I verify the HTTP response 200
      Then I connect to database
      And I verify external_id where namespace is xfl for table competition
      And I verify primary_external_id where title is FOOTBALL% for table match
      And I verify new records added in Venue,sport_season and team
      Then I verify the Tags


  Scenario: Import update for existing competition with existing matches in season
#      Given I do the docker compose for xfl run
      Then Run importData request to import competition with Matches
      Then The response contains the text '"Triggered command to start import of XFL competitions with matches."'
      Then I verify the Tags
      When a second import is requested (with some updates, here we need to include some changes to have some updates data)
      Then only new data is persisted
      And edited data for existing matches is updated (i.e. update a planned datetime for a match)
      And new tags are created for new/updated data
      And no changes in DB for data that it didnt change in second import
      And no tags created for data that it didnt change