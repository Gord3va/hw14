from functions import get_actor_from_cast, get_movie_by_type_year_genre


class TestFunctions:

    def test_get_actor_from_cast(self):
        result = get_actor_from_cast('Rose McIver', 'Ben Lamb')
        assert type(result) == list, "Возвращает не список"
        assert len(result) > 0, "Возвращает пустой список"

    def test_get_movie_by_type_year_genre(self):
        result = get_movie_by_type_year_genre('Movie', 2000, 'Horror Movies')
        print(result)
        assert type(result) == str, "Возвращает не строку"
        assert "title" in result
        assert "description" in result
