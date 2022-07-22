import json,os
from kivy.core.window import Window
from kivy.network.urlrequest import UrlRequest
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory
Window.size=(360,640)



class MainApp(App,MDApp):
   
    CLASSES={
    "Manager":"classes.manager",
    "LoginScreen":"classes.login",
    "Dashboard":"classes.dashboard",
    "PostDetail":"classes.post_detail"
   }

    KV_FILES={'screens/manager.kv','screens/login.kv','screens/dashboard.kv','screens/post_detail.kv'}
    AUTORELOADER_PATHS=[(".",{'recursive':True})]
    search_url='https://jsonplaceholder.typicode.com/posts'
    
    def build_app(self):


        return Factory.Manager()

    def on_start(self):


        return super().on_start()        
            
            
if __name__=="__main__":
    MainApp().run()


