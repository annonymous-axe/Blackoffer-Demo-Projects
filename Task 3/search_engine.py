from elasticsearch import Elasticsearch

engine = Elasticsearch(['https://localhost:9200'], verify_certs=False, http_auth=['elastic', 'e7VIG5nWlUDgbeqsOFWs'])

def get_latest_data():
    """
    This is default function called when user visit the website.
    This just load the latest data (according the dataset).
    """
    res = engine.search(index='news_headlines', 
                        body = { "query": { 
                            "range": { 
                                "date": { 
                                    "gte": "2017-12-31",
                                    "lte": "2018-12-31" }
                                }
                            }})
    articles = res['hits']['hits']
    return articles

def get_categories():
    """
    As the name suggest, this function retrieve the all categories present in data.
    """    
    res = engine.search(index='news_headlines',
                        body = {"aggs":{
                            "categories":{
                                "terms":{
                                    'field':"category"
                                }
                            }
                        }})
    return res['aggregations']['categories']['buckets']

def sorted_searching(word, dates=None, category="*", author="*"):
    """
    This is function used to filter the searching process.
    """
    query_body = {
    "query": {
        "bool": {
        "must": [{
            "match_phrase": {
            "headline": word
            }
        }],
        "filter": []  # Initialize empty filter list
        }
    }
    }

    if dates:
        query_body["query"]["bool"]["filter"].append({
            "range": {
            "date": {
                "gte": dates[0],
                "lte": dates[1]
            }
            }
        })

    if category != "*":
        query_body["query"]["bool"]["filter"].append({
            "term": {
            "category": category
            }
        })

    if author != "*":
        query_body["query"]["bool"]["filter"].append({
            "term": {
            "authors": author
            }
        })

    result = engine.search(index="news_headlines", body=query_body)
    return result['hits']['hits']