from plyer import notification
import time

import plyer
def main():
  title = 'Hello my better half'
  message= 'Know that I love you 💓'

  plyer.notification.notify(
    title= title,
    message= message,
    app_icon = "C:\\Users\Ashmi\\Desktop\\facebook page\\Notification\\hands.ico",
    app_name = "From Shorty's",
    timeout= 10,
    toast=False)

while True:
  main()
  time.sleep(3600)
  main()
  time.sleep(3600)