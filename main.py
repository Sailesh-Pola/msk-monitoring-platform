import os
from datetime import datetime
from utils.config_loader import load_config
from kafka.topic_collector import collect_topics

from kafka.watermark_collector import  collect_topic_watermark
from kafka.client_factory import create_consumer, create_admin_client

from storage.sqlite_manager import get_connection

from storage.topic_repository import insert_topic_snapshot

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def main():
    config = load_config()
    cluster_config = config["cluster"][0]
    cluster_name = cluster_config["name"]
    db_path = os.path.join(BASE_DIR, cluster_config["storage"]["sqlite_path"])
    connection = get_connection(db_path)
    admin_client = create_admin_client(cluster_config)
    consumer = create_consumer(cluster_config)
    topics = collect_topics(admin_client)
    watermarks = collect_topic_watermark(consumer, topics)
    run_timestamp = datetime.utcnow().isoformat()

    for topic in watermarks:
        matching_topic = next(t for t in topics if t["topic_name"] == topic["topic_name"])
        insert_topic_snapshot(connection= connection, cluster_name= cluster_name,run_timestamp= run_timestamp, topic_name=topic["topic_name"],
                              partition_count=matching_topic["partition_count"], total_low_watermark=topic["total_low_watermark"],
                              total_high_watermark=topic["total_high_watermark"], estimated_message_count=topic["estimated_message_count"])

        print(f"stored metrics for topic:  {topic['topic_name']}")

    consumer.close()
    connection.close()

if __name__ == "__main__":
    main()
