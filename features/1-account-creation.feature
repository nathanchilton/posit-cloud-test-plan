Feature: Account creation

    Scenario: Creating an account
        Given the posit.cloud page is displayed to the user
        When the user signs up for a new "Cloud Free" account
        Then the user should be instructed to verify the user's email address using a link in the email message
        And the user should receive an email message from Posit Cloud, with the following subject: "Please verify your email address"

    Scenario: Verifying email account
        Given the user has been prompted to "Verify Your Email"
        When the user clicks the "Verify your email" link in the email message
        And clicks the "Continue" button on the "Verify Your Email" page
        Then the user should see the "Your Workspace" page
