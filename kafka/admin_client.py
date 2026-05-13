from confluent_kafka.admin import AdminClient
from aws_msk_iam_sasl_signer import MSKAuthTokenProvider


def oauth_cb(oauth_config):
    auth_token, expiry_ms = MSKAuthTokenProvider.generate_auth_token('us-east-1')
    return auth_token, expiry_ms / 1000

def create_admin_client(bootstrap_servers):
    config = {
        "bootstrap.servers": ",".join(bootstrap_servers),
        "security.protocol": "SASL_SSL",
        "sasl.mechanism": "OAUTHBEARER",
        'oauth_cb': oauth_cb,
    }

    return AdminClient(config)