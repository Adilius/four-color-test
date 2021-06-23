from flask import request
from hashlib import sha256

# Takes the HTTP request headers and hash from client to create super-hash
def create_fingerprint(request, webhash = ""):
    hash_module = sha256()

    # HTTP request values
    user_agent = request.user_agent.string
    mimetype = request.mimetype
    accept_encodings = request.accept_encodings
    accept_languages = request.accept_languages
    accept_mimetypes = request.accept_mimetypes
    remote_addr = request.remote_addr

    # HTTP request values concatenated with web hash
    request_long = str(user_agent) + str(mimetype) + str(accept_encodings) + str(accept_languages) + str(accept_mimetypes) + str(remote_addr) + str(webhash)

    hash_module.update(request_long.encode('utf-8'))
    super_hash = hash_module.hexdigest()

    """
    print("--------REQUEST HEADERS--------")
    print("user_agent:", user_agent)
    print("mimetype:", mimetype)
    print("Accept_encodings:", accept_encodings)
    print("Accept_languages:", accept_languages)
    print("Accept_mimetypes:", accept_mimetypes)
    print("Remote_addr:", remote_addr)
    print("--------WEB HASH--------")
    print("Web hash:", webhash)
    print("Super hash:",super_hash)
    """

    return super_hash