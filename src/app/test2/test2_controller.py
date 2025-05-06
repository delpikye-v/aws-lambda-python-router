import json

from src.app.routers import BaseController, RouteEntity

## Module
class Test2Controller(BaseController):
    def __init__(self):
        self.list_routes = [
            RouteEntity(path="/test2-mutations", method="POST", handler=self.mutations),
        ]

    def mutations(self, event, **kargs):
        return {
            'statusCode': 200,
            'body': json.dumps({ 'key': 'This is test2' })
        }