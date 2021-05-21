#importing Notification from the py-notifier package
from pynotifier import Notification

#creating the notification
Notification(
    title='Stand up now!',
    description='stand up every 10 mins once',
    duration=600
).send()