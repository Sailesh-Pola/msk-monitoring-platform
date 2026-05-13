CREATE TABLE IF NOT EXISTS topic_snapshot(
    id SERIAL PRIMARY KEY,
    cluster_name VARCHAR(255) NOT NULL,
    run_time TIMESTAMP NOT NULL,
    topic_name VARCHAR(500) NOT NULL,
    partition_count INTEGER NOT NULL,
    replication_factor INTEGER NOT NULL,
    total_high_watermark BIGINT NOT NULL
    );