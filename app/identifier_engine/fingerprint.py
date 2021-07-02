from flask import request
from hashlib import blake2b

# Takes the HTTP request headers and hash from client to create combined hash
def create_fingerprint(request, webhash = ""):
    hash_module = blake2b(digest_size=16)

    # HTTP request values
    user_agent = request.user_agent.string
    mimetype = request.mimetype
    accept_encodings = request.accept_encodings
    accept_mimetypes = request.accept_mimetypes
    remote_addr = request.remote_addr

    print("-------- REQUEST HEADERS --------")
    print("user_agent:", user_agent)
    print("mimetype:", mimetype)
    print("Accept_encodings:", accept_encodings)
    print("Accept_mimetypes:", accept_mimetypes)
    print("Remote_addr:", remote_addr)

    # Create hash using HTTP request header
    request_long = str(user_agent) + str(mimetype) + str(accept_encodings) + str(accept_mimetypes) + str(remote_addr)
    hash_module.update(request_long.encode('utf-8'))
    HTTP_hash = hash_module.hexdigest()

    # Create combined hash using HTTP hash and webhash
    combined_string = str(request_long) + str(webhash)
    hash_module.update(combined_string.encode('utf-8'))
    combined_hash = hash_module.hexdigest()    

    print("-------- HASHES --------")
    print("Web hash:", webhash)
    print("HTTP hash:", HTTP_hash)
    print("Super hash:", combined_hash)

    return webhash, HTTP_hash, combined_hash