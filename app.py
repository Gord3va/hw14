import json
from flask import Flask
from utils import Films

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

my_film = Films()


@app.route('/films/<title>')
def page_search(title):
    # Фильм по названию
    result = get_by_title(title)
    return app.response_class(
        json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json")


@app.route('/films/<int:first_year>/to/<int:second_year>')
def page_range_year(first_year, second_year):
    # Фильмы в диапазоне лет
    result = get_by_range(first_year, second_year)
    return app.response_class(
        json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json")


@app.route('/rating/children')
def page_children_rating():
    # для детей
    rating = "'G'"
    result = get_by_rating(rating)
    return app.response_class(
        json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json")


@app.route('/rating/family')
def page_family_rating():
    # Фильмы для семьи
    rating = "'G', 'PG', 'PG-13'"
    result = get_by_rating(rating)
    return app.response_class(
        json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json")


@app.route('/rating/adult')
def page_adult_rating():
    # Фильмы для взрослых
    rating = "'R', 'NC-17'"
    result = get_by_rating(rating)
    return app.response_class(
        json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json")


@app.route('/genre/<genre>')
def page_genre_name(genre):
    # Фильмы по жанру
    result = get_by_genre(genre)
    return app.response_class(
        json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json")


if __name__ == "__main__":
    app.run()
