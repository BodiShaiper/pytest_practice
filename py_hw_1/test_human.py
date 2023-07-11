import pytest
from py_hw_1.human import Human


def test_human_initialization(create_bob):
    human = create_bob
    assert human.age == 30, 'Human age is incorrect'
    assert human.gender == "male", 'Human is not male'


def test_human_grow(create_bob):
    human = create_bob
    human_age_before_grow = create_bob.age
    human.grow()
    assert human.age == human_age_before_grow + 1, 'grow() function works incorrectly'


def test_human_grow_past_age_limit(create_sam):
    human = create_sam
    human.grow()
    assert human.age == 100, 'Sam is dead'
    assert human._Human__status == "dead"


def test_human_change_gender(create_sam):
    human = create_sam
    human.change_gender("female")
    assert human.gender == "female"


def test_human_change_gender_to_same_gender(create_bob):
    human = create_bob
    with pytest.raises(Exception):
        human.change_gender("male"), "The gender is the same, we can't change it"


def test_human_change_gender_invalid_gender(create_human):
    human = create_human
    with pytest.raises(Exception):
        human.change_gender("unknown"), "There is no such a gender. Gender validation works fine"


def test_human_change_name(create_human):
    human = create_human
    new_name = "Will Smith"
    human.name = new_name
    assert human.name == new_name, "The new name is not saved properly."


def test_human_is_alive(create_human):
    human = create_human
    assert human._Human__is_alive() == True, f"This human age is {human.age}, he's dead {human.age - 100} years ago."


def test_human_is_dead(create_human):
    human = create_human
    human._Human__status = "dead"
    with pytest.raises(Exception):
        human._Human__is_alive(), "Error. This human is actually not dead"


def test_human_validate_gender_invalid_gender(create_human):
    with pytest.raises(Exception):
        Human._Human__validate_gender("unknown")
