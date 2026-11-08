def search_movies(movies, query):
    results = []
    for movie in movies:
        if query in movie["title"]:
            results.append(movie)
    return results[:5]