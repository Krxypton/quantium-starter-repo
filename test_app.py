import pytest
from app import app
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=10)
    assert dash_duo.find_element("h1").text == "Pink Morsel Sales Visualiser"

def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-chart", timeout=10)
    assert dash_duo.find_element("#sales-chart")

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-filter", timeout=10)
    assert dash_duo.find_element("#region-filter")