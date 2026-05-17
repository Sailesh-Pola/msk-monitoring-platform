from utils.config_loader import load_config
from kafka.topic_collector import collect_topics
from kafka.client_factory import create_consumer, create_admin_client
from kafka.watermark_collector import  collect_topic_watermark


def main():
    config = load_config()

    cluster = config["clusters"][0]

    admin_client = create_admin_client(cluster)

    consumer = create_consumer(cluster)

    topics = collect_topics(admin_client)

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

if __name__ == "__main__":
    main()