import datetime
import time

import requests
from fake_useragent import UserAgent
from slack_sdk.webhook import WebhookClient

from constants import SLACK_WEBHOOK, URL_city, NUM_OF_DAYS

temp_user_agent = UserAgent()
browser_header = {"User-Agent": temp_user_agent.random}

city_ids = {581: "Hyderabad", 603: "Rengareddy"}

base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(NUM_OF_DAYS)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]


def send_slack_message(message):
    url = SLACK_WEBHOOK
    webhook = WebhookClient(url)
    response = webhook.send(text=message)
    assert response.status_code == 200


def main_func():
    while True:
        for inp_date in date_str[1:]:
            for city_id, city_name in city_ids.items():
                print("Check in {} "
                      "for date -------------------------> "
                      "{}".format(city_name, inp_date))
                url = URL_city.format(city_id, inp_date)
                response = requests.get(url, headers=browser_header)
                if response.ok:
                    resp_json = response.json()
                    if resp_json["centers"]:
                        print(" ---> Available on: {}".format(inp_date))
                        for center in resp_json["centers"]:
                            center_name = center["name"]
                            for session in center["sessions"]:
                                if (
                                        session["min_age_limit"] == 18
                                        and session["available_capacity_dose1"] > 1
                                ):
                                    now = datetime.datetime.now()
                                    current_time = now.strftime("%H:%M:%S")
                                    availability = f"{current_time}: " \
                                                   f"Vaccine Available at {center_name}, " \
                                                   f"pincode - {center['pincode']}, " \
                                                   f"quantity - {session['available_capacity_dose1']}"
                                    send_slack_message(availability)
                                    print(availability)
                                else:
                                    print(
                                        f" ---> Center {center_name} "
                                        f"is running but no slots for Dose1"
                                    )
                    else:
                        print(" ---> No available slots on "
                              "{}".format(inp_date))
                time.sleep(3)
            time.sleep(10)


if __name__ == "__main__":
    main_func()
