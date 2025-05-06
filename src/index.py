from src.app.routers import Routers

from src.app.awf.awf_controller import AwfController
from src.app.test2.test2_controller import Test2Controller

# IDEA base: NodeJS/NestJS
router = Routers([
    # Module
    AwfController(),
    Test2Controller(),
])

def app_handler(event, context):
    # wrapper: try catch error here
    path = event["resource"]
    http_method = event["httpMethod"]
    method = router.get(path=path, method=http_method)
    return method(event=event, context=context)