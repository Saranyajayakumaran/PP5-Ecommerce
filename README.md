# WELLNESS NEST

Welcome to Wellness Nest, your one-stop online destination for wellness products. A E-commerce Drogerie Store is designed to provide users with a seamless and intuitive shopping experience for all their wellness needs. With a range of features for personalized shopping, secure transactions, and customer engagement, Wellness Nest offers a comprehensive digital solution for health-conscious shoppers.

The payment system uses Stripe. Please note that this website is for educational purposes do not enter any personal credit/debit card details when using the site. [Wellnessnest]()

The website is responsive on all screens

![Responsive image](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/documentation/Screenshots/wireframes/am%20i%20responsive.png)


# Table of Contents
- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
  - [Frontend](#frontend)
  - [Backend](#backend)
  - [Database](#database)
  - [Payment Gateway](#payment-gateway)
  - [Cloud Storage](#cloud-storage)
  - [Deployment](#deployment)
  - [Git and GitHub](#git-and-github)
  - [SMTP Email Integration](#smtp-email-integration)
- [Wireframes](#wireframes)
- [Features](#features)
  - [NavBar](#navbar)
  - [Home Page](#home-page)
  - [Product Page](#product-page)
  - [Product Detail Page](#product-detail-page)
  - [Testimonial Page](#testimonial-page)
  - [Shopping Bag Page](#shopping-bag-page)
  - [Contact Us Page](#contact-us-page)
  - [Wishlist Page](#wishlist-page)
  - [User Authentication](#user-authentication)
    - [Login Form](#login-form)
    - [Sign-Up Form](#sign-up-form)
  - [Checkout Page](#checkout-page)
  - [My Profile Page](#my-profile-page)
  - [Footer](#footer)
- [Future Development Features](#future-development-features)
- [Testing](#testing)
- [Business Model](#business-model)
  - [Revenue Streams](#revenue-streams)
  - [Value Proposition](#value-proposition)
  - [Channels](#channels)
  - [Customer Relationships](#customer-relationships)
- [Marketing Strategy](#marketing-strategy)
  - [SEO Strategy](#seo-strategy)
  - [Social Media Marketing](#social-media-marketing)
  - [Content Marketing](#content-marketing)
- [Agile Methodology](#agile-methodology)
  - [Benefits of Agile](#benefits-of-agile)
- [Django Framework Overview](#django-framework-overview)
  - [Project Setup](#project-setup)
  - [Project Structure](#project-structure)
  - [Models](#models)
  - [Views](#views)
  - [Static Files](#static-files)
  - [Admin Interface](#admin-interface)
- [Using Bootstrap](#using-bootstrap)
- [AWS S3 Bucket](#aws-s3-bucket)
- [Stripe Integration](#stripe-integration)
- [Heroku Deployment](#heroku-deployment)
- [SMTP Email Integration](#smtp-email-integration)
- [Credits](#credits)


# Technologies used 
**Frontend**
- HTML, CSS, JavaScript, Bootstrap for responsive design.

**Backend**
- Django framework for server-side logic and database management.

**Database**-
- PostgreSQL for storing user and reservation data.

**Payment Gateway**
- Stripe: Used for secure and seamless payment processing. Integrated for handling payments, subscriptions, and invoicing.

**Cloud Storage**
- AWS S3 (Amazon Simple Storage Service): Used for storing and serving static files (CSS, JS, images) and media files (user uploads). Ensures scalability, reliability, and reduced server load.

**Deployment**
- Deployed on a cloud platform Heroku for accessibility.

**GitHub**
- Web-based platform providing hosting services for Git repositories and collaboration tools.

**Git**
- A distributed version control system for tracking changes in source code

**SMTP Email Integration**
- Configured with SMTP servers to send email notifications for user registration, password resets, and more.


# wireframes
Wireframes are visual representations of the application's layout and structure. They serve as a blueprint for designing the user interface (UI) and help to communicate the app's functionality and user flow.

You can find the wirefarems of the project with the below link:

wireframes [wireframes](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/wireframes.md)

# Features
## NavBar

- **Logo and Website Title**:  
  - The navbar prominently displays the **logo** and the **title** of the website.  
  - The logo and title serve as a clickable link, redirecting users to the homepage.

- **Navigation Options**:  
  - The navbar contains clearly labeled navigation links, allowing users to quickly access different sections of the website.  
  - The available options include:  
    - **Home**: Redirects users to the homepage.  
    - **Products**: Leads to the product page where users can view all available items.  
    - **Testimonials**: Displays the testimonials page for users to view or submit feedback.  
    - **Wishlist**: Redirects logged-in users to their wishlist page.  
    - **Shopping Bag**: Takes users to their shopping bag to review or edit their selected items.  
    - **Contact Us**: Opens the contact page for submitting inquiries.

- **Search Bar**:  
  - A search bar is integrated into the navbar, allowing users to search for products or specific information across the website.  
  - Users can type their query and press enter or click the search icon to view search results.

![Navbar image](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/documentation/Screenshots/features/nav%20bar.jpg)

## Home Page

- The home page welcomes users with a brief message or tagline, providing an introduction to the site and its offerings.
- A prominently displayed "Shop Now" button encourages users to start exploring products immediately.
- It shows the delivery cost information below the nav bar.

![Home page](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/documentation/Screenshots/features/home%20page.jpg)

## Product Page

- **All Products Displayed**:  
    - The product page lists all the products available on the website.
    - Each product is presented with its image, name, description, size, and price, giving users comprehensive details at a glance.

- **Sorting Functionality**:  
    - Users can sort the products based on various criteria:
        - **Name:** Alphabetical order (ascending or descending).
        - **Category:** Organized by product categories (A-Z or Z-A).
        - **Price:** Low to high or high to low.
    - Each product image is clickable.
    - Clicking the image redirects the user to the Product Detail Page, where more detailed information about the selected product is displayed.

![Product page](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/documentation/Screenshots/features/product%20page.png)

## Product Detail Page

- **Product Information:**
    - Displays comprehensive details about the selected product, including:
        - **Product Name:** The name of the product.
        - **SKU:** The unique stock-keeping unit identifier for the product.
        - **Description:** A detailed description of the product.
        - **Price:** Price of the product in euros.

- **Wishlist Button:**
    - Allows users to add the product to their wishlist with a single click.
    - This feature is available only to logged-in users.

- **Quantity Selector:**
    - Users can adjust the desired quantity using Increase and Decrease buttons before adding the product to the bag.

- **Add to Bag Button:**
    - Users can add the product, along with the selected quantity, to the shopping bag.
    - On successful addition, users are notified or redirected based on the site flow.

- **Keep Shopping Button:**
    - Provides an option for users to return to the product listing or category page without adding the current product to their bag.

![Product detail page](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/documentation/Screenshots/features/product%20detail%20page.png)

## Testimonial Page

- **Submit Feedback** 
    - Users can share their feedback about products by submitting a testimonial.
    - Each testimonial includes details like the product name, review message, and the date it was created.

- **Add Testimonial Button**
    - A prominently displayed "Add Testimonial" button allows users to easily submit a new review.
    - Clicking this button redirects users to a form where they can write and submit their testimonials.

- **Edit and Delete Reviews**  
    - Users can edit or delete their own testimonials if they wish to update or remove their feedback.
    - Only the author of a testimonial and admin has the ability to edit or delete it, ensuring security and accountability.

- **Author-Specific Controls**  
    - Review actions (edit/delete) are displayed only for the logged-in user who authored the review.
    - Other users can view testimonials but cannot modify or delete them.

![Testimonial page](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/documentation/Screenshots/features/testimonial%20page.png)

## Shopping Bag Page

- **View Added Products**:  
   - Displays all the products added to the shopping bag by the user.
   - For each product, the following details are shown:  
    - **Product Image**: A thumbnail for easy identification.  
    - **Product Name**: The name of the product.  
    - **SKU**: A unique identifier for the product.  
    - **Price**: The price of a single unit.  
    - **Quantity**: The number of units selected by the user.  
    - **Total Price**: The calculated price for the product based on the selected quantity.

- **Modify Product Quantity**:  
  - Users can increase or decrease the quantity of a product directly from the shopping bag.  
  - Changes are dynamically updated, and the total cost is recalculated.

- **Remove Products**:  
  - Users can remove individual products from the bag with a "Delete" button.  
  - A confirmation prompt may be provided to prevent accidental deletions.

- **Proceed to Checkout Button**:  
  - Provides a clear call-to-action to proceed with the checkout process.  
  - Redirects users to the checkout page to complete their purchase.

- **Keep Shopping Button**:  
  - Allows users to navigate back to the product listing page or homepage to continue shopping.

![Shopping Page](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/documentation/Screenshots/features/shopping%20bag%20page.png)


## Contact us Page
- **Enquiry Form**  
    - The contact page features a form that allows users to submit their queries or feedback.
    - The form collects the following details:
        - **Type of Enquiry:** Users can select the nature of their enquiry (e.g., General, Product-related, Support).
        - **Name:** Users can provide their name for personalized communication.
        - **Email ID:** Users enter their email address so responses can be sent directly to them.
        - **Subject:** A brief title or subject line for the enquiry.
        - **Message:** A detailed message explaining the enquiry.
- After successfully submitting the form, users receive a confirmation email.
- The form ensures that all required fields are completed before submission, helping to prevent incomplete enquiries.

![Contact Us Page](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/documentation/Screenshots/features/contact%20us%20page.png)

## Wishlist Page

- **Restricted Access**  
    - The Wishlist page is accessible only to logged-in users.
    - Guests are required to log in or create an account to access and use the wishlist functionality.

- **Add to Wishlist** 
- Logged-in users can add products to their wishlist directly from the product detail page.
- This allows users to save items for future reference or purchase.

- **Product Details**
    - Each product in the wishlist is displayed with the following information:
        - **Product Image:** A thumbnail image of the product for easy identification.
        - **Product Name:** The name of the product.
        - **SKU:** The unique stock-keeping unit identifier for the product.

- **Delete from Wishlist:**
    - Users have the option to remove products from their wishlist.
    - A "Delete" button is available for each product to quickly manage the wishlist.

![wishlist page](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/documentation/Screenshots/features/wishlist%20page.png)

## User Authentication

## Login Form
- **User Access**:  
  - Allows registered users to log in securely to access their account and personalized features.  
  - Users need to provide their **email** or **USername** and **password** to log in.

- **Error Handling**:  
  - Displays error messages for invalid credentials (e.g., incorrect email or password).  
  - Ensures security by preventing unauthorized access.

- **Redirects After Login**:  
  - Users are redirected to the homepage or their last visited page after successful login.

  ![Login Page](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/documentation/Screenshots/features/login%20page.png)

## Sign-Up Form

- **Account Creation**:  
  - New users can create an account by providing:  
    - **Name** (optional, based on configuration).  
    - **Email Address** (used for login and communication).  
    - **Password** (must meet minimum security requirements).  

- **Field Validation**:  
  - Ensures all required fields are filled in and valid.  
  - Password strength is validated to ensure security.

![SignUp Page](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/documentation/Screenshots/features/signup%20page.png)

## Checkout Page

- **User-Friendly Checkout Form**:  
    - The checkout page includes a form where users can provide the following details:  
    - **General Information**:  
      - **Name**: Full name of the user.  
      - **Email Address**: For order confirmation and communication.  
    - **Delivery Details**:  
      - **Phone Number**: Contact number for delivery coordination.  
      - **Street Address**: Exact location for delivery.  
      - **Town/City**: Delivery city.  
      - **Postcode**: Zip or postal code.  
      - **Country**: Dropdown or auto-detected country field.

- **Order Summary**:  
  - Displays a summary of the order, including:  
    - **Products**: List of all items in the order, each with its name, quantity, and price.  
    - **Delivery Costs**: Additional charges if applicable.  
    - **Grand Total**: Total cost calculated, including delivery charges.

- **Save user information**
  - A checkbox which allow user to save the user entered details automatically to their personal profile.
  - The saved information will be displayed for next order.

- **Secure Payment with Stripe Integration**:  
  - The checkout page integrates with Stripe for secure and seamless payment processing.  
  - Users can input their payment details directly on the page using Stripe's secure payment widget.  
  - Sensitive payment information is encrypted and securely transmitted.

- **Secure Checkout**:  
  - The page is designed with user security in mind, ensuring that all personal and payment details are handled securely.

- **Adjust Bag Button**:  
  - Allows users to return to the Shopping Bag page to make modifications to their order before proceeding with payment.

![Checkout Page](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/documentation/Screenshots/features/checkout%20page.png)

## My Profile Page

- **User Information Storage**:  
  - The profile page securely stores all the information entered by the user during the checkout process.
  - Stored details include:  
    - **General Information**:  
      - **Name**: The user’s full name.  
      - **Email Address**: For account communication and order updates.  
    - **Delivery Details**:  
      - **Phone Number**: Contact number for delivery coordination.  
      - **Street Address**: Delivery address of the user.  
      - **Town/City**: City for delivery.  
      - **Postcode**: Zip or postal code.  
      - **Country**: Country for delivery.  

- **Edit Information**:  
  - Users can update their saved information directly from the profile page.  
  - An **Update Information** button allows users to modify their details easily.  
  - Changes are saved securely, ensuring the information is up-to-date for future orders.

- **Pre-Filled Checkout Form**:  
  - When placing new orders, the information from the profile page is automatically pre-filled in the checkout form for convenience.  

![My Profile Page](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/documentation/Screenshots/features/my%20profile%20page.png)

### Footer
- **Quick Links**:  
  - The footer provides quick access to all the key pages of the website:  
    - **Home**  
    - **Products**  
    - **Testimonials**  
    - **Wishlist**  
    - **Shopping Bag**  
    - **Contact Us**  
  - These links mirror the navigation options in the navbar, allowing users to access pages conveniently from the footer.

- **Contact Information**:  
  - The footer contains detailed contact information, including:  
    - **Email Address**: A clickable email link for direct communication.  
    - **Physical Address**: The business or service location for user reference.

- **Social Media Links**:  
  - Links to social media pages are displayed, allowing users to connect with the website on:  
    - **Facebook**  
    - **Instagram**  
    - **Twitter**  
    - **YouTube**  
  - These links are displayed as recognizable social media icons and open in a new tab.

- **Subscription Newsletter**:  
  - A subscription form is included, enabling users to sign up for newsletters with mailchimp:  
    - Users can input their email address to subscribe.  
    - A **Subscribe** button allows users to confirm their subscription.  
    - After subscribing, users receive a confirmation message or email.

![Footer image](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/documentation/Screenshots/features/footer.png)


## Future Development Features

### New Product Notification Feature
- Send email alerts to registered users about newly added products.
- Include product details like name, price, category, and a link to view the product.

### Highlights in Website UI:
- Add a "New Arrivals" section on the homepage or product page to showcase recently added items.

### Multi-Language and Multi-Currency Support

- Expand to international markets by providing:
    - Language options for global users.
    - Automatic currency conversion based on user location.

###  Chatbot Integration
- Add an AI-driven chatbot to assist users with:
    - Product inquiries.
    - Order tracking.
    - General customer support.

### Social Commerce Integration
- Enable users to shop directly through social media platforms like Instagram or Facebook.
- Add social sharing buttons for users to share products with friends.

### Wishlist
- Functionality to add product directly from wishlist.
- Allow users to share their wishlist with friends and family via:
    - Social media platforms (e.g., Facebook, Instagram, WhatsApp).
    - Direct links or email.

## Testing
Find the testing page in the below link

[Testing page](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/test.md)

## Business Model

Our e-commerce website operates on a direct-to-consumer model, offering a seamless platform for users to browse, shop, and purchase products. Below are the key components of our business model:

**Revenue Streams**
- Product Sales: Revenue is generated from the direct sale of products listed on the website.
- Delivery Charges: Additional revenue from shipping fees for specific regions or orders below a certain value.

**Value Proposition**
- Convenience: Customers can shop from a wide range of products anytime, anywhere.
- Personalization: Features like wishlists, testimonials, and user profiles offer a tailored shopping experience.
- Secure Payments: Integration with trusted payment gateways ensures safe and reliable transactions.

**Channels**
- Website: The primary platform for showcasing products and facilitating transactions.
- Social Media: Used to engage with customers and drive traffic to the website.
- Email Campaigns: Newsletters for product updates and promotions.

**Customer Relationships**
- Responsive Support: Through the contact page for inquiries and issues.
- Feedback Mechanisms: Testimonials and reviews to foster trust and improve services.

## Marketing Strategy
Our marketing strategy focuses on building brand awareness, engaging users, and driving traffic to the website through multiple channels. Key components include:

### SEO Strategy
SEO (Search Engine Optimization) is the process of improving a website’s visibility on search engines like Google, Bing, or Yahoo. The goal is to drive more organic (non-paid) traffic to a website by optimizing its content, structure, and performance to align with search engine algorithms.

- Keywords are integrated into product titles and descriptions to improve organic search rankings.
- Meta tags, robots.txt, and a sitemap have been implemented to ensure better visibility on search engines.

- Keywords used for this project:
    1. wellness
    2. selfcare
    3. relaxation
    4. fitness
    5. drogerie
    6. drug
    7. beauty
    8. haircare
    9. health
    10. drug store
    11. organic
    12. spa
    13. shampoo
    14. skincare
    15. natural
    16. healthy
    17. wellness essentials
    18. Self-love
    19. Personal Care
    20. Health hacks


### Social Media Marketing
- Promoting products and engaging users through platforms like Instagram, Facebook, and Twitter.
- Use visually appealing content, interactive posts, and paid ads to drive traffic.

### Facebook Page for Drogerie Store - Wellness Nest
We have created a dedicated Facebook page for Drogerie Store - Wellness Nest to engage with our audience, promote wellness products, and build a community focused on healthy living.
- **Product Promotions:** Showcase our range of wellness products with regular updates on new arrivals, discounts, and seasonal offers.
- **Community Engagement:** Interact with our customers, answer queries, and gather feedback to enhance user satisfaction.
- **Health and Wellness Tips:** Share valuable content like tips for healthy living, DIY wellness hacks, and product use guides.
- **Social Proof:** Highlight customer testimonials, reviews, and success stories.

![Facebook page image](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/documentation/Screenshots/facebook/wellnessnest1.png)


# ER Diagram
![ER diagram](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/documentation/Screenshots/ER%20diagram/er%20diagrma%20screenshot.jpg)

### Content marketing

### Search Engine Optimization (SEO):
Improving visibility on search engines with optimized keywords and mobile-friendly design.

### Social Media Marketing: 
Promoting products and engaging users through platforms like Instagram, Facebook, and Twitter.

### Email Campaigns: 
Sending newsletters, personalized recommendations, and abandoned cart reminders to re-engage users.

### Targeted Ads: 
Running Google Ads and social media campaigns to attract specific demographics.

## Agile Methodology

Our e-commerce platform development follows the Agile methodology, a flexible and iterative approach to project management and software development. Agile focuses on delivering value to customers through continuous collaboration, adaptability, and incremental improvements.

### Benefits of Agile:

- Faster delivery of usable features.
- Improved flexibility to adapt to changes.
- Enhanced team collaboration and productivity.
- Focused delivery on customer priorities.


# Django framework
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Here are the steps outlining how Django works:

- **Project Setup**
    - **Create a Project:** Use django-admin startproject projectname to create a new Django project.
    - **Create an App:** Within the project, use python manage.py startapp appname to create a new application.

- **Project Structure**
    - **Manage.py:** A command-line utility that lets you interact with your Django project.
    - **Settings.py:** Configuration for your Django project (database settings, installed apps, middleware, etc.)
    - **Urls.py:** URL declarations for the Django project; maps URLs to views.
    - **Wsgi.py:** Entry point for WSGI-compatible web servers to serve your project.

- **Models**
    - **Define Models:** Define your data models in models.py using Django’s ORM.
    - **Migrations:** Create migrations using python manage.py makemigrations and apply them with python manage.py migrate.

- **Views**
    - **Define Views:** In views.py, define the functions or classes that handle requests and return responses.
    - **Templates:** Use HTML templates to render views. Templates are stored in the templates directory.

- **URLs**
    - **URL Configuration:** In urls.py, map URL patterns to views. Include app-specific URLs using Django’s include() function.

- **Forms**
    - **Create Forms:** Use Django’s forms library to handle form rendering and validation.
    - **Handle Forms:** Process forms in views, validate inputs, and handle errors.

- **Static Files**
    -**Static Files:** Store CSS, JavaScript, and images in the static directory and serve them using Django’s static file management.

- **Admin Interface**
    - **Admin Site:** Use Django’s built-in admin interface to manage site content. Register models in admin.py to make them accessible in the admin interface.

- **User Authentication**
    - **Authentication System:** Use Django’s allauth authentication system for user login, logout, password management, and user registration.

- **Deployment**
- **Prepare for Deployment:** Configure settings for production (e.g., DEBUG=False), collect static files with python manage.py collectstatic, and use a WSGI server for deployment.

# Using Bootstrap  

Bootstrap is a powerful front-end framework for developing responsive and mobile-first websites. It includes HTML, CSS, and JavaScript components for creating common UI elements and layouts quickly and efficiently.

Why Use Bootstrap?

- **Responsive Design:** Bootstrap's grid system and responsive utilities ensure your website looks great on all devices.
- **Pre-styled Components:** Provides a wide array of pre-styled components such as buttons, forms, navigation bars, and more, which can be easily customized.
- **Cross-browser Compatibility:** Ensures your website works consistently across different browsers.
- **Easy to Use:** Simple integration with existing projects and extensive documentation for reference.

**How to Use**

- **Use Bootstrap CDN**
    - For quick integration and faster page loading, include Bootstrap via its CDN. This also ensures you always use the latest version of Bootstrap.

- **Leverage Bootstrap Grid System**
    - Utilize Bootstrap’s grid system to create responsive layouts. The grid system uses a series of containers, rows, and columns to layout and align content.

# AWS S3 Bucket

Django with AWS S3 integration allows seamless storage and retrieval of static files (CSS, JavaScript, images) and media files (user uploads) using Amazon's Simple Storage Service (S3). This approach is highly scalable, cost-effective, and ensures reliable access to files.

- **Static and Media File Storage:** Store all static files and user-uploaded media in S3 buckets.
- **Scalability:** S3 handles large volumes of data effortlessly, making it ideal for scaling Django applications.
- **Security:** Secure your files with AWS IAM policies and bucket permissions.
- **Performance:** Reduce server load and latency by serving files directly from S3, often combined with AWS CloudFront (CDN) for faster content delivery.

# AWS Set Up

- **AWS S3 Bucket Creation:**
  - Create an S3 bucket on AWS.
  - Configure bucket policies and CORS for secure access.

- **Django Configuration:**
  - Install boto3 and django-storages packages.
  - Update Django settings ( **settings.py** )  to use S3 for static and media files:

***AWS_ACCESS_KEY_ID = 'your-access-key-id'***

***AWS_SECRET_ACCESS_KEY = 'your-secret-access-key'***

***AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'***

***AWS_S3_REGION_NAME = 'your-region'  # e.g., 'us-east-1'***

***STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'***

***DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'***

# Stripe Integration

This project integrates Stripe, a leading online payment processing platform, to handle secure and seamless payment transactions. Stripe enables businesses to accept payments via credit cards, debit cards, and various other payment methods.

**How It’s Used:**

**Payment Gateway:** The application utilizes Stripe as the primary gateway for processing payments.
**Checkout Process:** Secure and customizable Stripe Checkout is implemented for user transactions.
**Webhooks:** Stripe webhooks are used to handle events like payment success, failure, and refunds.

## Stripe API Keys

Stripe uses two types of API keys:

**Publishable Key:** Used on the frontend for client-side operations.
**Secret Key:** Used on the backend for server-side operations.

It’s recommended to store API keys securely in environment variables. [stripe dashboard](https://dashboard.stripe.com/login?redirect=%2Fapikeys)

STRIPE_PUBLISHABLE_KEY=pk_test_51HXYZabc...

STRIPE_SECRET_KEY=sk_test_51HXYZdef...

![stripe functinality](https://github.com/Saranyajayakumaran/PP5-Ecommerce/blob/main/documentation/Screenshots/stripe%20integration/stripe%20payment%20integration.png)

# Heroku Deployment

The app was deployed through Heroku. The steps are as follows:

- **Log into Github and locate Github Repository.**
    - If you haven't already, sign up for a Heroku account at Heroku's website.

- **Create a Heroku Account:**
    - If you haven't already, sign up for a Heroku account at Heroku's website.

- **Create a New Heroku App:**
    - Log into your Heroku account.
    - From the Heroku dashboard, click on the "New" button to create a new app.
    - Choose a unique name for your app.
    - Select the region closest to your location.
    - Click "Create app" to finalize the creation.

- **Configure App Settings:**
    - Go to your newly created app's settings.
    - Navigate to the "Config Vars" section.
        - Add the following Config Vars in Heroku:
        
        
|Variable name|Value|
|-------------|-----|
|AWS_ACCESS_KEY_ID| From AWS CSV file|
|AWS_SECRET_ACCESS_KEY| From AWS CSV file|
|DATABASE_URL|Postgres generated URL|
|EMAIL_HOST_PASS| Password from the email client |
|EMAIL_HOST_USER| Site's email address|
|SECRET_KEY|Random key generated and used in django|
|STRIPE_PUBLIC_KEY| Stripe Dashboard > Developers tab > API Keys > Publishable key |
|STRIPE_SECRET_KEY| Stripe Dashboard > Developers tab > API Keys > Secret key|
|STRIPE_WH_SECRET| Stripe Dashboard > Developers tab > Webhooks > site endpoint > Signing secret|
|USE_AWS| True|

    - Add any necessary environment variables that your application requires.
    - Postgres database link and secret key as same as in the django app
    - Ensure that you have configured the necessary build packs for your application.

- **Deploy Your Application:**
    - Scroll down to the "Deployment Method" section on your app's dashboard.
    - Select GitHub as the deployment method.
    - Connect your Heroku app to your GitHub repository by searching for and selecting the repository name.
    - Optionally, enable automatic deployment if you want your Heroku app to update automatically whenever changes are pushed to the connected GitHub repository.
    - Click the "Deploy Branch" button to manually deploy your application for the first time.

# SMTP Email Integration

### Configuration

To configure SMTP for this project, follow the steps below:

- **Add Email Settings:**

Configure the following variables in your settings.py file or use environment variables for sensitive information:

***EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'***

# SMTP Server Configuration

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = 587              
EMAIL_USE_TLS = True          
EMAIL_USE_SSL = False        

EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'

**Default "From" Email Address**

DEFAULT_FROM_EMAIL = 'Your Website Name <your-email@example.com>'

***Important!*** Use environment variables to store sensitive credentials.


# Credits
- I would thank many sources and people who supported to complete my project.
    - Thank my mentor Dick vlaanderen who guided me and his ideas and corrections were very helpful.
    - W3schools and Stackoverflow plays a major role in learning the concepts.[W3C schools](https://www.w3schools.com/) 
    - Authenication,signup and product management ,deployment methods are followed from blog project[boutique ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/933797d5e14d6c3f072df31adf0ca6f938d02218) 
    - Bootstrap classes Utilized from the Bootstrap documentation[Bootstrap](https://getbootstrap.com/) 
    - Some more youtube channels too get idea of e commerce project[desphis](https://www.youtube.com/@desphixs) 
      [codemy](https://www.youtube.com/watch?v=A0mSfYDH-nY)