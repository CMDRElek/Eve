from urllib.request import urlopen
import json as m_json
import function


query = function.cmd
response = urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
json = m_json.loads ( response )
results = json [ 'responseData' ] [ 'results' ]
for result in results:
    title = result['title']
    url = result['url']   # was URL in the original and that threw a name error exception
    print ( title + '; ' + url )