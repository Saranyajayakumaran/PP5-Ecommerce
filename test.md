# TESTING

## Validator Testing

## HTML

This project includes built-in HTML form validation to ensure accurate and complete data entry. Below are the validation features implemented:
All HTML pages were run through the W3C HTML Validator

![HTML Validation](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/documentation/Screenshots/html%20validation/product%20page.png)

Note: Image upload widget errors

All forms which include an image upload field show the same error below. This relates to the image upload widget on the form and thus changing the code breaks the field.

![Edit product page error](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/documentation/Screenshots/html%20validation/Edit%20product.png)

## CSS

No errors were found when passing my CSS files through the official W3C CSS Validator

![Edit product page error](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/documentation/Screenshots/html%20validation/css%20validation.png)


Python Validation - Pycodestyle
Python testing was done using Pycodestyle to ensure there were no syntax errors.

The only errors displayed (as per below screenshot) can be ignored. The majority are within automatically generated files with the exception of env.py and webhooks.py.

I have ignored the the formatting errors related to env.py as they relate to my Secret Keys and Database URL being to long. This file is not committed to github.


![Edit product page error](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/documentation/Screenshots/html%20validation/pylint%20error%20final.png)

# Functional Testing
# NavBar

|Testcase|Expected behavior|PASS/FAIL|
|--------|-----------------|---------|
|Click the title in navbar| Successfully render homepage|PASS|
|Click the products navbar| successfully show the dropdown items|PASS|
|Click the testimonials|Successfully render testimonial page|PASS|
|Click the contact us |Successfully render Enquiry form|PASS|
|Click wishlist icon (not logged in user)|Successfully render login page|PASS|
|Click wishlist icon (already logged in user)|Successfully render wishlist page|PASS|
|Click user icon| Successfully show dropdown items|PASS|
|Click shopping cart|Successfully render shopping bag|PASS|
|Search produt related name in searchbar| Successfully display the specific product| PASS|


# HomePage

|Testcase|Expected behavior|PASS/FAIL|
|--------|-----------------|---------|
|click shop now button| successfully render All products page|PASS|

# Products nav item

|Testcase|Expected behavior|PASS/FAIL|
|--------|-----------------|---------|
|Click all products dropdown item|Successfully render all products page|PASS|
|Click "Beauty" dropdown item|Successfully display only products in beauty category in product page|PASS|
|Click "Haircare" dropdown item|Successfully display only products in haircare category in product page|PASS|
|Click "Health and Wellness|Successfully display only products in health and wellness category in product page|PASS|
|Click "by Price"|Sort produts by price in ascending order|PASS|
|Click "by Rating"|Sort products by rating in ascending order|PASS|
|Click "by Category"|Sort Products by category from A-Z|PASS|

# Produts Page

|Testcase|Expected behavior|PASS/FAIL|
|--------|-----------------|---------|
|Click any product image| Render product detail page with specific product|PASS|
|Click Category badge|Display all products in specific category|PASS|
|Click sorting field|Display all sorting functionality in dropdown|PASS|
|Click Price(low to high)|Sort all the products price in ascending order|PASS|
|Click price(high to low)|Sort all the products price in descending order|PASS|
|Click Rating (low to high)|Sort all the products rating in ascending order|PASS|
|Click Rating( high to low) |Sort all the products rating in descending order|PASS|
|Click Name(A-Z)|sort all the products name A-Z|PASS|
|Click Name(Z-A)|Sort all the products name (Z-A)|PASS|
|Click category(A-Z)|Sort all the products by category name A-Z|PASS|
|Click category(Z-A)|Sort all the products by category name Z-A|PASS|
|Click up-arrow button in right corner|Scroll to top of the page|PASS|
|Click Products home link |Display all the products in product page|PASS|

# Product detail page

|Testcase|Expected behavior|PASS/FAIL|
|--------|-----------------|---------|
|Click "Keep shopping" Button| Redirect products page|PASS|
|Click "Add to bag" button|Add specific product to shopping bag and display success message "Product added to shopping bag successfully" with product details |PASS|
|Click Quantity '+' button in quantity input|Increase the number of qunatity max "99" disable '+' button when quanttiy reaches 99|PASS|
|Click Quantity '-' button in quantity input|Decrease the number of qunatity min "1" disable '-' button when quanttiy reaches 1|PASS|
|Click Category badge|Display all products in specific category|PASS|
|Click secure Checkout button in success message|Go to shopping bag page with grand total|PASS|

# Shopping bag Page

|Testcase|Expected behavior|PASS/FAIL|
|--------|-----------------|---------|
|Click Secure Checkout button|Go to checkout page|PASS|
|Click keep shopping button|Go to all products page|PASS|
|Click Product image in shopping bag page|Go to specific product detail page|PASS|
|Click Quantity '+' button in quantity input|Increase the number of qunatity max "99" disable '+' button when quanttiy reaches 99||
|Click Quantity '-' button in quantity input|Decrease the number of qunatity min "1" disable '-' button when quanttiy reaches 1||
|Click update icon after increse or decrease quantity|Update the quantity in shopping bag|PASS|
|Click delete icon |Delete the specific product from shopping bag|PASS|
|When no products added in shopping bag|Display no products in shopping bag|PASS|


# Checkout Page

## Valid input

|Testcase|User Input|Expected behavior|PASS/FAIL|
|--------|----------|-----------------|---------|
|Case 1| Enter valid inputs in checkout form"name:Test", | Order should complete and display order details and send email to the email address specified in the form" |PASS|
        "email:test@test.com",
        "Phone neumber:01234567890",
        "streetaddress1: test street1",
        "streetaddress2: test street2",
        "town or city: stuttgart",
        "Postalcode:123456",
        "country:Germany" and "Payment:42424242424242424" 
        
        click complete order 
|Case 2| Click save the info field to save the informations(logged in user)|save the information to my profile|PASS|
|Case 3| Click create account if user dont have an account|Go to sign up page|PASS|
|Case 4| Click login if user already have an account|Go to login page|PASS|
|Case 5| Click adjust bag| got to shopping bag page|PASS|


## Invalid Inputs

|Testcase|User Input|Expected behavior|PASS/FAIL|
|--------|----------|-----------------|---------|
|Case 1|Leave fullname field|Prompt user to enter the username|PASS|
|Case 2|Enter invalid email id "testtestmail.com"|Prompt user to enter valid email id|PASS|
|Case 3|Leave phone number empty|Prompt user to fill the phone number field|PASS|
|Case 4|Leave street address1 field empty|Prompt user to fill the filed|PASS|
|Case 5|Leave the town or city field empty|Prompt user to fill the field|PASS|
|Case 6|Dont select the country|Prompt user to select a country|PASS|
|Case 7|Leave the payment field empty|Display error message card details are imcomplete|PASS|


# Login Form

## valid input

|Testcase|User Input|Expected behavior|PASS/FAIL|
|--------|----------|-----------------|---------|
|Case 1|Fill the valid username and password|Render homepage of the website and success message"You are logged in as with username"|PASS|
|Case 2|Enter valid email address and password|Render homepage of the website and success message"You are logged in as with username"|PASS|
|Case 3|Click home button|go to home page|PASS|
|Case 4|Click forgot password|Ask the user to enter email address to recover password|PASS|
|Case 5|Enter email id and click reset my password|Send email to the user with link to recover password|PASS|
|Case 6|Click back to login|Go to login page|PASS|


## Invalid input

|Testcase|User Input|Expected behavior|PASS/FAIL|
|--------|----------|-----------------|---------|
|Case 1|Fill the username not password and click sign in|Prompt user to fill the passowrd field|PASS|
|Case 2|Leave the username and fill password and click sign in|Prompt user to fill the username field|PASS|
|Case 3|Fill the Wrong username and password and click sign in|Error message"The username or password you entered are incorrect|PASS|

# Signup Form

## Valid Input

|Testcase|User Input|Expected behavior|PASS/FAIL|
|--------|----------|-----------------|---------|
| Case 1|Enter all the valid inputs E-mail:"test@testmail.com"| Create an account and render login page|PASS|
                confirm email:"test@testmal.com"
                username:test
                password:unlock@test
                confirm_password:unlock@test
                and click signup
|Case 2| Click sign_in  link| Render login page|PASS|

## Invalid Input

|Testcase|User Input|Expected behavior|PASS/FAIL|
|--------|----------|-----------------|---------|
|Case 1| Enter the username already exist|Error:"A user with that username already exist"|PASS|
|Case 2| Enter the password similar to Email| Error:"The password is too similar to email"|PASS|
|Case 3|Enter a short password eg:"test"| Error: "The password is too short"|PASS|
|Case 4|Enter a invalid email address eg:"testtestmail.com"| Error:"Please include an @ in email address"|PASS|
|Case 5|Enter different mail in email and email confirmation field|Error:"You must type same email each time"|PASS|
|Case 6|Enter different Password and password again field| Error:"You must type the same password"|PASS|


# Testimonial Page

## Valid Input

|Testcase|User Input|Expected behavior|PASS/FAIL|
|--------|----------|-----------------|---------|
|not a logged in user|click add testimonial button|go to sign in page|PASS|
|already logged in user|click add testimonial button|render add testimonial form|PASS|
|Case 3|if user is a admin/super user|All testimonial should have edit and delete button|PASS|
|case 4| if user is a regular user|The edit and delet button should have only their own testimonials|PASS|

## Add your testimonial

## Valid Input
|Testcase|User Input|Expected behavior|PASS/FAIL|
|--------|----------|-----------------|---------|
|Case 1 |Select a product from the list and give a valid message and click submit|Testimonial should display in testimonial page|PASS|
|Case 2 |Click back to testimonial button|Go to testimonial page|PASS|

## Invalid Input

|Testcase|User Input|Expected behavior|PASS/FAIL|
|--------|----------|-----------------|---------|
|Case 1| Do not select a product |Prompt user to select a product in the list| PASS|
|Case 2| Enter only 5 characters in message input eg:testi |Error: "The messsage must be atleast 10 characters long| PASS|
|Case 3| Enter Banned keywords eg:"ridiculous"|Error: "The message contains inappropriate content 'ridiculous',Please remove it|PASS|


## Edit Testimonial

## Valid Input
|Testcase|User Input|Expected behavior|PASS/FAIL|
|--------|----------|-----------------|---------|
|Case 1 |Click edit button in testimonial page| render edit testimonial form with already available details|PASS|
|Case 2| Change product and change valid the message and click submit | Changes should reflect in testimonial page|PASS|
|Case 3|Click Back to testimonial button|Render to testimonial page|PASS|

## Invalid Input

|Testcase|User Input|Expected behavior|PASS/FAIL|
|--------|----------|-----------------|---------|
|Case 1| Do not select a product |Prompt user to select a product in the list| PASS|
|Case 2| Enter only 5 characters in message input eg:testi |Error: "The messsage must be atleast 10 characters long| PASS|
|Case 3| Enter Banned keywords eg:"ridiculous"|Error: "The message contains inappropriate content 'ridiculous',Please remove it|PASS|


## Delete testimonials

|Testcase|User Input|Expected behavior|PASS/FAIL|
|--------|----------|-----------------|---------|
|Case 1|Click delete button|Delete the testimonial and give a succes message |PASS|


## Contact Us page

## Valid Input
|Testcase|User Input|Expected behavior|PASS/FAIL|
|--------|----------|-----------------|---------|
|Case 1|Enter all valid details|   Enquiry should send to the admin and display success message| PASS|
        Fullname : 'testing'
        Email : 'testing@testing.com'
        Type of enquiry :'Gerneral enquiry'
        subject : 'Product availability'
        message: 'Do the product available in the logger?'
        and click submit
|Case 2|Click cancel button|Render products page|PASS|


## Invalid Input
|Testcase|User Input|Expected behavior|PASS/FAIL|
|--------|----------|-----------------|---------|
|Case 1|Enter user name with 2 character eg:'sa'| Error"Fullname must be atleast 3 character long"|PASS|
|Case 2|Enter subject only 4 characters eg:'test'| Error:"Subject must be atleast 5 character long"|PASS|
|Case 3|Enter message with only 10 characters eg:'complaints'|Error:"Message must be atleast 20 characters long"|PASS|
|Case 4| Enter Banned keywords eg:"ridiculous"|Error: "The message contains inappropriate content 'ridiculous',Please remove it|PASS|
 

# Wishlist Page

|Testcase|User Input|Expected behavior|PASS/FAIL|
|--------|----------|-----------------|---------|
|Not logged in user|click wishlist icon|Render login page|PASS|
|Logged in user|click wishlist icon|Render wishlist page|PASS|
|Case 3| If no item in wish list| Your wishlist is empty, start adding items|PASS|
|Case 4| If item in wishlist| Show all the wishlist item|PASS|
|Case 5| Click Product image| go to product detail page|PASS|
|Case 6|Click delete button|Remove item from wishlist |PASS|


# My Profile page

|Test Case|Expected behavior|PASS/FAIL|
|---------|-----------------|---------|
|If info saved already|show the informations in each field|PASS|
|Change info and click update informations button|Update user informations in profile|PASS|


# Super user Product management

## Add Product 
|Test Case|Expected behavior|PASS/FAIL|
|---------|-----------------|---------|
|Enter all valid input ,select image, name, sku,size,rating,price image url and click add product|Add product to the product page and immedietly reflect in product page|PASS|
|Click cancel button| render product page |PASS|

## Edit product
|Test Case|Expected behavior|PASS/FAIL|
|---------|-----------------|---------|
|User clicks edit button in product page |Render edit product form with all the already available details| PASS|
|Change the field and click update|The details should be updated and immedietly reflect in product| PPASS|
|Click cancel button|render product page|PASS|

## Delete product
|Test Case|Expected behavior|PASS/FAIL|
|---------|-----------------|---------|
|Click the delete link in product page|Delete the product|PASS|

# Footer
|Test Case|Expected behavior|PASS/FAIL|
|---------|-----------------|---------|
|Click facebook icon|Open facbook business page in separate window|PASS|
|Click twitter icon|Open twitter page in separate window|PASS|
|Click instagram icon|Open Instagram page in separate window|PASS|
|Click youtube icon |open youtube page in separate window|PASS|

## Quick Links

|Test Case|Expected behavior|PASS/FAIL|
|---------|-----------------|---------|
|Click home link|Open home page|PASS|
|Click Products link|Open all products page|PASS|
|Click Testimonials link|Open testimonial page|PASS|
|Click Wishlist page|Open login page if not already logged in|PASS|
|Click Contact Us page|Open enquiry form|PASS|
|Click Privacy Policy|Open Privacy Policy in new page|PASS|

## Newsletter Subscription

|Test Case|Expected behavior|PASS/FAIL|
|---------|-----------------|---------|
|Enter email address and click subscribe|Render mailchimp subscription confirmation page|PASS|


# Fixed Bugs

|Bug found|Problem|Solution|
|---------|-------|--------|
|Handling increase and decrease quantity in shopping bag|The quantity input field on the shopping page allowed negative values.|Updated the quantity-input.js file to enforce minimum and maximum value checks for the input field.|
|Handling the update button on the shopping bag page|The update button was not reflecting changes made to the increased or decreased quantity values.| Identified a mismatch between the class names used in the JavaScript and HTML, then corrected the class name.|
|Handling media file storage in AWS S3| Media files were not being stored in the S3 bucket after deploying the project.|Resolved the issue by reviewing and fixing bucket permissions.|
|Handling "Save Info" in the profile page|User information was not being saved in the "My Profile" page when the "Save Info" checkbox was selected during checkout.|Corrected a typo in the _save_info class in the HTML.|
|Handling Stripe payment integration|Payments were failing, and order details were not being created.|Found that the webhook event link was incorrect. Debugged the issue using print statements and fixed the URL.|
|Handling email notifications on successful payment| Emails were not being sent to users after a successful payment.|Discovered that the email backend was not properly configured in settings.py and corrected the configuration.|