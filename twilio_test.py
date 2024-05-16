from twilio.rest import Client

account_sid = 'ACdbc7e4bc2a1b1f96506da087300227b5'
auth_token = '92b91fb19d7000fddbb3bef53150f3df'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+15706693232',
  body='Ehoooooo',
  to='+359884678801'
)

print(message.sid)
