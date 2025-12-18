class EmailService:
    def send(self, message):
        print(f"Sending email with message: {message}")

class SMSService:
    def send(self, message):
        print(f"Sending SMS with message: {message}")

class Notification: 
    def __init__(self, service):
        self.service = service #INJECTED DEPENDENCY

    def notify(self, message):
        self.service.send(message)

email_service = EmailService()
sms_service = SMSService()
n1 = Notification(email_service)
n1.notify("Hello via Email!")

n2 = Notification(sms_service)
n2.notify("Hello via SMS!") 

""" 

crud operations create, update delete, read orm
object relation mapper 
python framework .insert.append data base sanga link garna sakchu ok then, 
using orm you can do sql using python code

converts database tables too python objects 
avoids writing sql manually 
examples django, peewee

 """

