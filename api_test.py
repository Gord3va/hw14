from app import app


class TestApp:

    def test_page_search(self):
        response = app.test_client().get('/films/title')
        assert response.status_code == 200
        assert type(response.json) == list

    def test_page_range_year(self):
        response = app.test_client().get('/films/2010/to/2011')
        assert response.status_code == 200
        assert type(response.json) == list

    def test_page_children_rating(self):
        response = app.test_client().get('/rating/children')
        assert response.status_code == 200
        assert type(response.json) == list

    def test_page_family_rating(self):
        response = app.test_client().get('/rating/family')
        assert response.status_code == 200
        assert type(response.json) == list

    def test_page_adult_rating(self):
        response = app.test_client().get('/rating/adult')
        assert response.status_code == 200
        assert type(response.json) == list

    def test_page_genre_name(self):
        response = app.test_client().get('/genre/genre')
        assert response.status_code == 200
        assert type(response.json) == list
