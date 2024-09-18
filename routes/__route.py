from flask import Flask
from config.config import Config
from typing import List

class Route:
    def __init__(self, app: Flask, route: str, view: callable) -> None:
        self.app = app
        self.route = route
        self.view = view
        self.app.add_url_rule(self.route, view_func=self.view)


def register_routes(routes:List[List[str]]) -> None:

    for route, view in routes:
        Route(Config.app, route, view)


