Feature: The "currentUser" button in the upper-right corner provides a useful menu

    Background:
        Given a Cloud Free user is on the "Your Workspace" page

    Scenario: The "currentUser" button should display the User Popup Panel
        When the user clicks the "currentUser" button
        Then the User Popup Panel should be displayed
        And the information displayed on the User Popup Panel should include the following sections:
            | Sections             |
            | PLAN                 |
            | CURRENT USAGE PERIOD |
            | USAGE                |
            | User's name          |

    Scenario: The user can access the Account page from the User Popup Panel
        Given the User Popup Panel is displayed
        When the user clicks the "Account" link on the User Popup Panel
        Then the Account page should be displayed
        And every one of these options from the dropdown menu should load content without error:
            | popupButtonAndMenuContainer Option |
            | Overview                           |
            | Usage                              |
            | Spaces                             |
            | Members                            |
            | Invoices                           |
            | Tokens                             |
            | Settings                           |
