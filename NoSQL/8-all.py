#!/usr/bin/env python3
"""Program lists all documents in a collection:"""


def list_all(mongo_collection):
    """ function that lists all documents in a collection:"""
    documents = []
    for document in mongo_collection.find():
        documents.append(document)
    # OR
    # documents = list(mongo_collection.find())
    return documents
