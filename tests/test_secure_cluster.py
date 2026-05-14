from utils.config_loader import load_config
import os
from kafka.client_factory import create_admin_client

def main():

    config = load_config()

    cluster = config["clusters"][0]

    ssl = cluster["security"]["ssl"]

    print("\n📋 Resolved SSL Paths:")
    for key, path in ssl.items():
        status = "✅ Found" if os.path.exists(path) else "❌ MISSING"
        print(f"  {key}: {path}  →  {status}")

    admin = create_admin_client(cluster)

    metadata = admin.list_topics(timeout=10)

    for topic in metadata.topics.keys():
        print(topic)

if __name__ == "__main__":
    main()