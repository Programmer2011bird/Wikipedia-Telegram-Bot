import requests


class API_HANDLER:
    def __init__(self) -> None:
        self.URL: str = "https://en.wikipedia.org/api/rest_v1"

    def getFullHTML(self, title: str) -> str:
        self.ENDPOINT: str = f"{self.URL}/page/html/{title}"
        
        RESPONSE: requests.Response = requests.get(self.ENDPOINT)
        RESPONSE_CONTENT: str = RESPONSE.content.decode()
        
        return RESPONSE_CONTENT

    def getFullPDF(self, title: str) -> bytes:
        self.ENDPOINT: str = f"{self.URL}/page/pdf/{title}"
        
        RESPONSE: requests.Response = requests.get(self.ENDPOINT)
        RESPONSE_CONTENT: bytes = RESPONSE.content

        return RESPONSE_CONTENT

    def getSummary(self, title: str) -> str:
        self.ENDPOINT: str = f"{self.URL}/page/summary/{title}"

        RESPONSE: requests.Response = requests.get(self.ENDPOINT)
        RESPONSE_JSON: dict = dict(RESPONSE.json())
        SUMMARY: str = str(RESPONSE_JSON["extract"])

        return SUMMARY


class Downloader:
    def __init__(self, Content: str | bytes, filePath: str) -> None:
        if type(Content) == bytes:
            with open(f"{filePath}", "wb") as file:
                file.write(Content)

        if type(Content) == str:
            with open(f"{filePath}", "w+") as file:
                file.write(Content)
