import secrets, base64

def generate_nonce():
    rand_str = secrets.token_urlsafe(16)
    return base64.b64encode(rand_str.encode('utf-8')).decode('utf-8')

def generate_nonces(n):
    return [generate_nonce() for _ in range(n)]

def generate_nonce_str_from_list(nonce_list):
    return ' '.join([f"'nonce-{nonce}'" for nonce in nonce_list])