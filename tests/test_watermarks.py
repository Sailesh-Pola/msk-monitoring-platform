from ensurepip import bootstrap

from utils.config_loader import load_config
from kafka.admin_client import create_admin_client
from kafka.topic_collector import collect_topics

from kafka.watermark_collector import create_consumer, collect_topic_watermark

config = load_config()

cluster = config["cluster"][0]
bootstrap_servers = cluster["bootstrap_servers"]

admin_client = create_admin_client(bootstrap_servers)

topics = collect_topics(admin_client)

consumer = create_consumer(bootstrap_servers)

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