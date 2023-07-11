import pytest, random, names
from py_hw_1.human import Human


@pytest.fixture()
def create_human():
    random_age = random.randint(1, 105)
    random_full_name = names.get_full_name()
    random_gender = random.choice(['male', 'female'])
    my_human = Human(random_full_name, random_age, random_gender)
    return my_human


@pytest.fixture()
def create_bob():
    bob = Human(name='Bob Doe', age=30, gender='male')
    return bob


@pytest.fixture()
def create_sam():
    sam = Human(name='Sam Old', age=100, gender='male')
    return sam
