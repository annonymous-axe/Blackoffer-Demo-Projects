from elasticsearch import Elasticsearch

engine = Elasticsearch(['https://localhost:9200'],  verify_certs=False,  http_auth=['elastic', 'n0Z3uSGTYNlIJE8SR8wQ'])

def get_latest_movies():
    """
    This is default function called when user visit the website.
    This just load the latest data (according the dataset).
    """

    query = {
        "sort": {
            "column2": {
                "order": "desc"
            }
        }
    }
    res = engine.search(index='movies', body = query, size=80)
    movies = res['hits']['hits'][1:]
    return movies

def get_categories(category):
    """
    As the name suggest, this function retrieve the all categories present in data.
    """    
    res = engine.search(index='movies',
                        body = {"aggs":{
                            "categories":{
                                "terms":{
                                    'field':category
                                }
                            }
                        }})
    return res["hits"]["hits"]

def get_search_movie(data):
    """
    This is function used to filter the searching process.
    """
    query_body = {
        "query":{
            "multi_match": {
                "query": data,
                "fields": ["column1", "column8", "column9", "column10", "column7"]
            }
        }
    }

    movies = engine.search(index="movies", body=query_body)
    return movies['hits']['hits']


if __name__ == "__main__":

    # for movie in get_latest_movies()[1:]:
    for movie in get_search_movie('Love')[0:]:
    # for movie in get_categories('Drama')[1:]:

        print(movie["_source"])