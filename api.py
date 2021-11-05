import httpx


class API:
    headers = {"Accept": "application/vnd.github.v3+json"}

    def raise_on_4xx_5xx(self, response):
        response.raise_for_status() 

    def get(self, url: str) -> list:
        """Uses httpx.Client().get to send the appropriate github headers, and return the url"""
        content = []
        with httpx.Client(headers=self.headers, event_hooks={'response': [self.raise_on_4xx_5xx]}) as client:
            while True:
                resp = client.get(url)
                body = resp.json()
                if isinstance(body, dict):
                    # short circuit if not list
                    return body
                content.extend(body)
                if not resp.links.get('next'):
                    break
                url = resp.links['next']['url']
        return content
