import requests

def synonyms (name):
    api_url = f'https://www.wordsapi.com/mashape/words/{name}/synonyms?when=2024-03-29T21:19:18.142Z&encrypted=8cfdb18ee722909be89807bdee58bfb0aeb1250931fb95b8'
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
    if response.status_code == requests.codes.ok:
        jsona = response.json()
        return jsona['synonyms']
    else:
        return "Error:", response.status_code, response.text

def antonyms (name):
    api_url = f'https://www.wordsapi.com/mashape/words/{name}/antonyms?when=2024-03-30T12:38:20.966Z&encrypted=8cfdb18ee722909be99107beed58bdb1aeb22d0939f991b8'
    response = requests.get(api_url)
    if response.status_code == requests.codes.ok :
        jsonA = response.json()
        return jsonA['antonyms']
    else:
        return "Error:" , response.status_code , response.text
    
print (antonyms('good'))