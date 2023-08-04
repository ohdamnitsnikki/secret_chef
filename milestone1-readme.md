# Secret Chef

The Secret Chef is a blog for people to gather around and share their best recipes, but also to experience new flavors as they go along. Anyone can visit the site and get inspired by the blog post pictures of homemade dinners. If you then choose to be a part of the Secret Chef community, you can also share your own tips. And just in case you change your mind about a recipe or if you have improved it, you are also able to edit or delete your own blog posts.

To keep the imaginary flavors on the page, all photos from the blog posts render in a slideshow on the front page.

![Seret Chef home page](media/facebookpage.png)

[View Secret Chef on Heroku Pages](https://git.heroku.com/secret-chef1337.git)

---

## CONTENTS

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [General Features on Each Page](#general-features-on-each-page)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

### Initial Discussion

The proprietor of the esteemed Secret Chef blog aspired to forge a community that celebrates the oft-overlooked realm of culinary artistry, where extraordinary flavors intertwine and caress the senses, transcending mere gustatory delight. In a world where culinary excellence remains underappreciated, this sacred platform beckons gifted Secret Chefs to unite and showcase their cherished recipes, while also embarking on a journey of inspiration and discovery, honing their craft with novel and divine gastronomic delights.

#### Key information for the site

* Anyone can join.
* Anyone is welcome to take part in the lovely recipes.
* Users can write blog posts.
* The admin decides what is getting published to keep track of relevant data.

### User Stories

#### User Goals

* To have a responsive blog that works well on various device sizes.
* To easily create an account and create, read, edit, and delete blog posts.
* To have the option to save account information for convenience during future visits.
* To view pictures of the recipes.
* To register, log in, and log out with ease.
* To view all posts.

#### Admin Goals

* To easily manage and modify posts by editing, adding, or deleting them.
* To view users' recipes and decide whether to publish them or not.
* To easily create their own blog posts.

## Design

For the color palette, I used [Coolors](https://coolors.co/palette/0081a7-00afb9-fdfcdc-fed9b7-f07167).
Instead of trying to match up the colors, I went through the site and found this palette amusing.

### Imagery

I plan to use vibrant and enticing food imagery throughout the site. This will include high-quality pictures of the recipes shared by users, showcasing the mouthwatering dishes and their appetizing presentation. Additionally, I aim to incorporate visually appealing graphics and illustrations that complement the overall theme of the blog and enhance the reader's culinary experience.

## Features

* Much of the styling on the site is achieved with the aid of Bootstrap classes. One of the most appealing aspects, in my opinion, of using Bootstrap is its ability to format elements into responsive columns, making the design look fantastic on any screen size.

* This project relies on Cloudinary storage, allauth, and Summernote to make it possible.

* Elephant SQL plays a crucial role in facilitating the seamless exchange of data between the application and the database.

* In case a blog post lacks a picture, there is a backup image of food that will be displayed, ensuring that the post maintains a consistent and attractive appearance.

* Leveraging Django forms, I also incorporated user-friendly messages that appear after registration, login, and logout events. Additionally, these messages are programmed to disappear automatically after a short duration using JavaScript, providing a smoother user experience.

### General features on each page

#### Navigation Bar
* The navigation bar includes responsive links to the home, blog posts, about, login/register/logout and write a posts page.
<img
  src="assets/images/navigation-bar.png"
  alt="The Navbar" 
  title="The Navbar"
  style="display: block; margin: 0 auto; max-width: 500px">
  
#### Header- Seret Chef!
* The header containes the applications name 
<img
  src="assets/images/header.png"
  alt="The Header" 
  title="The Header"
  style="display: block; margin: 0 auto; max-width: 300px">


#### Footer
* The Footer has navigation links that opens in a new window when used. One to our Facebook page, one for Instagram and one to our youtube chanel. 
<img
  src="assets/images/footer.png"
  alt="The Footer" 
  title="The Footer"
  style="display: block; margin: 0 auto; max-width: 500px">

**These elements are constant on each page for easy navigation.**

### Future Implementations

* For the future I would like to update the blog post form to make it render the post diffrently. I would like the content area to render into two part. One where each ingredience with the measurments renders into dots. Then I would like the step by step to appear the same way. Instead of just being one longer text.
* I would also implement a like function that makes blog post appear higher on the site.
* Users should also be able to comment and keep a conversation on each post.

### Accessibility

Be an amazing developer and get used to thinking about accessibility in all of your projects!

This is the place to make a note of anything you have done with accessibility in mind. Some examples include:

Have you used icons and added aria-labels to enable screen readers to understand these?
Have you ensured your site meets the minimum contrast requirements?
Have you chosen fonts that are dyslexia/accessible friendly?

Code Institute have an amazing channel for all things accessibility (a11y-accessibility) I would highly recommend joining this channel as it contains a wealth of information about accessibility and what we can do as developers to be more inclusive.

## Technologies Used

👩🏻‍💻 View an example of a completed Technologies Used section [here](https://github.com/kera-cudmore/Bully-Book-Club#Technologies-Used)

### Languages Used

Make a note here of all the languages used in creating your project. For the first project this will most likely just be HTML & CSS.

### Frameworks, Libraries & Programs Used

Add any frameworks, libraries or programs used while creating your project.

Make sure to include things like git, GitHub, the program used to make your wireframes, any programs used to compress your images, did you use a CSS framework like Bootstrap? If so add it here (add the version used).

A great tip for this section is to include them as you use them, that way you won't forget what you ended up using when you get to the end of your project.

## Deployment & Local Development

👩🏻‍💻 View an example of a completed Deployment & Local Development section [here](https://github.com/kera-cudmore/TheQuizArms#Deployment)

### Deployment

Include instructions here on how to deploy your project. For your first project you will most likely be using GitHub Pages.

### Local Development

The local development section gives instructions on how someone else could make a copy of your project to play with on their local machine. This section will get more complex in the later projects, and can be a great reference to yourself if you forget how to do this.

#### How to Fork

Place instructions on how to fork your project here.

#### How to Clone

Place instructions on how to clone your project here.

## Testing

Start as you mean to go on - and get used to writing a TESTING.md file from the very first project!

Testing requirements aren't massive for your first project, however if you start using a TESTING.md file from your first project you will thank yourself later when completing your later projects, which will contain much more information.
  
Use this part of the README to link to your TESTING.md file - you can view the example TESTING.md file [here](milestone1-testing.md)

## Credits

👩🏻‍💻 View an example of a completed Credits section [here](https://github.com/kera-cudmore/BookWorm#Credits)

The Credits section is where you can credit all the people and sources you used throughout your project.

### Code Used

If you have used some code in your project that you didn't write, this is the place to make note of it. Credit the author of the code and if possible a link to where you found the code. You could also add in a brief description of what the code does, or what you are using it for here.

### Content

Who wrote the content for the website? Was it yourself - or have you made the site for someone and they specified what the site was to say? This is the best place to put this information.

###  Media

If you have used any media on your site (images, audio, video etc) you can credit them here. I like to link back to the source where I found the media, and include where on the site the image is used.
  
###  Acknowledgments

If someone helped you out during your project, you can acknowledge them here! For example someone may have taken the time to help you on slack with a problem. Pop a little thank you here with a note of what they helped you with (I like to try and link back to their GitHub or Linked In account too). This is also a great place to thank your mentor and tutor support if you used them.
