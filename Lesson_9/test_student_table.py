import pytest
from Student_Table import StudentTable

db_connection_string = ("postgresql://"
                        "postgres:12031010@localhost:5432/QA_Boyarova")


@pytest.fixture(scope="function")
def student_table():
    return StudentTable(db_connection_string)

# возвращает уникальный индентификатор для тестовой записи.
# прибавляет 1 к максимально существующему user_id


@pytest.fixture(scope="function")
def unique_id(student_table):
    max_id = student_table.get_max_id()
    return max_id + 1

# автоматическая отчистка записи перед и после теста


@pytest.fixture(scope="function", autouse=True)
def clean_up(student_table, unique_id):
    student_table.delete(unique_id)
    yield
    student_table.delete(unique_id)

# добавление студента


def test_insert(student_table, unique_id):
    student_table.insert(unique_id)
    students = student_table.get_by_id(unique_id)
    assert len(students) == 1
    assert students[0][0] == unique_id

# изменение уровня


def test_update(student_table, unique_id):
    student_table.insert(unique_id)
    student_table.update(unique_id, "Elementary")
    students = student_table.get_by_id(unique_id)
    assert len(students) == 1
    assert students[0][1] == "Elementary"

# удаление


def test_delete(student_table, unique_id):
    student_table.insert(unique_id)
    student_table.delete(unique_id)
    students = student_table.get_by_id(unique_id)
    assert len(students) == 0
