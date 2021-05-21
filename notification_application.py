#importing Notification from the py-notifier package
from pynotifier import Notification

#creating the notification
Notification(
    title='Stand up now!',
    description='standing up is good',
    duration=100
).send()