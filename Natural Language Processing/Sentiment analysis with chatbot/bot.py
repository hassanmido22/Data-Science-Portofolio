from rivescript import RiveScript
import os

dirname = os.path.dirname(__file__)
brain_path = os.path.join(dirname, 'brain')

bot = RiveScript(utf8=True)
bot.load_directory(brain_path)
bot.sort_replies()


def chat(user_id, message):
    if message == '':
        return 0, "No Message to response"
    else:
        response = bot.reply(str(user_id), message)
    if response == "":
        return -1, "No Message to response"
    return 0, response
