from confluent_kafka.admin import AdminClient
from utils.kafka_auth import get_auth_config

def create_admin_client(bootstrap_servers):
    config = {
        "bootstrap.servers": ",".join(bootstrap_servers),
        **get_auth_config()
    }

    return AdminClient(config)