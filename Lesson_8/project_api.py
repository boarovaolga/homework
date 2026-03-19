import time

class ProjectApi:
    def __init__(self, client):
        self.client = client

    # Методы действий
    def create_project(self, title):
        return self.client.post('/api-v2/projects', json={'title': title})

    def update_project(self, project_id, title):
        return self.client.put(f'/api-v2/projects/{project_id}', json={'title': title})

    def get_project(self, project_id):
        return self.client.get(f'/api-v2/projects/{project_id}')

    def create_unique_project(self, prefix="Test"):
        unique_title = f"{prefix}_{int(time.time())}"
        resp = self.create_project(unique_title)
        return resp, unique_title

    # Методы проверки
    def assert_project_created(self, response, expected_title=None):
        assert response.status_code == 201, f"Ожидался 201, получен {response.status_code}"
        data = response.json()
        assert 'id' in data, "Ответ не содержит id проекта"

    def assert_project_retrieved(self, response,
                                 expected_id=None, expected_title=None):
        assert response.status_code == 200, \
            f"Ожидался 200, получен {response.status_code}"
        data = response.json()
        assert 'id' in data, "Ответ не содержит id"
        assert 'title' in data, "Ответ не содержит title"
        if expected_id:
            assert data['id'] == expected_id,\
                f"Ожидался id {expected_id}, получен {data['id']}"
        if expected_title:
            assert data['title'] == expected_title,\
                f"Ожидался title '{expected_title}', получен '{data['title']}'"

    def assert_project_updated(self, response, expected_title=None):
        assert response.status_code in (200, 204),\
            f"Ожидался 200/204, получен {response.status_code}"
        if response.status_code == 200 and expected_title:
            data = response.json()
            assert data.get('title') == expected_title

    def assert_error(self, response, expected_status):
        assert response.status_code == expected_status,\
            f"Ожидался {expected_status}, получен {response.status_code}"