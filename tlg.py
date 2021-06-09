# runs a setup function which gives us the sensitive information (this file should not be committed to git)
#this function runs when the bot boots up 
#uses Bot to get incoming messages, uses user_manager to send each message to the requested user 


from telegram import Bot, update 

from manager import user_manager

from setup import setter



token = setter()




users = user_manager()

bot = Bot(token)

def main():
    current_offset = 0 #marks which message we're up to 
    while True:#forever check updates 
        print ("on another loop")
        updates = bot.getUpdates(offset=current_offset)
        if len(updates) > 0:
            for update in updates:
                if True:    #debugging mode, usually keep as try
                    print(update)
            current_offset += update.update_id + 1


if __name__ == '__main__':
    main()
