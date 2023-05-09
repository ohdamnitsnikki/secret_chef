# Secret Chef!

Secret Chef is a website for sharing recipes with other secret chefs at home. The site targets everyone who likes to impress their guests with good food and would like to improve their cooking and baking skills.

## CONTENTS

* [How does Secret Chef work?](#what-does-the-app-do)
* [Styling that are consistent on the app](#consistent-styling)
  * [Navigation](#navigaion-bar)
  * [Header](#header)
  * [Footer](#footer )

* [Element styling that aren't consistent](#the-windows)
  * [Home](#home)
  * [About](#about)
  * [Register](#register)
* [Admin panel](#admin-panel)
* [Features](#features)
* [Features left to implement](#features-left-to-implement)
* [Testing](#testing)
* [Credits](#credits)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

  ## What does the app do?
* As a user just visiting the page you are able to read the admins blog posts and comments and also view the amount of likes a post have. But as a logged in user you are able to:
   * Comment on the posts and by that being able to conversate with other users.
   * Like and unlike posts.

## Consistent styling 

### Navigation Bar
* The navigation bar includes responsive links to the home, about, login, logout and register page. 
<img
  src="assets/images/navigation-bar.png"
  alt="The Navbar" 
  title="The Navbar"
  style="display: block; margin: 0 auto; max-width: 500px">
  
### Header- Seret Chef!
* The header containes the applications name 
<img
  src="assets/images/header.png"
  alt="The Header" 
  title="The Header"
  style="display: block; margin: 0 auto; max-width: 300px">


### Footer
* The Footer has navigation links that opens in a new window when used. One to our Facebook page, one for Instagram and one to our youtube chanel. 
<img
  src="assets/images/footer.png"
  alt="The Footer" 
  title="The Footer"
  style="display: block; margin: 0 auto; max-width: 500px">

**These elements are constant on each page for easy navigation.**

## The windows 

### Home Page 

* The home page is where you can see the blogposts thats been posted, the author of the post, what time and date it was and how many likes the post has.

<img
  src="assets/images/home.png"
  alt="Baby Care information cards" 
  title="Baby Care information cards"
  style="display: block; margin: 0 auto; max-width: 500px">

1. By pressing the title of the post in this case "Scones" you'll enter that specific post.
2. From here you can read the description of the recipe. 
3. You can also read the comments and comment if your a user.
<img
  src="assets/images/description.png"
  alt="Baby Care information cards" 
  title="Baby Care information cards"
  style="display: block; margin: 0 auto; max-width: 500px">
  <img
  src="assets/images/comment.png"
  alt="Baby Care information cards" 
  title="Baby Care information cards"
  style="display: block; margin: 0 auto; max-width: 500px">

### About

* The about page contains a short description of the reason of this app.

<img
  src="assets/images/about.png"
  alt="Must haves information cards" 
  title="Must Haves information cards"
  style="display: block; margin: 0 auto; max-width: 350x">

### Register 

* If your new to the page you will see register and login in the navbar. 
* If your already logged-in you will see signout.

<img 
src="assets/images/sign_up.png" 
alt="Tips and Tricks information cards" 
title="Tips and Tricks information cards"
style="display: block; margin: 0 auto; max-width: 350px">

<img 
src="assets/images/sign_in.png" 
alt="Tips and Tricks information cards" 
title="Tips and Tricks information cards"
style="display: block; margin: 0 auto; max-width: 350px">

<img 
src="assets/images/sign_out.png" 
alt="Tips and Tricks information cards" 
title="Tips and Tricks information cards"
style="display: block; margin: 0 auto; max-width: 350px">

## Admin
With Djangos build in batteries included as they say in the walkthrough project I created an admin panel the same way as in the project. From here me as a admin can write, edit and delete posts and also approve, dismiss, edit and delete users comments.

## Features

* A lot of the styling is styled with help of Bootstrap classes. The best part in my opinion of why using bootstrap is that it styles elements in columns and therefore automatically looks good on any screensize.
* I've used cloudinary storage, allauth and summernote for this project to be possible. 
* Elephant SQL is used to help posting and fetching info back and forth of the database.
* If a blogg post would be missing a picture there is a backup photo of food to be shown to make the post always appear nice and concistent.

## Features Left to Implement

1. I would love the users to being able to interfear with the blog more than with likes and comments. Just like some options on the app only is viewable when logged in. I would like there to be one more window shown at times like this. A post window with a form for users to share their recipes with:
 * A title.
 * The measurements.
 * A description.
 * An uploaded photo.
Futher on I would like this just like with comments to end up in the admin panel awaiting approval for being posted.

2. I would also like the users to being able to edit there comments.

## Testing

1. My page appear good on desktop (1201px and up) and also on smaller screens (1200px and below). 

2. Page works good on chrome, firefox, iphone and android.

3. All links are tested in each try of diffrent browsers and all opens in a new window for good ux.

### Validator Testing

Url for new parent is tested in both [W3C-validator](https://validator.w3.org/) and [W3C-CSS-validaor](http://jigsaw.w3.org/css-validator/validator?lang=sv&profile=css3svg&uri=https%3A%2F%2Fohdamnitsnikki.github.io%2Fnew-parent%2F&usermedium=all&vextwarning=&warning=1)

### Deployment 

**_New Parent_** is deployed to GitHub pages, this was the steps:
* Through the GitHub repository go to settings
* Click on pages and use the branch menu to choose "main"
* Refresh the page and a link to the final project will be deployed

Live link here - [New Parent](https://ohdamnitsnikki.github.io/new-parent/)

* On the main site there is a fork button to create your own repository without affecting the orginal project or you could go into the project file and use the code button and clone the project directly.

## Credits

1. The template is taken from [Code Institute](https://github.com/Code-Institute-Org/gitpod-full-template)
2. For help during these projects I've used my mentor, the tutors and the I think therfore I blog walkthrough project.
3. The form for registration, sign in and sign out is completely built with djangos premade forms. Also the blog posts html code is from the walkthrough project. I've just added in some colours to make it fit my page since the content already looked so good. That also goes for the comment content and comment form. 
4. To get inspired about box-shadows and subsribe button I've used [W3School](https://www.w3schools.com/)
5. To understand how to style img in readme file I've used code from [SeanCDavid](https://www.seancdavis.com/posts/three-ways-to-add-image-to-github-readme/)

### Media

*  
* 
* 
