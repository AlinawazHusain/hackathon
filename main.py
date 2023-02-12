import pymongo
from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.label import Label



client=pymongo.MongoClient("mongodb://localhost:27017")
db=client['UserData']
collection=db['Users']
class LibraryApp(MDApp):

    def build(self):
        mainbox=BoxLayout(orientation="vertical", spacing=20,padding=(40,10,40,100))
        self.books=MDTextField(hint_text="Enter book name", helper_text="Enter proper name", helper_text_mode="on_focus")
        self.number=MDTextField(hint_text="Enter quantity ", helper_text="Enter exact number of books", helper_text_mode="on_focus")
        self.price=MDTextField(hint_text="Enter price of single book", helper_text="Enter roundoff price", helper_text_mode="on_focus")
        mainbox.add_widget(self.books)
        mainbox.add_widget(self.number)
        mainbox.add_widget(self.price)

        save=MDFillRoundFlatButton(text="save",pos_hint={'center_x':0.5},on_press=self.saving)
        mainbox.add_widget(save)

        view=MDFillRoundFlatButton(text="show data",pos_hint={'center_x':0.5},on_press=self.viewing)
        mainbox.add_widget(view)

        self.label=Label(text="")
        mainbox.add_widget(self.label)




        return mainbox
    


    




    def saving(self,save):
        books=self.books.text
        quantity=self.number.text
        quantity=int(quantity)
        price=self.price.text
        price=int(price)
        totalPrice=quantity*price
        all={'BookName':books,'Quantity':quantity, 'PriceOf1Book':price, 'TotalCost':totalPrice}
        collection.insert_one(all)
        self.books.text=""
        self.number.text=""
        self.price.text=""


    def viewing(self,view):
        for x in collection.find():
            self.label.text=self.label.text + x

    



LibraryApp().run()