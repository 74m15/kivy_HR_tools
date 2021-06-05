# -*- coding: utf-8 -*-
"""
Created on Fri Jun 04 19:45:01 2021

@author: CAPUANO-P
"""

from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
#from kivymd.uix.navigationdrawer import (NavigationLayout, MDNavigationDrawer)

class ContentNavigationDrawer(MDBoxLayout):
    nav_drawer = ObjectProperty(None)
    screen_manager = ObjectProperty(None)

class HrApp(MDApp):
    def build(self, *args, **kwargs):
        super(HrApp, self).build(*args, **kwargs)

            
if __name__ == '__main__':
    HrApp().run()