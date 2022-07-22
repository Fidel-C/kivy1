from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import FadeTransition
from kivymd.uix.list import OneLineListItem,ThreeLineListItem,MDList
from kivymd.uix.spinner import MDSpinner
from functools import partial
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty,ListProperty,ObjectProperty,NumericProperty
from kivy.uix.recycleview import RecycleView
from kivymd.app import App
from kivy.uix.image import AsyncImage
import webbrowser



class Dashboard(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)

    products=ListProperty()
    cart=ListProperty()

    

    def logout(self):
        self.manager.current="login"
        self.manager.transition=FadeTransition()


    url="https://jsonplaceholder.typicode.com/posts/"

    

    def on_pre_enter(self, *args):
        super().on_pre_enter(*args)
        return self.get_all_posts()


    def get_all_posts(self):
        req=UrlRequest(self.url,on_success=self.get_json,on_error=self.get_error)


    def get_detail(self,*args):
        req=UrlRequest(f"{self.url}/{args[0]}",on_success=self.get_one_json,on_error=self.get_error)



    def get_json(self, req,res):
        self.ids.rv.data=[{"prod_title":item["title"],"prod_id":item["id"]} for item in res]

    def get_error(self,*args):
        dialog=MDDialog()
        dialog.add_widget(MDLabel(text=str(args[1]),halign="center"))
        dialog.open()

    def show_cart(self):
        # container=MDList()
        for item in range(10):
            self.ids.box.add_widget(CartItem(title=f"item {item}",text="jgkkh"))
            # self.ids.box.add_widget(container)
            
            

        # dialog.title="Cart" 
        # dialog.buttons=cards
        # dialog.open()
        # webbrowser.open("https://mobiledata.com.ng")
        



class CartItem(ThreeLineListItem):
    title=StringProperty()
    # qty=NumericProperty()
    # id=NumericProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

   
          

       






class RV(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        
 
    
class ProductCard(MDCard):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    url="https://jsonplaceholder.typicode.com/posts/"
    prod_title=StringProperty()
    prod_url=StringProperty()
    prod_id=NumericProperty()


    def add_to_cart(self,prod_id):
        cart=self.parent.parent.parent.parent.cart
        cart_item={"id":prod_id,
        "title":self.prod_title,"url":self.prod_url,"qty":1}
        if cart_item in cart:
            cart_item["qty"]+=1
        else:
            cart.append(cart_item)
        

    def get_detail(self,prod_id):
        req=UrlRequest(f"{self.url}/{prod_id}",on_success=self.get_one_json,on_error=self.get_error)

    def get_one_json(self, req,res):
        print(res)
        dialog=MDDialog()
        dialog.add_widget(MDLabel(text=str(res["title"]),halign="center"))
        dialog.open()
    
    def get_error(self,*args):
        dialog=MDDialog()
        dialog.add_widget(MDLabel(text=str(args[1]),halign="center"))
        dialog.open()

    