from utils import Films
import pytest


@pytest.fixture()
def films():
    films_ = Films()
    return films_


@pytest.fixture()
def query():
    query = f"""
                            SELECT title, country, release_year, listed_in AS genre, description 
                            FROM netflix
                            WHERE title LIKE '%100%'
                            ORDER BY release_year DESC
                            LIMIT 1
        """
    return query


by_title_keys_should_be = {"title", "country", "release_year", "genre", "description"}
get_by_range_keys_should_be = {"title", "release_year"}
get_by_rating_keys_should_be = {"title", "rating", "description"}
get_by_genre_keys_should_be = {"title", "description"}


class TestUtils:

    def test_connection(self, query, films):
        result = films.connection(query)
        assert type(result) == list, "Возвращает не список"
        assert len(result) > 0, "Возвращает пустой список"

    def test_get_by_title(self, films):
        result = films.get_by_title('100')
        assert type(result) == list, "Возвращает не список"
        assert len(result) == 1, "Возвращает не одно значение"
        assert set(result[0].keys()) == by_title_keys_should_be, "Неверный список ключей"

    def test_get_by_range(self, films):
        result = films.get_by_range(2000, 2007)
        assert type(result) == list, "Возвращает не список"
        assert len(result) > 0, "Возвращает пустой список"
        assert set(result[0].keys()) == get_by_range_keys_should_be, "Неверный список ключей"

    def test_get_by_rating(self, films):
        result = films.get_by_rating("'R'")
        assert type(result) == list, "Возвращает не список"
        assert len(result) > 0, "Возвращает пустой список"
        assert set(result[0].keys()) == get_by_rating_keys_should_be, "Неверный список ключей"

    def test_get_by_genre(self, films):
        result = films.get_by_genre("Horror Movies")
        assert type(result) == list, "Возвращает не список"
        assert len(result) > 0, "Возвращает пустой список"
        assert set(result[0].keys()) == get_by_genre_keys_should_be, "Неверный список ключей"
