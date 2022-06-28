Code Institute Portfolio 4 Submission (Full-Stack)

# The Gaming Blog
This website was made using ideas from the Assessment Guide that I was given, Project Example Idea 2 to example looked like this:

**Site owner's goal:**
-   The site owner would like to create a discussion community.
**Potential features to include:**
-   Posts can be up/downvoted
-   Comments can be left on a post **X**
-   Time/Date of posting
-   Topic groupings/categories

I incorporated the possible features that were discussed, such as like a post, publishing time/date, and categorizing each post. 

Overall, I made a gaming community website where they can debate all the hot subjects in the globe regarding the newest releases in games, consoles, hardware, you name it! I designed/styled this website using the famous bootstrap, which really helped me near the conclusion of my project because the whole Python/Django stuff had taken up a lot of my time; I still struggle with it today, I won't lie, but it was great being put on the spot.

My major goal was to develop a good responsiveness website that looked nice and worked well across all devices, and bootstrap was my hero once again.

## Page Responsiveness
![enter image description here](https://cdn.discordapp.com/attachments/919077234109739008/991112436113477692/QQ.jpg)

I tested the responsiveness across all layouts, including Android phones, tablets, and website displays. The majority of the styling is from Bootstrap since I appreciate how simple it is to make responsive websites with the code they offer. I also utilized Django's forms and stylized them again to my preference.

## Features
**The Gaming Blog** contains several features for users to enjoy as well as functions that users will never see.

 - **User verification:** - User verification prevents access to specific tasks. For example, if I am a user and want to create a blog, it will alert you on a different page that you cannot do so since you do not have an account. This also applies to modifying postings; you can only edit your post if you're signed into the proper account; if someone else is hooked into another account, they won't be able to access it, and if they have the link to that specific page, they won't be able to access it. 
- **Likes:** - I've added the option for any user to like any blog they click on; all of this is kept in the database. All the user has to do is log into their account and click the like button; this will accumulate based on the number of likes each blog receives.
- **Edit Profile:** - When a person creates an account, they will be able to change their profile. This contains the user's username, first and last name, email address, and the opportunity to reset their password if necessary.
- **Categories:** - There are currently three categories inside the gaming theme; when someone makes a blog under a given category, they can simply go to discover blogs and pick the genre they desire. All of these categories are organised, for example, all of the PlayStation blogs are on one page, and so on. This was done for ease of organisation and a pleasant overall user experience.
- **Delete Blog:** - I implemented the option for a user to remove a blog, and I validated that only they can delete their article.
- **Built-In-Django-Features:** - Django provides a wonderful built-in form for Signup/register forms, which makes it much easier to create forms that are appropriately constructed and checked.

Possible Features To Be Added

 - The ability to log in different ways.
 - Make the website look much nicer, at the moment it's very basic to my liking.

## Languages Used
### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://www.javascript.com/about)
-   [Python](https://www.python.org/)

## User Stories

## Deployment
Heroku deployment

