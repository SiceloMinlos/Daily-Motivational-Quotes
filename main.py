from email import message
from twilio.rest import Client
import keys, scrapper

client = Client(keys.account_sid, keys.auth_token)

message = client.messages.create(
    body= scrapper.random_quote()["Quote"] + " -by " + scrapper.random_quote()["Author"],
    from_=keys.twilio_number,
    to=keys.target_number
)