# Cowin Notifier Hyderabad

The purpose of this script is to get alerts of vaccine availabilty on slack or teams, which most of us use for office work. So do make use of it to get alerts for availability.
Please note, this doesn't book vaccine on its own, its just a simple notifier based cowin APIs.

Be logged in on cowin website (the session time is around 15 mins, so make sure you have an active session) and after you get the alert, you'll have to select the slot and enter the captcha to book the slot manually.


## Pre-requisites

```sh
- Python3 installed on your machine
- Admin access to a slack workspace (you can create one if you don't have access)
- Or access to a MS Teams Account
```

### How to set up this script

```sh
$ cd cowin-notifier-hyderabad
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python main.py # for slack notification
or
$ python teams.py # for teams notification

# You can run the script in background as well, feel free to refer to this [blog](https://janakiev.com/blog/python-background/) for the same.
```

### Steps for Slack incoming webhook setup

- You need to have admin access to a slack workspace (if not create [one](https://slack.com/intl/en-in/help/articles/206845317-Create-a-Slack-workspace))
- Once you are logged into slack workspace, go to this [URL](https://api.slack.com/messaging/webhooks), follow till 3rd step and copy the webhook URL.
- Replace the copied webhook URL in constants.py for constant ```SLACK_WEBHOOK```

### Steps for Teams incoming webhook setup

- You need to be part of a MS Teams account
- Create a new team and channel inside it
- Navigate to the channel where you want to add the webhook and select (•••) More Options from the top navigation bar
- Choose Connectors from the drop-down menu and search for Incoming Webhook
- Select the Configure button, provide a name, and optionally, upload an image avatar for your webhook
- The dialog window will present a webhook URL, copy it
- Replace the copied webhook URL in constants.py for constant ```TEAMS_WEBHOOK```

Note - As of now, this script get you alerts only for next two consicutive days and only for two cities - Hyderabad &  Rengareddy. Feel free to change the city_ids, city_id information is available [here](https://apisetu.gov.in/public/marketplace/api/cowin).
