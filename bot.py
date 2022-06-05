from asyncore import write
from concurrent.futures import thread
from warnings import filters
from telegram import Update
from telegram.ext.updater import Updater
from telegram.update import Update 
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import threading

updater= Updater("5585865275:AAG699JkfXaM4WMhH07F5qKjh982RvhqPK8",
 use_context= 'True')
while True:
    def main():
    
        #print(count)
        #count+=1
        def start(update: Update,context: CallbackContext ):
            update.message.reply_text("""Welcome to dayatva's Bot, we heartly Welcomes You :)
            Click  /help to know for available commands"""
            )
        
        def help(update: Update, context: CallbackContext):
            update.message.reply_text("""Available Commands:-
                   /Founders
                   /members
                   /past_members
                   /official_website
                   /youtube
                   /instagram
                   /LinkedIn
                   /facebook
                   /twitter
                   """
            )
        
        def Youtube(update: Update, context: CallbackContext):
            update.message.reply_text('https://www.youtube.com/c/DayatvaASocialInitiative')
        
        def Instagram(update: Update, context: CallbackContext):
            update.message.reply_text('https://www.instagram.com/dayatva_iitram/')
        
        def website(update: Update, context: CallbackContext):
            update.message.reply_text('https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi-_cHnwI_4AhVMxTgGHW-kAtwQFnoECAsQAQ&url=http%3A%2F%2Fdayatva.iitram.in%2F&usg=AOvVaw0v1EQ3ztiMCvMYJnWawmVD')
            
        def Founders(update: Update, context: CallbackContext):
            update.message.reply_text("""Dayatva's Foundation Stone was graved by :
                 *Mukul Jangid
                 *Chirag rawat
                 *Manish Kumar
                 *Amir Miya      
            """)
        
        def members(update: Update, context: CallbackContext):
            update.message.reply_text("""Chanakyas of Dayatva :
                 *Akash Solanki
                 *Animesh Rathi
                 *Divyash Kumbhani
                 *Ipsita Sengupta
                 *Jay Bhavsar
                 *Manan Shah
        
            The Dhronacharya's:-
                 *Abhishek Mehta
                 *Anurag Tripathi
                 *Dhanvi Mengar
                 *Harshini Kolte
                 *Manu Singh
                 *Meet Parmer
                 *Mohit Wanjare
                 *Mudra Patel
                 *Pushpender Singh
                 *Rakesh Gupta
                 *Siddhant Naik
        
            The Arjuna's :-
                 *Abhishek Kumar
                 *Maitri Kiran
                 *Munish Kumar
                 *Saket Tripathi
                 
            The Abhimanyu's:-
                 *Antara tandon
                 *Mayank Vyas
                 *Garv Anand 
                 *Raj Chetia
                 *Saransh Jaiswal
                 *Md. Saad
                 *Nidhi 
                 *Akash
                 *Karan Modi
                 *Yash Dhariwal
                 *Kunj Patel
                 *Naman Shah
                 *Mohan Krishna
                 *Savan 
                 *Kartik
                 *Dhaval Mehta 
        
        
                      
            """)
        
        def past_members(update: Update, context: CallbackContext):
            update.message.reply_text("""Past Members :
                 *Divyansh Anand
                 *Prince Kumar
                 *Harsh Lodhi
                 *Rishita
                 *Malhar Solanki
                 *G Khsitij
                 *Tathya Bhatt
                 *Jash Rana       
            """)
        
        
        
        def LinkedIn(update: Update, context: CallbackContext):
            update.message.reply_text('https://in.linkedin.com/company/dayatvaiitram?original_referer=https%3A%2F%2Fwww.google.com%2F')
        
        def FaceBook(update: Update, context: CallbackContext):
            update.message.reply_text('https://www.facebook.com/DayatvaIITRAM/')
        
        def twitter(update: Update, context: CallbackContext):
            update.message.reply_text('https://mobile.twitter.com/dayatva')
        
        def unknown_text(update: Updater, context: CallbackContext):
            update.message.reply_text("Sorry we Can't Recognise You :('%s'"% update.message.text)
        
        def unknown(update: Updater, context: CallbackContext):
            update.message.reply_text("Sorry'%s' is not a valid Command"% update.message.text)
        
        updater.dispatcher.add_handler(CommandHandler('start', start))
        updater.dispatcher.add_handler(CommandHandler('instagram', Instagram))
        updater.dispatcher.add_handler(CommandHandler('youtube', Youtube))
        updater.dispatcher.add_handler(CommandHandler('official_website', website))    
        updater.dispatcher.add_handler(CommandHandler('founders', Founders))
        updater.dispatcher.add_handler(CommandHandler('members', members))
        updater.dispatcher.add_handler(CommandHandler('past_members',past_members ))
        updater.dispatcher.add_handler(CommandHandler('help', help))
        updater.dispatcher.add_handler(CommandHandler('LinkedIn', LinkedIn))
        updater.dispatcher.add_handler(CommandHandler('facebook', FaceBook))
        updater.dispatcher.add_handler(CommandHandler('twitter', twitter))
        updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
        updater.dispatcher.add_handler(MessageHandler(
            Filters.command, unknown))
        updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
        
        
        updater.start_polling()
    
    x= threading.Thread(target= main, daemon=True)
    x.start()    