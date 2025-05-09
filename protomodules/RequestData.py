import requests

class ResearchData:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {'Authorization': f'Bearer {self.api_key}'}

    def find_supporting_data(self, query):
        # Correcting the query parameter to 'q' as expected by the API
        url = f"https://serpapi.com/search?q={query}&api_key={self.api_key}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to retrieve data, Status code: {response.status_code}, Message: {response.text}")

    def parse_data(self, data):
        parsed_data = []
        if data and 'results' in data:
            for item in data.get('results', []):
                parsed_data.append({
                    'title': item.get('title', 'No title provided'),
                    'summary': item.get('summary', 'No summary available'),
                    'url': item.get('url', 'No URL provided')
                })
        return parsed_data

# Usage
api_key = '---'  # Replace with your actual API key
research_assistant = ResearchData(api_key)
query = "happiness"
try:
    results = research_assistant.find_supporting_data(query)
    parsed_results = research_assistant.parse_data(results)
    # Assuming 'extended_corpus' is defined elsewhere and accessible here
    #extended_corpus.extend_corpus_with_nltk_resources([result['summary'] for result in parsed_results if result['summary'] not in extended_corpus])
except Exception as e:
    print(f"Error occurred: {e}")

print(results)
# if no extended corpus just extend the single corpus 
#corpus.extend(results)
