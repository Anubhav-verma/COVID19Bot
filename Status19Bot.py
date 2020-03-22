from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
import Covid19_data
from robot.api import logger
import logging

# For Logging activities
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Creates updater
updater = Updater(token='1121867431:AAE9V-59SvNLuLayEA7SqWnNISit-acWBTs', use_context=True)

# introducing dispatcher
dispatcher = updater.dispatcher


def start(update, context):
    # Sends text message
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm your bot, please talk to me! Anubhav")


def echo(update, context):
    # echos the given message
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


# def inline_caps(update, context):
#     # Changes user's text into Upper Case letters
#     query = update.inline_query.query
#     if not query:
#         return
#     results = list()
#     results.append(
#         InlineQueryResultArticle(
#             id=query.upper(),
#             title='Caps',
#             input_message_content=InputTextMessageContent(query.upper())
#         )
#     )
#     context.bot.answer_inline_query(update.inline_query.id, results)


# def current_status(update, context):
#     # Gives Current Number of total cases to the user
#     query = Covid19_data.get_total_cases_count()
#     logger.console(query)
#     query = update.inline_query.query
#     if not query:
#         return
#     results = list()
#     results.append(
#         InlineQueryResultArticle(
#             id=query.upper(),
#             title='Total cases in India',
#             input_message_content=InputTextMessageContent(query)
#         )
#     )
#     context.bot.answer_inline_query(update.inline_query.id, results)


def give_total_cases(update, context):
    # returns the current number of cases in india
    if update.message.text == "current status":
        total_cases = Covid19_data.get_total_cases_count()
        update.message.text = total_cases
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


start_handler = CommandHandler('start', start)  # Loads start command's functionality
dispatcher.add_handler(start_handler)  # Dispatches the command

echo_handler = MessageHandler(Filters.text, give_total_cases)  # Loads user's message
dispatcher.add_handler(echo_handler)    # Dispatches the message

# inline_caps_handler = InlineQueryHandler(current_status)
# dispatcher.add_handler(inline_caps_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()  # Starts fetching commands from user
