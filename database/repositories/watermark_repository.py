from sqlalchemy import text

def insert_partition_offset(session, cluster_name, run_time, topic_name, partition_id, low_watermark, high_watermark):
    query = text("""
        INSERT INTO partition_offset(cluster_name, run_time, topic_name, partition_id, low_watermark, high_watermark)
        VALUES(:cluster_name, :run_time, :topic_name, :partition_id, :low_watermark, :high_watermark) 
    """)

    session.execute(query, {"cluster_name": cluster_name, "run_time": run_time, "topic_name": topic_name, "partition_id": partition_id,
                            "low_watermark": low_watermark, "high_watermark": high_watermark})