Feature: ofbl_integration.feature

  @ofbl_integration_import_data
  Scenario: First import for competition and matches in a season
    Given I do the docker compose for ofbl run
    Then I import the data
    And I verify the HTTP response 200
    And The response contains the text 'OK'
    Then I connect to database
    And I verify external_id where name is BL1 for table competition
    And I verify primary_external_id where title is BL1-GD% for table match
    And I verify new records added in Venue,sport_season and team
    Then I verify the Tags
#    And I verify docker message for tags-integrations


  @ofbl_updateData
  Scenario: Import update for existing competition with existing matches in season
    Given I do the docker compose for ofbl run
    Then I import the data
    And I verify the HTTP response 200
    And The response contains the text 'OK'
    Then I connect to database
    And I verify external_id where name is BL1 for table competition
    And I verify primary_external_id where title is BL1-GD% for table match
    And I verify new records added in Venue,sport_season and team
    Then I verify the Tags
    When A second import is requested with updated Data
#    Then Only new data is persisted
#    And Edited data for existing matches is updated (i.e. update a planned datetime for a match)
#    And new tags are created for new/updated data
#    And no changes in DB for data that it didnt change in second import
#    And no tags created for data that it didnt change




