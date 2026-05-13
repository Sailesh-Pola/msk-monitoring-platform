from confluent_kafka.admin import AdminClient


config ={
    "bootstrap.servers": "b-1.loanmgt.rm74d5.c1.kafka.us-east-1.amazonaws.com:9098",
}

admin = AdminClient(config)

metadata = admin.list_topics(timeout=10)

print(metadata.topics.keys())