from confluent_kafka import Consumer, TopicPartition
from aws_msk_iam_sasl_signer import MSKAuthTokenProvider
from utils.kafka_auth import get_auth_config

def oauth_cb(config):
    """OAuth callback for MSK IAM authentication."""
    auth_token, expiry_ms = MSKAuthTokenProvider.generate_auth_token('us-east-1')
    return auth_token, expiry_ms / 1000

def create_consumer(bootstrap_servers):

    config = {
        "bootstrap.servers": ",".join(bootstrap_servers),
        "group.id": "msk-monitor-group",
        "auto.offset.reset": "earliest",
        **get_auth_config(),
        "socket.timeout.ms": 10000,
        "session.timeout.ms": 10000,
    }

    return Consumer(config)

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





