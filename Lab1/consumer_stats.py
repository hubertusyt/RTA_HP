from kafka import KafkaConsumer
from collections import defaultdict
import json

consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='broker:9092',
    auto_offset_reset='earliest',
    group_id='stats-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Per-category state: {category: {count, total, min, max}}
stats = defaultdict(lambda: {'count': 0, 'total': 0.0, 'min': float('inf'), 'max': float('-inf')})
msg_count = 0

print("Tracking per-category statistics (summary every 10 messages)...")

for msg in consumer:
    tx = msg.value
    cat = tx['category']
    amount = tx['amount']

    s = stats[cat]
    s['count'] += 1
    s['total'] += amount
    s['min'] = min(s['min'], amount)
    s['max'] = max(s['max'], amount)
    msg_count += 1

    if msg_count % 10 == 0:
        print(f"\n--- Category Stats after {msg_count} messages ---")
        print(f"{'Category':<14} {'Count':>6} {'Total':>12} {'Min':>9} {'Max':>9} {'Avg':>9}")
        print("-" * 63)
        for cat_name in sorted(stats):
            s = stats[cat_name]
            avg = s['total'] / s['count']
            print(f"{cat_name:<14} {s['count']:>6} {s['total']:>12.2f} {s['min']:>9.2f} {s['max']:>9.2f} {avg:>9.2f}")
