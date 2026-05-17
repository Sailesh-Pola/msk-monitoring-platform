def insert_topic_snapshot(connection, cluster_name, run_timestamp, topic_name, partition_count, total_low_watermark,
                          total_high_watermark, estimated_message_count):
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO topic_snapshot (cluster_name, run_timestamp, topic_name, partition_count,"
                   " total_low_watermark, total_high_watermark, estimated_message_count)
                   values(?,?,?,?,?,?,?)""",
                   (cluster_name, run_timestamp, topic_name, partition_count, total_low_watermark, total_high_watermark, estimated_message_count))

    connection.commit()


