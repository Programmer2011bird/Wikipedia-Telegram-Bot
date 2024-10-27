import requests
import json


class Downloader:
    def __init__(self, Content: str | bytes, filePath: str):
        pass

class API_HANDLER:
    def __init__(self) -> None:
        self.URL: str = "https://en.wikipedia.org/api/rest_v1"

    def getFullHTML(self, title: str) -> str:
        self.ENDPOINT: str = f"{self.URL}/page/html/{title}"
        
        RESPONSE: requests.Response = requests.get(self.ENDPOINT)
        RESPONSE_CONTENT: str = RESPONSE.content.decode()

        return RESPONSE_CONTENT

    def getFullPDF(self, title: str) -> tuple[bytes, str]:
        self.ENDPOINT: str = f"{self.URL}/page/pdf/{title}"
        
        RESPONSE: requests.Response = requests.get(self.ENDPOINT)
        RESPONSE_CONTENT: bytes = RESPONSE.content
        FILE_NAMES: str = dict(RESPONSE.headers)["content-disposition"]
        PDF_FILE_NAME: str = FILE_NAMES.split(';')[1].split('"')[1]

        return (RESPONSE_CONTENT, PDF_FILE_NAME)

    def getSummary(self, title: str) -> str:
        self.ENDPOINT: str = f"{self.URL}/page/summary/{title}"

        RESPONSE: requests.Response = requests.get(self.ENDPOINT)
        RESPONSE_JSON = RESPONSE.json()
        SUMMARY: str = str(RESPONSE_JSON["extract"])

        return SUMMARY


if __name__ == "__main__":
    API: API_HANDLER = API_HANDLER()
    print(API.getSummary("Earth"))
