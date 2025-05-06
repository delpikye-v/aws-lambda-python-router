class RouteEntity:
    def __init__(self, path, method, handler):
        self.path = path
        self.method = method
        self.handler = handler

class BaseController:
    list_routes: list[RouteEntity]

    def routes(self):
        return self.list_routes

class Routers:
    def __init__(self, controllers: list[BaseController] = []):
        self.routes = {}
        for controller in controllers:
            self.add(controller.routes())

    def add(self, routes: list[RouteEntity]):
        for route in routes:
            self.routes[f"{route.method}-{route.path}"] = route.handler

    def get(self, path: str, method: str):
        try:
            route = self.routes.get(f"{method}-{path}")
        except KeyError:
            raise RuntimeError(f"Cannot route request to the correct method. path={path}, method={method}")
        return route
