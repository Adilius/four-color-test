from flask import request
from hashlib import blake2b

# Takes the HTTP request headers and hash from webclient to create combined hash
def create_fingerprint(request, web_hash = ""):
    hash_module = blake2b(digest_size=16)

    # Get HTTP request values
    user_agent = request.user_agent.string
    mimetype = request.mimetype
    accept_encodings = request.accept_encodings
    accept_mimetypes = request.accept_mimetypes
    remote_addr = request.remote_addr

    # Create hash using HTTP request header
    request_long = str(user_agent) + str(mimetype) + str(accept_encodings) + str(accept_mimetypes) + str(remote_addr)
    hash_module.update(request_long.encode('utf-8'))
    http_hash = hash_module.hexdigest()

    # Create combined hash using http_hash and web_hash
    combined_string = str(http_hash) + str(web_hash)
    hash_module.update(combined_string.encode('utf-8'))
    combined_hash = hash_module.hexdigest()    

    return combined_hash