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
|Click Category badge||Display all products in specific category|PASS|
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
|Case 1|Enter valid inputs in checkout form 
"name:Test",
"email:test@test.com",
"Phone neumber:01234567890",
"streetaddress1: test street1",
"streetaddress2: test street2",
"town or city: stuttgart",
"Postalcode:123456",
"country:Germany" and "Payment:42424242424242424"
click complete order|  Order should complete and display order details and send email to the email address specified in the form"|PASS|
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

|Testcase|User Input|Expected behavior|PASS/FAIL|
|--------|----------|-----------------|---------|
|



 




