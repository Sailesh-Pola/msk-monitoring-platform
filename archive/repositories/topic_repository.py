from sqlalchemy import text

def insert_topic_snapshot(session, cluster_name, run_time, topic_name, partition_count, replication_factor, total_high_watermark):
    query = text("""
        INSERT INTO topic_snapshot (cluster_name, run_time, topic_name, partition_count, replication_factor, total_high_watermark)
        VALUES(:cluster_name, :run_time, :topic_name, :partition_count, :replication_factor, :total_high_watermark)
    """)

    session.execute(query, {"cluster_name": cluster_name,"run_time": run_time, "topic_name": topic_name,
                            "partition_count": partition_count, "replication_factor": replication_factor, "total_high_watermark": total_high_watermark})
