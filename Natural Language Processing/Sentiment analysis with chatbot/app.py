from flask import Flask, request, jsonify
import bot

app = Flask(__name__)


@app.route('/message', methods=['POST'])
def message():
    if request.method == "POST":
        request_data = request.get_json()
        if "message" in request_data.keys() and "user_id" in request_data.keys():
            message = request_data['message']
            response = {}
            if message:
                state, reply = bot.chat(request_data['user_id'], message.lower())
                if state == 0:
                    response["reply"] = reply
                    response["status"] = 'Success'

                    return jsonify(response), 200
                elif state == -1:
                    response["reply"] = "there is no response"
                    response['status'] = "Failed"

                    return jsonify(response), 400
            else:
                response["reply"] = "there is no message"
                response['status'] = "Failed"

                return jsonify(response), 400

            return jsonify(response)
        else:
            return jsonify({"message": "request is not correct"}), 400


if __name__ == "__main__":
    app.run()
