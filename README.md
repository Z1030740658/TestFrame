**pytest-requests-webdriver-appium-api-ui-testing-framework**
solution is running with:
- pipenv
- requests
- appium-python-client
- faker
- pytest
- flake8
- Python 3.7

---

## Setup, install dependencies.

Here, pipenv is used instead of pip. Run in command line:

1. Install Python 3.7.0
2. Run in command line: `pip install pipenv`
3. Run in command line: `pipenv install` (if the virtualenv is already activated, you can also use `pipenv sync`). Consider `pipenv install --dev` and `pipenv sync --dev` in case of dev dependencies.

Why pipenv?

Putting the dependencies into a requirements.txt and then using pip will work but is not really necessary. The whole point of using pipenv for most people is to avoid the need to manage a requirements.txt or to use pip.

---

## Run code static analysis.

- Run flake8: `pipenv run flake8 .`

---

## Run tests locally.

- Create ".env" file with "ENV=development" row in it in the root directory.
- Run all tests: `pipenv run pytest`
- Run project related tests: `pipenv run pytest tests/{project_name}`
- Run project related tests subset: `pipenv run pytest tests/{project_name}/{test_name}.py`

---

## To run Android UI tests locally.

1. You should have AVD (Android Studio) installed and virtual device configured, then you are able to start AVD with .bat file:

        cd C:\Users\%username%\AppData\Local\Android\sdk\emulator
        emulator @Pixel_2_API_29

where Pixel_2_API_29 - the name of my emulator.

2. Plase .apk file that should be tested to the root of project and set its corresponding name in config, `APK` variable.

3. Install Appium desktop, start a new inspecting session with capabilities same as your virtual device (inspecting elements), for example:

        {
        "platformName": "Android",
        "platformVersion": "10.0",
        "deviceName": "Pixel 2",
        "app": "C:\\project\\awesome.apk"
        }

4. Or do it from command line having appium.js installed, or start desktop client session (just running tests, no elements inspection).

---

## To run web UI tests.

1. You should have driver placed in the root directory.
2. Set its corresponding name in config, `WEB_DRIVER` variable.

---

## Current project related tests.

Currently, there are three projects with draft tests, they are in 'tests' folder:

- api_backend
- android_ui
- web_ui
