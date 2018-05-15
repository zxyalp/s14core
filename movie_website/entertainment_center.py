# -*- coding: utf-8 -*-
"""
Created on 2018/5/13

@author: xing yan
"""
import media
import fresh_tomatoes
import collections


def create_movie_list(movie_list):
    """Create a movie object list based on the incoming movie list"""

    movies = []

    for movie in movie_list:
        movie_media = media.Movie(movie.pop("title"), movie.pop("poster_image_url"), movie.pop("trailer_url"), **movie)
        movie_media.show_other_info()
        movies.append(movie_media)

    return movies


avengers3 = collections.OrderedDict({"title": "复仇者联盟3：无限战争",
                                     "poster_image_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public"
                                                         "/p2517753454.webp",
                                     "trailer_url": "http://v.youku.com/v_show/id_XMjUwOTY3MjgwMA==.html",
                                     "导演": "东尼·罗素 / 乔·罗素",
                                     "编剧": " 杰克·科比 / 克里斯托弗·马库斯 / 斯蒂芬·麦克菲利 / 吉姆·斯特林",
                                     "语言": "英语",
                                     "上映日期": "2018-05-11(中国大陆)"})

red_sea_initiative = {"title": "红海行动",
                      "poster_image_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2514119443.webp",
                      "trailer_url": "http://v.youku.com/v_show/id_XMzA3NjY1NzkyNA==.html",
                      "导演": "林超贤",
                      "主演": "张译 / 黄景瑜 / 海清 / 杜江 / 蒋璐霞 / 更多...",
                      "类型": "动作 / 战争",
                      "制片国家/地区": "中国大陆 / 香港",
                      "语言": "汉语普通话 / 阿拉伯语 / 英语 / 索马里语 / 粤语",
                      "上映日期": "2018-02-16(中国大陆)",
                      "红海行动的剧情简介": "索马里海域外，中国商船遭遇劫持，船员全数沦为阶下囚。蛟龙突击队沉着应对，潜入商船进行突"
                      "袭，成功解救全部人质。返航途中，非洲北部伊维亚共和国发生政变，恐怖组织连同叛军攻入首都， 当地华侨面临危险，海"
                      "军战舰接到上级命令改变航向，前往执行撤侨任务, 了解更多..."}

megan_leavey = {"title": "战犬瑞克斯",
                "poster_image_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2520197352.webp",
                "trailer_url": "http://v.youku.com/v_show/id_XMjc4NDMxMjIzMg==.html",
                "导演": "加芙列拉·考珀斯维特",
                "编剧": "帕梅拉·格雷 / 安妮·玛莫罗 / 蒂姆·洛夫斯特特",
                "主演": "凯特·玛拉 / 汤姆·费尔顿 / 布莱德利·惠特福德 / 杰拉丁妮·詹姆斯 / 科曼",
                "类型": "剧情 / 传记 / 战争",
                "制片国家/地区": "美国",
                "语言": "英语",
                "上映日期": "2018-05-11(中国大陆) / 2017-05-07(蒙特克莱电影节) / 2017-06-09(美国)",
                "片长": "116分钟"}

ready_player_one = {"title": "头号玩家",
                    "poster_image_url": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2516578307.webp",
                    "trailer_url": "http://v.youku.com/v_show/id_XMjkxNTQwNDc0NA==.html"}

rampage = {"title": "狂暴巨兽",
           "poster_image_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2516079193.webp",
           "trailer_url": "http://v.youku.com/v_show/id_XMzUyMjI1NDU5Ng==.html"}

baahubali2 = {"title": "巴霍巴利王2：终结",
              "poster_image_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2521118750.webp",
              "trailer_url": "http://v.youku.com/v_show/id_XMjc1MzQ5OTg2NA==.html"}

movies_list = [avengers3, red_sea_initiative, megan_leavey, ready_player_one, rampage, baahubali2]

fresh_tomatoes.open_movies_page(create_movie_list(movies_list))
