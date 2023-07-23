#!/usr/bin/env python3
def schools_by_topic(mongo_collection, topic):
    collection = mongo_collection.find({"topic": topic})
    return collection
