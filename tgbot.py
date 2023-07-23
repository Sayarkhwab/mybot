import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with the token you received from the BotFather
TELEGRAM_BOT_TOKEN = '6229135903:AAGYxHS9eDTScoTCqPJvN32KzCvJ-XhNkG8'

# Replace 'YOUR_API_URL' with the URL of your API
API_URL = 'https://apis.imkaif.me/#/Web%20Scarpers/_gdtot_gdtot_get'

def start(update, context):
    update.message.reply_text('Hello! I am your bot. Send me a message to get started!')

def echo(update, context):
    user_input = update.message.text
    response = get_api_response(user_input)
    update.message.reply_text(response)

def get_api_response(user_input):
    try:
        # Make a request to your API with the user's input
        api_response = requests.get(API_URL, params={'input': user_input})

        # Process the API response
        if api_response.status_code == 200:
            return api_response.json()
        else:
            return "Sorry, there was an error processing your request."

    except requests.RequestException:
        return "Sorry, there was an error connecting to the API."

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Define command handlers
    dp.add_handler(CommandHandler("start", start))

    # Define a message handler to echo user messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
