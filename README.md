### How to run a serverless in VS code

python3 --version --> install version 3.12.0 --> **Install version by pyenv**

python3 -m venv venv — **Create a Virtual Environment**

source venv/bin/activate — **Activate the Virtual Environment**

pip3 install -r requirements-dev.txt — **Install Dependencies**

### **Start the local simulation**:
    1. npm install
    2. npm run dev 

    Note: serverless offline start --reloadHandler
        - If we install serverless offline globally, we can run it directly instead of via 'npm run dev' in package.json file
        - Run multiple sls: serverless offline --httpPort=3002 --lambdaPort=3003

deactivate - **Deactivate the Virtual Environment**

source venv/bin/deactivate

### Some helpful extensions in VSCode:

autopep8, pylance, sonarlint , python indent

### Run test
- npm run test
- npm run test-html

- Specifying Test Cases or Methods
    - python3 -m unittest path/to/test_module.py::TestCaseClass
    - python3 -m unittest path/to/test_module.py::TestCaseClass.test_method

    - coverage run -m unittest test_my_function.py --- run global
    - coverage run -m unittest discover
    - coverage report
    - coverage html


### Development setup

#### Serverless
To expose APIGW via serverless-offline, add events to serverless functions
