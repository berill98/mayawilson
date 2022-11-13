# Maya Wilson Photography

Welcome to Maya Wilson Photography!
Users can browse and purchase the different photography packages and make an enquiry. They can also learn more about the photographer.

The payment system uses Stripe. Please note that this website is for educational purposes do not enter any personal credit/debit card details when using the site.

To test this system, test card details can be used. A list of these can be found in Stripe's documentation [here](https://stripe.com/docs/testing#cards).

The live link can be found here - [Maya Wilson](https://mayawilson.herokuapp.com/)

## Site Owner Goals

- To provide  information about the available photo packages.
- To promote herself as a photographer.
- To encourage users to create an account.
- To encourage users to buy photo sessions.
- To present the user with a website that is responsive and easy to use.

## User stories

As a first-time user:

-	I want to understand the main purpose of the website easily
-	I want to be able to navigate throughout the site.
-	I want to enjoy nice and clean design and style that is inline with the subject of the site.
-	I want to learn more about the photographer and her story
-	I want to view a list of the available photo packages
-	I want to view individual package details
-	I want to easily register for an account, if I want to return later

As a registered user:

-	I want to easily login or logout
-	I want to easily recover my password in case I forget it
-	I want to receive an email confirmation after registering
-	I want to have my own user profile
-	I want to be able to add a photo package to my shopping bag
-	I want to easily select a date for my photography session when purchasing it
-	I want to view the package in my bag
-	I want to easily enter payment information
-	I want to feel my personal and payment information is safe and secure
-	I want to view an order confirmation after checkout
-	I want to see my order history in my profile

As an admin:

-	I want to be able to add a new photography package
-	I want to edit/update a package
-	I want to delete a package

User stories not yet implemented:
-   As a first-time user, I want to find the photographer's whole portfolio on the site.
-   As a registered user, I would like to be able to leave reviews.

## UX

### Fonts

- I have used Google Fonts to find the font that suits best to the feel of the website. I have used [Cedarville Cursive](https://fonts.google.com/specimen/Cedarville+Cursive) for the logo and the main titles and [Roboto](https://fonts.google.com/specimen/Roboto) for the page contents.

### Icons

- The icons on the website were taken from [FontAwesome](https://fontawesome.com/).

### Colors

- The main colours on the website are brown, white, and dark green. This is because I wanted a simple, clean design with natural colours.

### Wireframes

Hand-drawn wireframes.
<details><summary><b>Wireframes</b> (click to expand)</summary>

- [Home Page]()
- [Login Page]()
- [Registration Page]()
- [About Page]()
- [Contact Page]()
- [Packages Page]()
- [Package Details Page]()
- [Checkout Page]()
- [Profile Page]()

</details>

## Features

### Existing Features

#### Design

- A clean and simple design and layout with consistency throughout.
- Responsive design allowing users to use site across all devices.

![Design](docs/readme_images/home.png)

#### Header
1. Navbar
- Easy navigation by using the navigation bar. Nav links are clearly idenfied both on desktop and when sidenav is expanded on smaller the devices.

![Navbar](docs/readme_images/navbarlarge.png)
![Navbar](docs/readme_images/navbarsmall.png)

2. Logo
- The leaf logo is positioned in the top left of the header and is linked to the home pagefor help the navigation of the users.

![Logo](docs/readme_images/logo.png)

3. User icon
- The User icon is a drop down menu which includes the Sign up and Log in links. Once a user is logged in, the options will change to My Profile and Logout. If the user is superuser Package Management becomes available in the dropdown menu.

![Icons](docs/readme_images/icons.png)
![Dropdown](docs/readme_images/accountfornotloggedin.png)

4. Bag icon
- It is on the right side of the header next to the user icon. Once a package is added to the basket a number displaying the total price appears, and the colour changes into green.
Once a product is added to the bag, a number displaying the total quantity of items appears, located at the top right of the bag icon. Clicking the bag icon navigates the user to the checkout page which displays the added package and the checkout form.

![Icons](docs/readme_images/baggreen.png)

#### Home page

- The home page includes a call to action button which encourages the user to 'Book now'.

![Home](docs/readme_images/home.png)

#### About page

- The About page includes a little introduction from the photographer and two photos of her portfolio.

![About](docs/readme_images/about.png)

#### Packages page

- Each package card shows an image, its name and price.
- If the user is a superuser, edit and delete buttons will appear at the bottom of the card.
- If the user clicks on the card it will take them to the package details page.

![Packages](docs/readme_images/packages.png)

#### Package details page

- The package details page displays the image, name, price, package details details like photos included, duration time and a short description.
- If the user is a superuser, edit and delete buttons will appear.
- If the user is logged in a date input field and a disabled quantity field will appear along with the Book this package button.

![Package detail](docs/readme_images/packagedetail.png)

#### Package Management

1. Add package
- The add package page can be accessed by clicking the 'Package Management' button in the user dropdown meneu and is only visible to superusers.
- If a user tries to add a product without being a superuser they are redirected to the home page.
- The user must fill out all the fields that have an Asterix. If the form is submitted with any of these fields left blank or with just whitespace then an error message will appear above that particular field, notifying the user of the issue.
- The user can add a photo if they wish. If they choose not to, a default image displays as their package image.
- Clicking the 'Add Package' button at the bottom of the form will create the package.
- The user will receive a success message notifying them that the product has been successfully added.

![Add package](docs/readme_images/addpackage.png)

2. Edit a package
- The superuser can edit a Package by clicking the edit button on the package card or on the package detail page.
- The form opens with all fields populated with the original content.
- If a user tries to add a package without being a superuser they are redirected to the home page.
- Clicking the 'Update Package' button at the bottom of the form will update the package with the changes.
- The superuser will receive a success message notifying them that the package has been successfully updated.

![Edit package](docs/readme_images/editpackage.png)

3. Delete a package
- The superuser can choose to delete a package by clicking the delete button on the package card or on the package detail page.
- The superuser will receive a success message notifying them that the package has been successfully deleted.

![Delete package](docs/readme_images/deletepackage.png)

#### Contact page

- A user can open up the contact form by clicking on the "Contact" button in the navbar.
- The user must fill out all the fields that have an Asterix. If the form is submitted with any of these fields left blank or with just whitespace then an error message will appear above that particular field, notifying the user of the issue.
- When the form is submitted, the user is taken to the confirmation page.

![Contact](docs/readme_images/contact.png)

#### Login, logout

- Users of the site can create an account and verify their email address. (Link emailed to the address they provided)
- Users can login into their existing account.
- Users can logout of their account.
- Users can reset their password if they forget it.
- Success messages inform the user if they have logged in/logged out successfully.

![Login](docs/readme_images/login.png)
![Logout](docs/readme_images/logout.png)
![Register](docs/readme_images/register.png)

#### My profile

- Logged in users have access to their profile, where they can view their order history.

![My profile](docs/readme_images/profile.png)

#### Checkout

- The user can fill out a form with their contact details, address and card number.
- The user must fill out all the fields that have an Asterix. If the form is submitted with any of these fields left blank or with just whitespace then an error message will appear above that particular field, notifying the user of the issue.
- The user can see a summary of their purchase, the package name, the booked date and the total price.
- Clicking the package image in the summary will take the user to that product's detail page.

- The card payment is handled by Stripe to ensure secure payment.
- Incorrect card numbers will automatically show an invalid card number error.
- A loading screen will appear when a payment is being processed to stop the user clicking away.
- There is a warning message at the bottom of the page informing the user of how much their card is about to be charged.
- When the form is submitted, the user is taken to the confirmation page.

![Checkout](docs/readme_images/checkout1.png)
![Checkout](docs/readme_images/checkout2.png)

### Defensive Programming

To protect the site and defend against any "brute force", I added some defensive programming:
-   Where I have used function based views I have used Django's login_required decorator to restrict access as required. 
-   Check if a user is logged in. This checks if tuser is logged in, if so allows the user to perform the action. If not will redirect user to the appropriate page.
-   Check if user is superuser (is admin). The admin is the only one who can add, edit and delete packages. If the check fails, the user is redirected and a message displayed.
-   Certain action buttons are only displayed to certain users, for example 'Package management' is only displayed to superusers. Only logged in user can add any package to their basket.
-   If incorrect or empty data is added to a form, the form won't submit and a warning will appear to the user informing them what field raised the error.
-   The database url and secret key are stored in the env.py file to prevent unwanted connections to the database. Stripe keys are also stored in the env.py file. 
-   Cross-Site Request Forgery (CSRF) tokens were used on all forms throughout this site.

### Features left to implement

- An option for newsletter signup.
- Users to have ability to delete their account.
- A portfolio page.
- Users to have ability to leave reviews.
- Enquiries dashboard for the superusers.

## Structure of the site

The structure of the site has been developed to enable users to access and use the site with ease.
- Home Page- accessible by all users, whether logged in or not. 
- Navbar - is accessible to all users. The navbar changes to a sidenav on tablet screens and smaller for responsiveness. The options available under the account icon change depending on whether a user is logged in or not.

    * For logged in users:  
![Account icon for logged in users](docs/readme_images/accountforusers.png)
    * For not logged in users:  
![Account icon for not logged in users](docs/readme_images/accountfornotloggedin.png)
    * For admin:  
![Account icon for admin](docs/readme_images/accountforadmin.png)

- The About page is accessible to all users, whether logged in or not.
- The Contact page is accessible to all users, whether logged in or not.
- List of packages and the details of the packages are accessible to all users, whether logged in or not.
- Book this package button and the Checkout page are only accessible to registered users.
- Edit and delete package buttons are only accessible to superusers.ir order history.
- Checkout page is only accessible to logged in users once they have a package in their basket.

![Database Schema Diagram]()

## Technologies used

### Languages

- Python
- HTML5
- CSS3
- Javascript

### Frameworks, Tools and Libraries

- [Django](https://www.djangoproject.com/)
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [Stripe](https://stripe.com/ie)
- [AWS](https://aws.amazon.com/?nc2=h_lg)
- [Heroku](https://dashboard.heroku.com/login)
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
- [Font Awesome](https://fontawesome.com/)
- [GitHub](https://github.com/)
- [Google Fonts](https://fonts.google.com/)
- [W3C](https://www.w3.org/)
- [Jshint](https://jshint.com/)
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/)

## Testing

To view all testing documentation please refer to [TESTING.md](TESTING.md).

## Deployment

### Heroku

I followed the following steps to deploy this pwebsite to Heroku:

#### Create a Heroku App:
- Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account.
- On the main page click the button labelled New in the top right corner and from the drop-down menu select "Create New App".
- Enter a unique app name.
- Then select your region.
- Click on the Create App button.

#### Attach the Postgres database:
- In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
- Copy the DATABASE_URL located in Config Vars in the Settings Tab.
- Go back to your IDE and install 2 more requirements:
    - `pip3 install dj_databse_url`
    - `pip3 install psycopg2-binary` 
- Create requirements.txt file by typing `pip3 freeze --local > requirements.txt`
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file. 
- In settings.py file import dj_database_url, comment out the default configurations within database settings and add the following: 

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
```
- Run migrations and create a superuser for the new database. 
- Create an if statement in settings.py to run the postgres database when using the app on heroku or sqlite if not

```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
    }
```

- Create a file named "Procfile" in the main directory and add the following: `web: gunicorn project-name.wsgi:application`
- Add Heroku to the ALLOWED_HOSTS list in the main settings.py in the following format ['app_name.heroku.com', 'localhost']

- Then push these changes to GitHub.

#### Updating Heroku Config Vars
Add the following Config Vars in Heroku:

|     Variable name     |                           Value/where to find value                           |
|:---------------------:|:-----------------------------------------------------------------------------:|
| AWS_ACCESS_KEY_ID     | AWS CSV file(instructions below)                                               |
| AWS_SECRET_ACCESS_KEY | AWS CSV file(instructions below)                                               |
| DATABASE_URL          | Postgres generated (as per step above)                                        |
| EMAIL_HOST_PASS       | Password from email client                                                    |
| EMAIL_HOST_USER       | Site's email address                                                          |
| SECRET_KEY            | Random key generated as above                                                 |
| STRIPE_PUBLIC_KEY     | Stripe Dashboard > Developers tab > API Keys > Publishable key                |
| STRIPE_SECRET_KEY     | Stripe Dashboard > Developers tab > API Keys > Secret key                     |
| USE_AWS               | True (when AWS set up - instructions below)                                   |

#### Deploy
- Ensure in settings that DEBUG is False
- Go to the deploy tab on Heroku and connect to GitHub, then choose the needed repository. 
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
- Click View to view the deployed site.

The site is now live.

#### AWS Set Up

- Create an AWS account or login if you have one.
- From the 'Services' tab on the AWS Management Console, search 'S3' and select it.
- Click 'Create a new bucket', give it a name (preferably the same as your Heroku app name), and choose the region closest to you.
- Under 'Object Ownership' select 'ACLs enabled' and leave the Object Ownership as Bucket owner preferred.
- Uncheck block all public access and acknowledge that the bucket will be public.
- Click 'Create bucket'.
- Open the created bucket, go to the 'Properties' tab. Scroll to the bottom and under 'Static website hosting' click 'edit' and change the Static website hosting option to 'enabled'. Copy the default values for the index and error documents and click 'save changes'.
- Open the 'Permissions' tab, locate the CORS configuration section and add the following code:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
- In the 'Bucket Policy' section and select 'Policy Generator'.
- Choose 'S3 Bucket Policy' from the type dropdown.
- In 'Step 2: Add Statements', add the following settings:
    - Effect: Allow
    - Principal: *
    - Actions: GetObject
    - ARN: Bucket ARN (copy from S3 Bucket page)
- Click 'Add Statement'.
- Click 'Generate Policy'.
- Copy the policy that appears
- Paste the generated policy into the Permissions > Bucket Policy area.
- Add '/*' at the end of the 'Resource' key, and save.
- Go to the 'Access Control List' section click edit and enable List for Everyone (public access) and accept the warning box.

#### IAM
- From the 'Services' menu, search IAM and select it.
- Once on the IAM page, click 'User Groups' from the side bar, then click 'Create group'. Choose a name and click 'Create'.
- Go to 'Policies', click 'Create New Policy'. Go to the 'JSON' tab and click 'Import Managed Policy'. 
- Search 'S3' and select 'AmazonS3FullAccess'. Click 'Import'.
- Get the bucket ARN from 'S3 Permissions' as per above.
- Delete the '*' from the 'Resource' key and add the following code into the area:

```
"Resource": [
    "YOUR-ARN-NO-HERE",
    "YOUR-ARN-NO-HERE/*"
]
```

- Click 'Next Tags' > 'Next Review' and then provide a name and description and click 'Create Policy'.
- Click'User Groups' and open the created group. Go to the 'Permissions' tab and click 'Add Permissions' and then 'Attach Policies'.
- Search for the policy you created and click 'Add Permissions'.
- You need to create a user to put in the group. Select users from the sidebar and click 'Add user'.
- Give your user a user name, check 'Programmatic Access'.
- Click 'Next' and select the group you created.
- Keep clicking 'Next' until you reach the 'Create user' button and click that.
- Download the CSV file which contains the AWS_SECRET_ACCESS_KEY and your AWS_ACCESS_KEY_ID needed in the Heroku variables as per above list and also in your env.py.

### Connecting S3 to Django 
- Go back to your IDE and install 2 more requirements:
    - `pip3 install boto3`
    - `pip3 install django-storages` 
- Update your requirements.txt file by typing `pip3 freeze --local > requirements.txt` and add storages to your installed apps.
- Create an if statement in settings.py 

```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'insert-your-bucket-name-here'
    AWS_S3_REGION_NAME = 'insert-your-region-here'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

```
- Then add the line 

    - `AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'` to tell django where our static files will be coming from in production.

- Create a file called custom storages and import both our settings from django.conf as well as the s3boto3 storage class from django storages. 
- Create the following classes:

```
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

- In settings.py add the following inside the if statement:

```
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

```

- Then add the following at the top of the if statement:
```
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
```

- Go to S3, go to your bucket and click 'Create folder'. Name the folder 'media' and click 'Save'.
- Inside the folder, click 'Upload', 'Add files', and then select all the images that you are using for your site.
- Then under 'Permissions' select the option 'Grant public-read access' and click upload.
- Your static files and media files should be automatically linked from Django to your S3 bucket.

## Credits

### Media

| Media  | Photographer  | Link |
| :------------ |:---------------:| -----:|
| Standard package photo | Jessica Rockowitz | [Unsplash](https://images.unsplash.com/photo-1542037012038-5f9fb2b3c681?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80) |
| Mini package photo | Jessica Rockowitz | [Unsplash](https://images.unsplash.com/photo-1643130420647-bbb7bc1b695a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80) |
| Premium package photo | Jessica Rockowitz | [Unsplash](https://images.unsplash.com/photo-1542036571694-e620974a6b5a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80) |
| Photo on About page | Jessica Rockowitz | [Unsplash](https://images.unsplash.com/photo-1642272288582-c183724556d6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80) |
| Photo on About page | Jessica Rockowitz | [Unsplash](https://images.unsplash.com/photo-1542036899624-42218b01ec1f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80) |

### Resources used

- [W3Schools](https://www.w3schools.com/)
- [Django Docs](https://docs.djangoproject.com/en/4.0/)
- [Bootstrap 4.6 Docs](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [Stack Overflow](https://stackoverflow.com/)
- [Code Institute - Boutique Ado Walkthrough Project](https://github.com/Code-Institute-Solutions/boutique_ado_v1)

## Acknowledgments

My mentor Tim for his support, advice and feedback.