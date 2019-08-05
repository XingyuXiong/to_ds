from scrab_news import *

api_key='793110ecda064a68846a1510d0e7d0ae'
newsapi=NewsApiClient(api_key=api_key)

'''
test_data={
"status": "ok",
"totalResults": 38,
"articles": [
{
"source": {
"id": null,
"name": "Espn.com"
},
"author": null,
"title": "Syndergaard 'electric,' confident he'll stay a Met - ESPN",
"description": "Noah Syndergaard dominated the White Sox with 11 strikeouts over 7&frac13; innings Tuesday and expressed confidence that he wouldn't be traded ahead of Wednesday's deadline.",
"url": "https://www.espn.com/mlb/story/_/id/27290932/syndergaard-electric-confident-stay-met",
"urlToImage": "https://a3.espncdn.com/combiner/i?img=%2Fphoto%2F2019%2F0731%2Fr577333_1296x729_16%2D9.jpg",
"publishedAt": "2019-07-31T06:00:31Z \xf4",
"content": "CHICAGO -- If Tuesday marked the swan song of Noah Syndergaard's New York Mets career, he made the most of his final outing. Not that he thinks it was.\r\nThe big right-hander they call \"Thor\" went 7 strong innings, holding the Chicago White Sox to an unearned … [+4525 chars]"
}]}
solve_code_error(test_data['articles'][0])'''


news=News()
news.write_default_news()
news.read_default_news()
news.add_topic()
news.read_news('France')
