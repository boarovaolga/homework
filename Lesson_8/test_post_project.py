class TestPostProject:
    def test_create_project_valid_title(self, project_api):
        title = "New Project"
        response = project_api.create_project(title)
        project_api.assert_project_created(response, expected_title=title)

# Негативная проверка
    def test_create_project_no_title(self, project_api):
        response = project_api.client.post('/api-v2/projects', json={})
        project_api.assert_error(response, expected_status=400)