import json

from src.app.routers import BaseController, RouteEntity

## Module
class AwfController(BaseController):
    def __init__(self):
        self.list_routes = [
            RouteEntity(path="/dk-test-mutations", method="POST", handler=self.mutations),
            RouteEntity(path="/dk-test-configs/{name}", method="GET", handler=self.queries),
        ]

    def mutations(self, event, **kargs):
        return {
            'statusCode': 200,
            'body': json.dumps({ 'key': 'This is test' })
        }

    def queries(self, event, **kargs):
        return {
            'statusCode': 200,
            'body': json.dumps({ 'key': 'This is test' })
        }