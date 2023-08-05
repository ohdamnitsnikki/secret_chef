# Secret Chef -  Testing

Visit the deployed site: [Secret Chef](https://kera-cudmore.github.io/TheQuizArms/)

- - -

## CONTENTS

* [AUTOMATED TESTING](#automated-testing)
  * [W3C Validator](#w3c-validator)
  * [JavaScript Validator](#javascript-validator)
* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)

Throughout the entire build, testing was a continuous process. I relied on Chrome developer tools to identify and resolve any issues that arose during the development phase.

To ensure the smooth functioning of the project, I actively used Google developer tools, employing them for troubleshooting whenever things didn't work as anticipated.

The console in the developer tools proved to be valuable in working through specific sections of JavaScript, guaranteeing the functionality of the code and pinpointing any potential issues.

Furthermore, I thoroughly checked each page using both Google Chrome developer tools and Firefox inspector tool to confirm responsiveness across various screen sizes and devices.

- - -

## AUTOMATED TESTING

### W3C Validator

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the website. It was also used to validate the CSS.

* [base.html](testing/w3/w3-index.png) - Five errors regarding the fact that the validator doesn't understand the way you style django apps.
* [about.html](testing/w3/w3-game.png) - Two errors and one warning, all of them considered the fact that the validator doesn't undertsand the extend base template.
* [index.html](testing/w3/w3-highscores.png) - Three errors and one warning regarding the fact that the validator doesn't understand the way you style django apps.
* [blog_post_success.html](testing/w3/w3-404.png) - Three errors and one warning regarding the fact that the validator doesn't understand the way you style django apps.
* [create_blog_post.html](testing/w3/w3-500.png) - Two errors and one warning, all of them considered the fact that the validator doesn't undertsand the extend base template.
* [edit_posts.html](testing/w3/w3-500.png) - Two errors and one warning, all of them considered the fact that the validator doesn't undertsand the extend base template.
* [user_posts.html](testing/w3/w3-500.png) - Thirteen errors and one warning regarding the fact that the validator doesn't understand the way you style django apps.

* [style.css](testing/w3/w3-css.png) - Passed, no errors found.

- - -

### JavaScript Validator

[jshint](https://jshint.com/) was used to validate the JavaScript.

* [base.html](testing/jshint/jshint-javascript.png) - Passed with two warnings. 
* [index.html](testing/jshint/jshint-game.png) - Passed.
* [user_posts.html](testing/jshint/jshint-highscores.png) - Passed.

- - -

## MANUAL TESTING

### Testing User Stories

`First Time Visitors`

| Goals | How are they achieved? | Image |
| :--- | :--- | :--- |
| As a first time user, I want to easily understand the page I'm on | To achieve good UX the index page renders a slideshow of all the food images from the blog posts. | ![Index page](media/shop_now_button.png) |
| As a first time user, I want to easily navigate through out the page | To make a userfriendly page the navbar has clear links for home, blogposts and the about page. | ![Navbar](media/navbar.png) |
| As a first time user, I want to be able to sign up to the site and create a profile | Users can create their own profile for the site by using the sign up page. Links to the sign up page are included on the navbar. | ![sign up link](media/register_link.png) |
| As a first time user, I want to be able to read blog posts | Users can read blogposts by using the blog posts link. | ![Blog posts](media/register_link.png) |
| As a first time user, I want to be able to read about the blog | Users can read the about section by using the about link. | ![About Section](media/register_link.png) |
| As a first time user, I want to be able to follow the blog on social media | Users can use the links in the footer to reach the blogs social media. | ![Footer](media/register_link.png) |


`Returning Visitors`

| Goals | How are they achieved? | Image |
| :--- | :--- | :--- |
| As a returning user, I want to being able to log out from my account. | When users are logged in the links in the navbar changes from register/login to logout. | ![Logout](media/shop_now_button.png) |
| As a returning user, I want to being able to create blogposts. | Users can use a form to create a blogpost. | ![Write a post](media/navbar.png) |
| As a returning user, I want to be able to edit and delete my posts | Users can edit and delete there own blogposts | ![Edit and Delete](media/register_link.png) |

`Admin`

| Goals | How are they achieved? | Image |
| :--- | :--- | :--- |
| As a admin, I want to being able to decide which posts to post. | From the admin panel the admin decides on which posts to post and not. | ![Admin posts](media/shop_now_button.png) |
| As a admin, I want to being able to edit and deleter posts. |Admin can choose to edit and delete posts after the rendered on the blog. | ![Edit and Delete](media/navbar.png) |
| As a admin, I want to be able to create posts | Admin can create a post the same way as an user or through the adimn panel| ![Admin post](media/register_link.png) |

- - -

### Full Testing

Full testing was performed on the following devices:

* Laptop:
  * Asus
* Mobile Devices:
  * iPhone 13 pro.
  * iPhone 11 pro.
  * Samsung S 21 Ultra.

Each device tested the site using the following browsers:

* Google Chrome
* Safari
* Firefox

Additional testing was taken by friends and family on a variety of devices and screen sizes. They reported no issues while creating blog posts or going through the page.

`The navbar`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| The Sites title | Link directs the user back to the home page | Clicked title | Home page reloads | Pass |
| Home link | Link directs the user back to the home page | Clicked link | Home page reloads | Pass |
| Blog Posts link | Link directs user to blog posts page | Clicked link | Blog page opens | Pass |
| About link | Directs the user to the about section | Clicked link | About page opens | Pass |
| Login/Register links | Directs the user to login/register page | Clicked link | Directs user to login/register page | Pass |
| Logout link (if user is logged in) | Directs the user to logout page | Clicked link| Directs the user to logout page| Pass |
| Write a Post link (if user is logged in) | Directs the user to blog post form page | Clicked link | Opens blog form | Pass |

`The Footer`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| The Instagram Icon | Link opens social media in a new window | Clicked icon | Opens socialmedia in a new window | Pass |
| The Facebook Icon | Link opens social media in a new window | Clicked icon | Opens socialmedia in a new window | Pass |
| The Youtube Icon | Link opens social media in a new window | Clicked icon | Opens socialmedia in a new window | Pass |

`Blog Posts page (if user is author or staff)`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| The Edit button | Link directs the user to a update blog post form | Clicked button | Directs user to the edit form | Pass |
| The Delete button | Link opens a "Are you sure you want to delete modal" | Clicked button | Opens modal | Pass |
| The (Delete Modal) NO button | Closes modal with no actions | Clicked button | Close modal | Pass |
| The (Delete Modal) Close icon button| Closes modal with no actions | Clicked button | Close modal | Pass |
| The (Delete Modal) Yes button| Closes modal and removes post | Clicked button | Close modal and removed post | Pass |
| The (Delete Modal) click next to the modal| Closes modal with no actions | Clicked next to modal | Close modal | Pass |

`Register/login/logout`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| The Register page | Renders four text areas that activates when clicked | Clicked area | Activates form | Pass |
| The Register page | Signup button that creates user when form is filles | Clicked button | User created | Pass |
| The Register page | Renders a link to singin page| Clicked link| Redirects user to singin page | Pass |
| The Login page | Renders two text areas that activates when clicked | Clicked area | Activates form | Pass |
| The Login page | Signin button that signs user in | Clicked button | User signed in | Pass |
| The Login page | A radio button for remember me | Click button | Page remembers user | Pass |
| The Login page | Link to register form | Click link | Redirects user to register page | Pass |
| The Logout page | Sign out button for signing user out | Clicked button | User gets signed out| Pass |

`Write a post page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Text Areas | Activates when clicked | Clicked area | Activated textfield | Pass |
| Dropdown Menu | Shows category options| Clicked menu | Renders options | Pass |
| Select file button | Opens source to add an image | Clicked button | Opens library | Pass |
| Create Post button (if user failed filling out the form) | Redirects user to the failed field | Clicked button| Redirects to the failed field | Pass |
| Create Post button | Redirects user to the success page | Clicked button | Redirects to the success page | Pass |

`Edit post Page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Text Areas | Activates when clicked for admin and author to edit | Clicked area | Activated textfield | Pass |
| Dropdown Menu | Shows category options| Clicked menu | Renders options | Pass |
| Save button | Redirects user to the blog posts page page | Clicked button | Redirects to the blog posts page | Pass |

Back to [README.md](README.md)