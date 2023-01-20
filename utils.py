import sqlite3

class Films:
    def connection(query: str) -> list[dict]:
        """
        получает результат список словатей с фильмами
        """
        with sqlite3.connect('netflix.db') as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            result_list = []
            for title in result:
                res_dict = dict(title)
                result_list.append(res_dict)
            return result_list


    def get_by_title(title: str) -> list[dict]:
        """
        самый свежий фильм по названию
        """
        query = f"""
                            SELECT title, country, release_year, listed_in AS genre, description 
                            FROM netflix
                            WHERE title LIKE '%{title}%'
                            ORDER BY release_year DESC
                            LIMIT 1
        """
        result = connection(query)
        return result


    def get_by_range(first_year: int, second_year: int) -> list[dict]:
        """
        Возвращает фильмы за период
        """
        query = f"""
                        SELECT title, release_year
                        FROM netflix
                        WHERE release_year BETWEEN {first_year} AND {second_year}
                        LIMIT 100
        """
        result = connection(query)
        return result


    def get_by_rating(rating: str) -> list[dict]:
        """
        фильмы по рейтингу
        """
        query = f"""
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating != ''
                    AND rating IN ({rating})
        """
        result = connection(query)
        return result


    def get_by_genre(genre: str) -> list[dict]:
        """
        10 самых свежих фильмов в жанре
        """
        querty = f"""
                    SELECT title, description
                    FROM netflix
                    WHERE listed_in LIKE '%{genre}%'
                    ORDER BY release_year DESC
                    LIMIT 10
        """
        result = connection(querty)
        return result




