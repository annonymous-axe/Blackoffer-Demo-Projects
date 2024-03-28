from flask import Flask, render_template, request, session
import search_engine

app = Flask(__name__)
app.secret_key = "this7is8my9secret9key"

@app.route('/')
def index():
    """
    This is default function called, when user visit the site.
    """
    articles = search_engine.get_latest_data()
    categories = search_engine.get_categories()
    return render_template('index.html', categories=[list(category.values()) for category in categories],
                           articles=[article['_source'] for article in articles])


@app.route("/search", methods=["POST"])
def search():
    """
    This is simple search function. Which just search the word in databased using search_engine.
    And return a html template which contain the result.
    """
    word = request.form['search_word']
    session["search_word"] = word

    articles = search_engine.sorted_searching(word)
    categories = search_engine.get_categories()

    if len(articles) == 0:
        return render_template("fallback.html", word=word)
    return render_template('index.html', word=word, categories=[list(category.values()) for category in categories],
                           articles=[article['_source'] for article in articles])

@app.route('/sroted_serach', methods=["POST"])
def sroted_serach():
    """
    This is similar to search() but it apply the all filters we selected.
    """
    word = session["search_word"]
    category = request.form.get('categories')
    # dates = request.form.get('dates')
    if category != 'all':
        articles = search_engine.sorted_searching(word, category=category)

    categories = search_engine.get_categories()
    return render_template('index.html', word=word, categories=[list(category.values()) for category in categories],
                           articles=[article['_source'] for article in articles])


        
if __name__ == "__main__":
    app.run(debug=True)