# -*- coding: utf-8 -*-
"""
Created on 2018/5/13

@author: xing yan
"""
import webbrowser


class Movie(object):
    """Create movie information."""

    def __init__(self, movie_title, poster_image, trailer, **kwargs):
        """kwargs include director, screenwriter, starring, language, release time, story introduction, etc. """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_url = trailer
        self.movie_other_info = kwargs

    def show_trailer(self):
        webbrowser.open(self.trailer_url)

    def show_other_info(self):
        movie_other_info = ''
        other_content = '<span >{key}:</span>{value}</br>'
        for key, value in self.movie_other_info.items():
            movie_other_info += other_content.format(key=key, value=value)
        return movie_other_info
