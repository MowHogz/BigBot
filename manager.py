#
#this bot should have a dictionary of all the users {chat_id:user} with user class 
#should have a function add_user and a function of exists (or does_exist) which checks if a specific user exists in our database, in later stages we can also check from an actual database (and not just a dictionary)
#to_admin function which sends a function to admin using the .send function of the admins object
class user_manager:
    def __init__(self,admin_bot = False):
        pass