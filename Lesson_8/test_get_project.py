from api_client import ApiClient
from project_api import ProjectApi


class TestGetProject:
    def test_get_existing_project(self, project_api):
        create_resp, title = project_api.create_unique_project("GetTest")
        project_api.assert_project_created(create_resp)
        project_id = create_resp.json()['id']

        response = project_api.get_project(project_id)
        (project_api.assert_project_retrieved
         (response, expected_id=project_id, expected_title=title))

    # Негативные проверки
    # передаём в URL идентификатор в неверном формате
    def test_get_project_invalid_id(self, project_api):
        response = project_api.get_project("123")
        assert response.status_code in (400, 404)

    # Создаём клиент без токена (пустая строка) и пытаемся получить проект
    def test_get_project_without_auth(self, base_url):
        no_auth_client = ApiClient(base_url, token="")
        no_auth_api = ProjectApi(no_auth_client)
        response = no_auth_api.get_project("some-id")
        no_auth_api.assert_error(response, expected_status=401)
