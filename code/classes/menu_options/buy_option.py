"""This module houses the BuyOption class."""
from classes.menu_classes.menu import Menu

class BuyOption(Menu):
    """Menu class for the purchase option on Products."""
    def __init__(self, name, description, account, database_manager, return_menu):
        self.database_manager = database_manager
        self.return_menu = return_menu
        self.user_data = None
        super().__init__(name, description, account)

    def start(self):
        """Called when drawing the menu, checks if payment information
        is available and allows purchase if it is."""
        #Verify card data:
        self.user_data = self.database_manager.is_username_taken(self.account.username)
        if self.user_data["Card_Details"] == "":
            print("No card data on this account. Please go to account settings to add your card details.")
        else:
            print("Product successfully purchased.")
        self.return_menu.start()
