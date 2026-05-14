from confluent_kafka.admin import AdminClient
from confluent_kafka import Consumer

def build_kafka_consumer(cluster_config):
    config  = {
        "bootstrap.servers": ",".join(cluster_config["bootstrap_servers"])
    }
    security = cluster_config.get("security")
    if security:
        protocol = security.get("protocol")
        config["security.protocol"] = protocol
        if protocol == "SSL":
            ssl_config = security.get("ssl", {})
            config["ssl.ca.location"] = ssl_config.get("ca_location")

            config["ssl.certificate.location"] = ssl_config.get("certificate_location")

            config["ssl.key.location"] = ssl_config.get("key_location")
            endpoint_alg = ssl_config.get("endpoint_identification_algorithm") or "none"
            config["ssl.endpoint.identification.algorithm"] = str(endpoint_alg)

    return config

def create_admin_client(cluster_config):
    config = build_kafka_consumer(cluster_config)
    return AdminClient(config)

def create_consumer(cluster_config):
    config = build_kafka_consumer(cluster_config)
    config["group.id"] = "msk-monitoring-group"
    config["auto.offset.reset"] = "earliest"
    return Consumer(config)
