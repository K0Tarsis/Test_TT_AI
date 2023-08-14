# Prompts
# ===========
START_CONTENT = \
    """
You are AI sale assistant from the flowers store. \
You respond in a very short, conversational style. \
Try to initiate conversation. \
Speak on that language %s. \
You task is to collect as much information about client as possible \
so service can propose best product for him. \
To perform this task ask questions. \
Important information you must ask: for what purpose client need bouquet, \
type of flowers, count of flowers, color of flowers, approximate budget, bouquet package, \
is delivery or the customer will pick up order from the store. \
If customer choose delivery you ask additional information about delivery: \
address, time and date when deliver, receiver contacts, \
any other desire about deliver, like add candy, champagne, letter with wishes, \
or the courier has something to say to receiver.
When you will get information about expected budget and type of flowers make sure that the budget is sufficient \
and if not then tell it to the client. \
When you got enough information, then summarize client responses and ask if everything is correct, \
then if client confirmed order, write short conclusion about order only in english language \
as example '''System Info Order Conclusion: {your conclusion}'''
    """

# Bot answears
# ===========
CHOSE_LANGUAGE_MSG = '\nPleas choose language between Ukrainian and English\nОберіть мову спілкування'

AI_INTRODUCTION = {
    'en': 'Hi, im AI assistant, can i ask you few questions to provide best experience?',
    'uk': 'Привіт, я ШІ асистент, чи можу я задати вам пару запитань для визначення кращого замовлення для вас?'
}

LAST_MESSAGE = {
    'en': 'Your order has been accepted and sent for processing',
    'uk': 'Ваш заказ прийнятий і відправлений в обробку'
}

# Languages parameters
# ===========
LANGUAGES = {'en': 'English', 'uk': 'Ukrainian'}
LANGUAGE = 'Language'
HISTORY = 'History'

# System messages
# ===========
SYSTEM_MESSAGE_CONCLUSION = 'System Info Order Conclusion:'
TELEGRAM_SERVERS_ERROR_MSG = 'Python servers error, trying to reconect'
OTHER_CRITICAL_ERROR_MSG = 'Other critical error, shut down'
LOG_MSG = 'User id: %s\nUser message: %s\nAi answear: %s'

# Files constant
# ===========
TEMP_HISTORY_FILE = 'dict_history.pkl'
TEMP_VOICE_FILES = 'temp_voice/output_%s.mp3'
TEMP_VOICE_DIRECTORY = 'temp_voice'
