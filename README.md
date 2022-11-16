## 🌈 Here you will find tests for the landing page of the Exlab project

doc folder contains checklist

command to run all tests:

                pytest tests/test_LandingPage.py



Supports console options:

--browser_name=chrome  (firefox or chrome or yandex)

--language=ru  (default='en')

--headless=true  (default='None')

--width_window=1920  (default='1920')

--height_window=1080  (default='1080')

for example:

               pytest tests/test_LandingPage.py --browser_name=firefox --headless=true
