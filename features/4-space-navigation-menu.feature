Feature: Space Navigation Menu

    Background:
        Given a Cloud Free user is on the "Your Workspace" page

    Scenario: About page loads
        When user clicks the "About" link in the "Space Navigation Menu"
        Then the "Personal Workspace" content should appear to load successfully

    Scenario: Usage page loads
        When user clicks the "Usage" link in the "Space Navigation Menu"
        Then the "Usage" content should appear to load successfully

    Scenario Outline: Stats for different <period>s can be displayed
        Given the "Usage" page is displayed
        When "<period>" is selected from the "View by" dropdown menu
        Then stats should be shown for "Compute Hours" and "Active Content"

        When a different "<period>" is selected
        Then spinners should appear temporarily
        And stats should be shown for "Compute Hours" and "Active Content"

        Examples:
            | period         |
            | Usage Period   |
            | Calendar Month |
