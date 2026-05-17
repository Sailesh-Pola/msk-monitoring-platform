from datetime import datetime
from utils.config_loader import load_config
from kafka.admin_client import create_admin_client
from kafka.topic_collector import collect_topics

from kafka.watermark_collector import  collect_topic_watermark
from kafka.client_factory import create_consumer

from archive.postgres_manager import SessionLocal

from archive.repositories.topic_repository import insert_topic_snapshot
from archive.repositories.watermark_repository import insert_partition_offset

def main():
    config = load_config()

    cluster_config = config["clusters"][0]
    cluster_name = cluster_config["name"]
    run_time = datetime.now()
    admin_client = create_admin_client(cluster_config)

    topics = collect_topics(admin_client)

    consumer = create_consumer(cluster_config)

    watermarks = collect_topic_watermark(consumer, topics)

    session = SessionLocal()

    try:
        for topic in topics:
            watermark_data = next(item for item in watermarks if item["topic_name"] == topic["topic_name"])
            insert_topic_snapshot(session=session, cluster_name=cluster_name, run_time=run_time, topic_name=topic["topic_name"],
                                  partition_count=topic["partition_count"],replication_factor=topic["replication_factor"],
                                  total_high_watermark=watermark_data["total_high_watermark"])

            for partition in watermark_data["partitions_watermarks"]:
                insert_partition_offset(session=session, cluster_name=cluster_name, run_time=run_time, topic_name=topic["topic_name"],
                                        partition_id=partition["partition_id"],low_watermark=partition["low_watermark"],high_watermark=partition["high_watermark"])
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")

    finally:
        session.close()
        consumer.close()

if __name__ == "__main__":
    main()
