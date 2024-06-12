# Integeration_test_assignment

This is a simple project to demonstrate the intgeration test using the pytest framework. The project uses the request library to github api to get the repo content and delete a file in a repo and then check if the file is deleted or not.

## Installation

1. Clone the repository
2. Install the dependencies using the following command

```bash
pip install -r requirements.txt
```

3.  Generate the github token and pass it in the test file
4.  Run the test using the following command

```bash
pytest integration/github_api_test.py -v
```

Or

```bash
pytest  -v
```
