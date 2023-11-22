# Salesforce Call Summarization

Summarize sales calls using Deepgram, and log the call summaries on a Salesforce opportunity and account.

See the related blog post for a full walk-through: [TODO](www.deepgram.com)

## Install requirements

```
pip install -r requirements.txt
```

## Run

1. Fill in your credentials on lines 7-10:

```
DEEPGRAM_API_KEY = "<YOUR_DEEPGRAM_API_KEY>"
EMAIL = "<YOUR_SALESFORCE_EMAIL>"
PASSWORD = "<YOUR_SALESFORCE_PASSWORD>"
SECURITY_TOKEN = "<YOUR_SALESFORCE_SECURITY_TOKEN>"
```

2. Optionally, edit the Salesforce account name and the audio URL on lines 12-13:

```
ACCOUNT_NAME = "Deepgram"
CALL_URL = "https://static.deepgram.com/examples/nasa-spacewalk-interview.wav"
```

3. Run from the command line:

```
python summarize_and_log_calls.py
```

4. Output from a successful run is as follows:

```
Generated call summary: <summary>
Account Deepgram has ID <id>
Opportunity name '<opp name>' has ID <id>
Salesforce result: OrderedDict([('id', '<id>'), ('success', True), ('errors', [])])
Wrote call event with ID: <id>
Finished processing the call.
```

## Development and Contributing

Interested in contributing? We ❤️ pull requests!

To make sure our community is safe for all, be sure to review and agree to our
[Code of Conduct](./CODE_OF_CONDUCT.md). Then see the
[Contribution](./CONTRIBUTING.md) guidelines for more information.

## Getting Help

We love to hear from you so if you have questions, comments or find a bug in the
project, let us know! You can either:

- [Open an issue](https://github.com/deepgram/[reponame]/issues/new) on this repository
- Ask a question, share the cool things you're working on, or see what else we have going on in our [Community Forum](https://github.com/orgs/deepgram/discussions/)
- Tweet at us! We're [@DeepgramAI on Twitter](https://twitter.com/DeepgramAI)

## Further Reading

Check out the Developer Documentation at [https://developers.deepgram.com/](https://developers.deepgram.com/)
