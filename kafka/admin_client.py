from confluent_kafka.admin import AdminClient

def create_admin_client(bootstrap_servers):
    config = {
        "bootstrap.servers": ",".join(bootstrap_servers)
    }

    return AdminClient(config)