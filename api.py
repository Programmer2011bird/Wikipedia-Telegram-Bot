import requests


class Downloader:
    def __init__(self, URL: str, filePath: str):
        pass

class API_HANDLER:
    def __init__(self) -> None:
        self.URL: str = "https://en.wikipedia.org/api/rest_v1/"

    def getFullHTML(self, title: str):
        self.ENDPOINT: str = ""

    def getFullPDF(self, title: str):
        self.ENDPOINT: str = ""

    def getSummary(self, title: str):
        self.ENDPOINT: str = ""


if __name__ == "__main__":
    API: API_HANDLER = API_HANDLER()

