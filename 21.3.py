def count_words(file_obj):

    content = file_obj.read()
    words = content.split()
    return len(words)



import pytest
from my_module import count_words

@pytest.fixture
def file_obj_fixture(tmp_path):

    content = "This is a sample text file for testing."
    file_path = tmp_path / "test_file.txt"
    with open(file_path, "w") as file:
        file.write(content)
    
    with open(file_path, "r") as file_obj:
        yield file_obj

def test_count_words(file_obj_fixture):

    result = count_words(file_obj_fixture)
    assert result == 7
