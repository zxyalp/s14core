# -*- coding: utf-8 -*-
"""
Created on 2018/5/13

@author: xing yan
"""
import webbrowser


class Movie(object):
    """Create movie information."""

    def __init__(self, movie_title, poster_image_url, trailer_url, **kwargs):
        """kwargs include director, screenwriter, starring, language, release time, story introduction, etc. """
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_url = trailer_url
        self.movie_other_info = kwargs

    def show_trailer(self):
        webbrowser.open(self.trailer_url)

