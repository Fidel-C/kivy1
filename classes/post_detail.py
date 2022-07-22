from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
class PostDetail(MDScreen):
  def __init__(self, **kw):
      super().__init__(**kw)






class ProductCard(MDCard):
  card_title=StringProperty()
  card_subtitle=StringProperty()
 
 