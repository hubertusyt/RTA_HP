from kafka import KafkaConsumer
from collections import defaultdict
from datetime import datetime
import json

consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='broker:9092',
    auto_offset_reset='earliest',
    group_id='velocity-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# {user_id: [datetime, datetime, ...]}
user_timestamps = defaultdict(list)
WINDOW_SECONDS = 60
ALERT_THRESHOLD = 3

print("Monitoring velocity anomalies (>3 transactions / 60s per user)...")

for msg in consumer:
    tx = msg.value
    user_id = tx['user_id']
    now = datetime.fromisoformat(tx['timestamp'])

    # Keep only timestamps within the 60-second window
    user_timestamps[user_id] = [
        ts for ts in user_timestamps[user_id]
        if (now - ts).total_seconds() <= WINDOW_SECONDS
    ]
    user_timestamps[user_id].append(now)

    count = len(user_timestamps[user_id])
    if count > ALERT_THRESHOLD:
        print(
            f"VELOCITY ALERT: {user_id} made {count} transactions in the last "
            f"{WINDOW_SECONDS}s | latest: {tx['tx_id']} | {tx['amount']:.2f} PLN | {tx['store']}"
        )
