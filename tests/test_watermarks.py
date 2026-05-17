from utils.config_loader import load_config
from kafka.topic_collector import collect_topics
from kafka.client_factory import create_consumer, create_admin_client
from kafka.watermark_collector import  collect_topic_watermark

config = load_config()

admin_client = create_admin_client(config)

topics = collect_topics(admin_client)

consumer = create_consumer(config)

watermarks = collect_topic_watermark(consumer, topics)

for topic in watermarks:
    print(f"\ntopic: {topic['topic_name']}")
    print(
        f"Total high watermark: " f"{topic['total_high_watermark']}"
    )
    for partition in topic["partition_watermarks"]:

        print(
            f"Partition {partition['partition_id']} "
            f"-> High: {partition['high_watermark']} "
        )

consumer.close()