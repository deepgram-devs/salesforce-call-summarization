from datetime import datetime, timedelta

from deepgram import Deepgram
from simple_salesforce import Salesforce

DEEPGRAM_API_KEY = "<YOUR_DEEPGRAM_API_KEY>"
EMAIL = "<YOUR_SALESFORCE_EMAIL>"
PASSWORD = "<YOUR_SALESFORCE_PASSWORD>"
SECURITY_TOKEN = "<YOUR_SALESFORCE_SECURITY_TOKEN>"

ACCOUNT_NAME = "Deepgram"
CALL_URL = "https://static.deepgram.com/examples/nasa-spacewalk-interview.wav"

def summarize(deepgram_client, call_url):
    """Use Deepgram to summarize the call at the URL provided."""
    response = deepgram_client.transcription.sync_prerecorded({"url": call_url}, {"summarize": "v2"})
    summary = response["results"]["summary"]["short"]
    print("Generated call summary:", summary)
    return summary

def update_salesforce(salesforce_client, account_name, summary):
    """Given an account name and call summary, add a Salesforce call event to the account and its latest opportunity."""

    # First, get account ID given account name
    query = f"SELECT Id FROM Account WHERE Name = '{account_name}'"
    results = salesforce_client.query(query)["records"]
    if results:
        account = results[0]
        account_id = account.get("Id", None)
        print(f"Account {account_name} has ID {account_id}")

        # Then get the latest opportunity on the account
        query = f"SELECT Name, Id FROM Opportunity WHERE AccountId = '{account_id}'"
        results = salesforce_client.query(query)["records"]
        if results:
            latest_opportunity = results[-1]
            opp_name = latest_opportunity.get("Name", None)
            opp_id = latest_opportunity.get("Id", None)
            print(f"Opportunity name '{opp_name}' has ID {opp_id}")

            # Finally, log a new call event to the account and opportunity, with the Deepgram call summary and today's date
            call_datetime = (datetime.utcnow() - timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%S.%f%z")
            response = salesforce_client.Event.create({
                "Subject": "Call",
                "Description": summary,
                "DurationInMinutes": 60,
                "ActivityDateTime": call_datetime,
                "WhatId": account_id,
                "WhatId": opp_id
            })
            print("Salesforce result:", response)
            print("Wrote call event with ID:", response["id"])

def main():

    deepgram_client = Deepgram(DEEPGRAM_API_KEY)

    salesforce_client = Salesforce(
        username=EMAIL, 
        password=PASSWORD,
        security_token=SECURITY_TOKEN
    )

    summary = summarize(deepgram_client, CALL_URL)

    if summary:
        update_salesforce(salesforce_client, ACCOUNT_NAME, summary)

    print("Finished processing the call.")

if __name__ == "__main__":
    main()
