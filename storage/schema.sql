CREATE TABLE IF NOT EXISTS topic_snapshot(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cluster_name TEXT NOT NULL,
    run_timestamp TEXT NOT NULL,
    topic_name TEXT NOT NULL,
    partition_count INTEGER NOT NULL,
    total_low_watermark INTEGER NOT NULL,
    total_high_watermark BIGINT NOT NULL,
    estimated_message_count INTEGER NOT NULL
    );

