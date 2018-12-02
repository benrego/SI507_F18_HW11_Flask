from flask import Flask, render_template, url_for
import requests
import secrets_example
import json

app = Flask(__name__)   #making an instance


@app.route('/')
def default():
    return '<h1>Welcome!</h1>'


@app.route('/user/<name>')
def nyt_articles(name):
    base_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
    params = {'api-key':secrets_example.api_key}
    results = requests.get(base_url, params)
    nyt_results = results.text
    nyt_data_obj = json.loads(nyt_results)['results']
    article_list = []
    acc = 0
    for article in nyt_data_obj[:5]:
        acc +=1
        article_list.append(article['title']+" ("+article['url']+")")
    return render_template('user.html',
        name=name, my_list=article_list)

@app.route('/user/<name>/<location>')
def nyt_article_gen(name,location):
    beginning_url = 'https://api.nytimes.com/svc/topstories/v2/'
    end_url = location+'.json'
    base_url = beginning_url+end_url
    params = {'api-key':secrets_example.api_key}
    results = requests.get(base_url, params)
    nyt_results = results.text
    nyt_data_obj = json.loads(nyt_results)['results']
    article_list = []
    acc = 0
    for article in nyt_data_obj[:5]:
        acc +=1
        article_list.append(article['title']+" ("+article['url']+")")
    return render_template('user.html',
        name=name, location=location,my_list=article_list)



if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)
