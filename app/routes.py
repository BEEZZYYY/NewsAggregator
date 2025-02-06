from flask import Blueprint, render_template, jsonify, current_app, request
import requests

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/news')
def get_news():
    api_key = current_app.config.get('NEWS_API_KEY')
    base_url = 'https://newsapi.org/v2/top-headlines'

    # Получаем дополнительные параметры из запроса
    category = request.args.get('category')
    search_query = request.args.get('q')

    params = {
        'country': 'us',   # Можно изменить на нужную страну, например 'ru'
        'apiKey': api_key,
        'pageSize': 10
    }
    if category:
        params['category'] = category  # Например, 'sports' или 'technology'
    if search_query:
        params['q'] = search_query

    response = requests.get(base_url, params=params)
    data = response.json()
    return jsonify(data)
