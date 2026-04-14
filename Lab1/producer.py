from kafka import KafkaProducer
import json, random, time
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='broker:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_transaction(tx_num):
    return {
        "tx_id": f"TX{tx_num:04d}",
        "user_id": f"u{random.randint(1, 20):02d}",
        "amount": round(random.uniform(5.0, 5000.0), 2),
        "store": random.choice(["Warsaw", "Krakow", "Gdansk", "Wroclaw"]),
        "category": random.choice(["electronics", "clothing", "food", "books"]),
        "timestamp": datetime.now().isoformat()
    }

print("Starting producer – sending 50 transactions to 'transactions' topic...")

for i in range(1, 51):
    tx = generate_transaction(i)
    producer.send('transactions', value=tx)
    print(f"Sent: {tx['tx_id']} | {tx['user_id']} | {tx['amount']:.2f} PLN | {tx['store']} | {tx['category']}")
    time.sleep(1)

producer.flush()
print("Done – 50 transactions sent.")
