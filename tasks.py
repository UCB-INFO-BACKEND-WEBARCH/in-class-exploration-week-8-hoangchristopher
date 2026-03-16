from rq.decorators import job
from redis import Redis
import os

redis_conn = Redis.from_url(os.getenv('REDIS_URL', 'redis://localhost:6379/0'))

@job('notifications', connection=redis_conn)
def send_notification(notification_id, email, message):
    # Your code here
    pass