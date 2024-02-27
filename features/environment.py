from behave import *
from playwright.sync_api import sync_playwright
import os.path
import json


def get_login_credentials(context):
    if os.path.isfile("env.json"):
        from dotmap import DotMap

        ENV_JSON = DotMap(json.load(open("env.json"))).toDict()
        context.USERNAME = ENV_JSON.get("USERNAME")
        context.PASSWORD = ENV_JSON.get("PASSWORD")

    if not ("USERNAME" in context and "PASSWORD" in context):
        print(
            """
        Please create an env.json file in the root of this project,
            with valid credentials for a "Cloud Free" posit.cloud account.

            The file should look like this, but contain real credentials:
            {
                "USERNAME": "username@example.com",
                "PASSWORD": "vszUd_LOL-Th1S1SN0TMyP@$$w0RDxxx!"
            }
            """
        )
        exit(0)


def set_up_faker():
    from faker import Faker

    fake = Faker()
    return fake


def before_all(context):

    get_login_credentials(context)
    context.fake = set_up_faker()

    playwright = sync_playwright().start()
    context.playwright = playwright

    browser_ = playwright.chromium.launch(headless=False)
    context_ = browser_.new_context()
    context.page = context_.new_page()


def after_all(context):
    context.playwright.stop()
