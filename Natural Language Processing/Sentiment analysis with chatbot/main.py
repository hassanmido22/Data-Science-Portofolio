import bot
import random
import json

if __name__ == '__main__':  # for test
    user_id = random.randint(1, 9999999)
    while True:
        message = input()
        stat, reply = bot.chat(user_id, message)
        reply = json.loads(reply.replace("\'", "\""))
        if stat == 0:
            print(reply["text"])
            print('\n')
        else:
            print('Error')

