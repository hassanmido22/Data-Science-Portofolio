import random
import pandas as pd
import sentmint_analysis


def model(text):
    return sentmint_analysis.LR(text), sentmint_analysis.DT(text)


answers = {
    "welcome":
        [
            "hi, my name is Mimo. How can I help you? do you want to ask about something or make a complain?",
            "hello, Mimo is here fo you. do you want to ask about something or make a complain?"
        ],
    "complain":
        [
            "Sorry for that, please write your complain (one complain in one message).",
            "Oh, I am sorry for hearing that, please tell me your complain blow (one complain in one message)."
        ],
    "complain_received":
        [
            "Your complain is received please take a rest and we will contact you soon. Do you want anything else?",
            "Your complain in our hands now, don't worry we will contact you soon. Any other thing I can help you with?"
        ],
    "thanks_response":
        [
            "Glad to help you. could you please write your opinion in this service?",
            "It is my pleasure sure. could you please give me your opinion in this new chat-bot?"
        ],
    "asking":
        [
            "Ask about any thing you want.",
            "Sure, what is your question?"
        ],
    "asking_received":
        [
            "Okay, we will send you the answer in your mail now. Do you want anything else?",
            "Few seconds and the answer will be in your mail box. Any other thing I can help you with?",
            "Answer in on its way to your mail box. Do you want anything else?"
        ]
}


def get_answer(key):
    try:
        return answers[key][random.randint(0, len(answers[key]) - 1)]
    except:
        return key


def create_answer(text_key, buttons):
    j_buttons = []
    for button in buttons:
        data_value = button.split('=')
        j_buttons.append({"text": data_value[0], "value": data_value[1]})

    my_json = {
            "text": get_answer(text_key),
            "button": j_buttons
        }
    return my_json


file_path = "costumer_review.csv"


def add_review(user_id, text):
    lr, dt = model(text)
    res_df = {'user_id': user_id, 'text': text, 'Linear_regression_review': lr, 'Decision_tree_review': dt}
    try:
        df = pd.read_csv(file_path)
        df = df.append(res_df, ignore_index=True)
    except:
        df = pd.DataFrame({'user_id': [user_id], 'text': [text], 'Linear_regression_review': [lr], 'Decision_tree_review': [dt]})
    df.to_csv(file_path)
    return create_answer("Thank you so much", [])
