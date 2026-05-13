from confluent_kafka.admin import AdminClient
from aws_msk_iam_sasl_signer import MSKAuthTokenProvider

def oauth_cb(oauth_config):
    auth_token, expiry_ms = MSKAuthTokenProvider.generate_auth_token('us-east-1')
    return auth_token, expiry_ms / 1000


config ={
    "bootstrap.servers": "b-1.loanmgt.rm74d5.c1.kafka.us-east-1.amazonaws.com:9098",
    "security.protocol":"SASL_SSL",
    "sasl.mechanism":"OAUTHBEARER",
    'oauth_cb':oauth_cb,
}

admin = AdminClient(config)

metadata = admin.list_topics(timeout=10)

print(metadata.topics.keys())
