from aws_msk_iam_sasl_signer import MSKAuthTokenProvider

AWS_REGION = 'us-east-1'

def oauth_cb(config):
    auth_token, expiry_ms = MSKAuthTokenProvider.generate_auth_token(AWS_REGION)
    return auth_token, expiry_ms / 1000

def get_auth_config() -> dict:
    return {
        "security.protocol": "SASL_SSL",
        "sasl.mechanism": "OAUTHBEARER",
        "oauth_cb": oauth_cb,
    }