# -*- coding: utf-8 -*-
"""
Created on 2018/5/13

@author: xing yan
"""
import media
import fresh_tomatoes


def create_movie_list(movie_list):
    """Create a movie object list based on the incoming movie list"""

    movies = []

    for movie in movie_list:
        print(movie.get("title"), movie.get("poster_image_url"), movie.get("trailer_url"))
        movie_media = media.Movie(movie.get("title"), movie.get("poster_image_url"), movie.get("trailer_url"))
        movies.append(movie_media)

    return movies


avengers3 = {"title": "复仇者联盟3：无限战争",
             "poster_image_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2517753454.webp",
             "trailer_url": "http://v.youku.com/v_show/id_XMjUwOTY3MjgwMA==.html",
             "language": "英语",
             "release_date": "2018-05-11(中国大陆)",
             "director": "东尼·罗素 / 乔·罗素",
             "screenwriter": " 杰克·科比 / 克里斯托弗·马库斯 / 斯蒂芬·麦克菲利 / 吉姆·斯特林"}

red_sea_initiative = {"title": "红海行动",
                      "poster_image_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2514119443.webp",
                      "trailer_url": "http://v.youku.com/v_show/id_XMjUwOTY3MjgwMA==.html"}

megan_leavey = {"title": "战犬瑞克斯",
                "poster_image_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2520197352.webp",
                "trailer_url": "http://v.youku.com/v_show/id_XMjUwOTY3MjgwMA==.html"}

ready_player_one = {"title": "头号玩家",
                    "poster_image_url": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2516578307.webp",
                    "trailer_url": "http://v.youku.com/v_show/id_XMjUwOTY3MjgwMA==.html"}

rampage = {"title": "狂暴巨兽",
           "poster_image_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2516079193.webp",
           "trailer_url": "http://v.youku.com/v_show/id_XMjUwOTY3MjgwMA==.html"}

baahubali2 = {"title": "巴霍巴利王2：终结",
              "poster_image_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2521118750.webp",
              "trailer_url": "http://v.youku.com/v_show/id_XMjUwOTY3MjgwMA==.html"}

movies_list = [avengers3, red_sea_initiative, megan_leavey, ready_player_one, rampage, baahubali2]

fresh_tomatoes.open_movies_page(create_movie_list(movies_list))
