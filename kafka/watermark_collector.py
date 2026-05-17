from confluent_kafka import  TopicPartition

def collect_topic_watermark(consumer, topics_metadata):
    topic_watermarks = []

    for topic in topics_metadata:

        topic_name = topic["topic_name"]
        total_high_watermark = 0
        partition_watermarks = []

        for partition_id in range(topic["partition_count"]):

            topic_partition = TopicPartition(topic_name, partition_id)

            low,high = consumer.get_watermark_offsets(topic_partition, timeout=10)
            partition_watermarks.append({"partition_id": partition_id, "low_watermark": low, "high_watermark": high})
            total_high_watermark += high

        topic_watermarks.append({"topic_name": topic_name, "total_high_watermark": total_high_watermark, "partition_watermarks": partition_watermarks})

    return topic_watermarks





