from flask import request

def printAddr(request):
    print("--------REQUEST HEADERS--------")
    print("Accept_encodings:", request.accept_encodings)
    print("Accept_languages:", request.accept_languages)
    print("Accept_mimetypes:", request.accept_mimetypes)
    print("Remote_addr:", request.remote_addr)
    print("user_agent:", request.user_agent.string)
    print("--------REQUEST HEADERS--------")