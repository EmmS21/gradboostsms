from flask import Flask
from twilio.rest import Client
from datetime import datetime
import time
import random
import urllib.request
app = Flask(__name__)
@app.route("/sms")
def hello():
    account_sid = 'AC963cc6862f5f7a66d4feb7ecf1299c83'
    auth_token = 'b67bcb674aa16f237cee3df199cdbd14'
    client = Client(account_sid,auth_token)
    #time to send messages
    end_time = datetime.strptime("10-06-2020", "%d-%m-%Y")
    list_numbs = ['+15162341744', '+27615304405', '+2347033228906', '+2348129190338', '+2347065094065', '+2348029033427'] #numbers to send sms to
    names = ['Jasmine', 'Vusi', 'Ritmwa', 'Ajibola', 'Benjamin', 'Gershinen'] #name of receipient
    name_num = dict(zip(list_numbs, names))
    file_path = "https://raw.githubusercontent.com/EmmS21/GradientBoostIntrotoDS/master/Challenges/data-programming.txt"
    file = urllib.request.urlopen(file_path)
    full_text = [line.decode("utf-8").replace('\n', '') for line in file]
    while datetime.now() <= end_time:
        for num, name in name_num.items():
            chall = random.choice(full_text)
            client.messages.create(from_="+12058988731",
                                   to="{}".format(num),
                                   body="Hi {}. This is an automated message from The Gradient Boost.  Please complete the challenge, upload to your GitHub repository, name it TheGradientBoostWhatsAppcodingchallengesMay2020 and send us the link on Slack.  Here is your weekly programming challenge:  {}".format(name, ''.join(map(str, chall)))
                                   )
        time.sleep(604800.0 - time.time() % 604800.0)  # rerun function every 7 days

if __name__ == "__main__":
    app.run(debug=True)