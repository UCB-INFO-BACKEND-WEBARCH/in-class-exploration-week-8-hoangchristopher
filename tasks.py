from rq.decorators import job
from redis import Redis
import os
import time

redis_conn = Redis.from_url(os.getenv('REDIS_URL', 'redis://localhost:6379/0'))

@job('notifications', connection=redis_conn)
def send_notification(notification_id, email, message):
    # Your code here
    print(f"Getting data...")
    time.sleep(3)
    print(f"Data retrieved")

    return {
        "notification_id" : notification_id,
        "email" : email, 
        "message" : message,
        "status" : "sent",
        "sent_at" : time.time()
    }