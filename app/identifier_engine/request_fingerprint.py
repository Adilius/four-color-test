from flask import request

def printAddr(request):
    print("Printaddr:", request.remote_addr)
    print("content_type:", request.content_type)