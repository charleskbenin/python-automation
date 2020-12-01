from twilio.rest import Client 
 
account_sid = '##############' 
auth_token = '###############' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hello babe',      
                              to='whatsapp:#'
                          ) 
 
print(message.sid)

# from_='whatsapp:+14155238886', 
