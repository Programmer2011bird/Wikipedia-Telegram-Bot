import requests


class Downloader:
    def __init__(self, URL: str, filePath: str):
        pass

class API_HANDLER:
    def __init__(self) -> None:
        self.URL: str = "https://en.wikipedia.org/api/rest_v1"

    def getFullHTML(self, title: str):
        self.ENDPOINT: str = f"{self.URL}/page/html/{title}"
        
        RESPONSE: requests.Response = requests.get(self.ENDPOINT)
        RESPONSE_JSON: dict = dict(RESPONSE.json())

    def getFullPDF(self, title: str):
        self.ENDPOINT: str = f"{self.URL}/page/pdf/{title}/a4"

        RESPONSE: requests.Response = requests.get(self.ENDPOINT)
        RESPONSE_JSON: dict = dict(RESPONSE.json())

    def getSummary(self, title: str):
        self.ENDPOINT: str = f"{self.URL}/page/summary/{title}"

        RESPONSE: requests.Response = requests.get(self.ENDPOINT)
        RESPONSE_JSON: dict = dict(RESPONSE.json())


if __name__ == "__main__":
    API: API_HANDLER = API_HANDLER()

