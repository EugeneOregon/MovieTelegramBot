from keyboards.inline.choice_buttons import new_post
from loader import db
from models.movie_link import Movie
from models.parser import Parser


class Check:
    def __init__(self):
        self.movie_url = None
        self.movie_poster_title = None
        self.all_movies_db = None
        self.movies = None
        self.parser = Parser()
        self.movie = Movie()

    async def get_link_movie(self, url):
        self.movie_url = self.movie.get_movie(url)

    async def check_movie_in_db(self):
        await self.parser.parse()
        self.movies = self.parser.movies
        for movie in self.movies:
            response_check = await db.select_film(link=movie['link'])
            if response_check is None:
                await self.parser.parse(movie['link'])
                self.movie_poster_title = self.parser.movie_update
                await self.get_link_movie(movie['link'])
                await db.add_film(movie['link'], self.movie_poster_title[0]['title'], self.movie_url,
                                  self.movie_poster_title[0]['poster'])

                await new_post(movie['link'])
