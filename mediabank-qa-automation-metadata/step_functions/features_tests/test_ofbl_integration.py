from pytest_bdd import scenario, given, when, then


@scenario('../../features/ofbl_integration.feature', 'First import for competition and matches in a season')
def test_ofbl_integration_import_data():
    pass

@scenario('../../features/ofbl_integration.feature',
          'Import update for existing competition with existing matches in season')
def test_ofbl_integration_updated_data():
    pass
