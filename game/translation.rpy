init -3 python:
    if persistent.lang is None:
        persistent.lang = "russian"


    lang = persistent.lang

init python:
    config.main_menu.insert(3, (u'Language', "language_chooser", "True"))
