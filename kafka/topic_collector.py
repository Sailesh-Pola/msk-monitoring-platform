def collect_topics(admin_client):
   metadata = admin_client.list_topics(timeout=10)

   topics = []

   for topic_name, topic_metadata in metadata.topics.items():
       if topic_metadata.error is not None:
           continue

       topic_info ={
           "topic_name": topic_name,
           "partition_count": len(topic_metadata.partitions),
           "replication_factor": len(next(iter(topic_metadata.partitions.values())).replicas)
       }

       topics.append(topic_info)

   return topics
