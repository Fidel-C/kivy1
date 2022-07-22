from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import AnimationTransition,FadeTransition
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class LoginScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def login(self):
        if self.ids.email.text=="admin" and self.ids.password.text=="test":
            self.manager.current="dashboard"
            self.manager.transition=FadeTransition()
            # self.ids.email.text,self.ids.password.text="",""
        else:
            dialog=MDDialog()
            dialog.text=f"{self.ids.email.text} and {self.ids.password.text} not correct"
            dialog.open()

 
 