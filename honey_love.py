from twilio.rest import Client 
 
account_sid = 'AC0abdc06431e2fe4eecf0598d124d6ede' 
auth_token = '867398f50f291f6b19a93764f11f46ec' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hello babe',      
                              to='whatsapp:#'
                          ) 
 
print(message.sid)

# from_='whatsapp:+14155238886', 