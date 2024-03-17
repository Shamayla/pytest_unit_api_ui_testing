import pytest
from playwright.sync_api import Page, expect


@pytest.mark.ui
def test_acme_bank_login(page: Page):
    #Arrange
    page.goto("https://demo.applitools.com")

    #Act
    page.locator('#username').fill("Andy")
    page.locator('#password').fill("andy")
    page.locator("#log-in").click()

    #Assert
    expect(page.locator('div.logo-w')).to_be_visible()
    expect(page.locator('//div[@class="logged-user-name"]')).to_have_text('Jack Gomez')