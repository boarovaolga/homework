class TestPutProject:
    def test_update_project_title(self, project_api):
        create_resp, original_title = (
            project_api.create_unique_project("Original"))
        project_api.assert_project_created(create_resp)
        project_id = create_resp.json()['id']

        new_title = "Modified Project"
        update_resp = project_api.update_project(project_id, new_title)
        assert update_resp.status_code in (200, 204)

        get_resp = project_api.get_project(project_id)
        (project_api.assert_project_retrieved
         (get_resp, expected_id=project_id, expected_title=new_title))

    # Негативные проверки
    # обновить проект с несуществующим идентификатором
    def test_update_project_not_found(self, project_api):
        response = project_api.update_project("non-existent-id", "New Title")
        project_api.assert_error(response, expected_status=404)

    # передаём в URL некорректный идентификатор
    def test_update_project_invalid_id_format(self, project_api):
        response = project_api.update_project("", "New Title")
        assert response.status_code in (400, 404)
