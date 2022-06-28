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


-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://www.javascript.com/about)
-   [Python](https://www.python.org/)

## User Stories
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 50%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: center;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>

<table>
  <tr>
    <th>DONE</th>
    <th>STORY ID</th>
    <th>As A/An</th>
    <th>I Want To Be Able To</th>
    <th>Screenshot</th>
    <th></th>
  </tr>
  <tr>
    <td>✔</td>
    <td>1</td>
    <td>Site-User</td>
    <td>Create a blog</td>
    <td><a href = "https://cdn.discordapp.com/attachments/919077234109739008/991393203339145316/create.png"> Screenshot </a></td>
  </tr>
  <tr>
    <td>✔</td>
    <td>2</td>
    <td>Site-User</td>
    <td>Sign up page</td>
    <td><a href = "https://cdn.discordapp.com/attachments/919077234109739008/991398752365576222/signup.png"> Screenshot </a></td>
  </tr>
  <tr>
    <td>✔</td>
    <td>3</td>
    <td>Site-User</td>
    <td>Login page</td>
    <td><a href = "https://cdn.discordapp.com/attachments/919077234109739008/991399336938311881/login.png"> Screenshot </a></td>
  </tr>
  <tr>
    <td>✔</td>
    <td>4</td>
    <td>Site-User</td>
    <td>Category</td>
    <td><a href = "https://cdn.discordapp.com/attachments/919077234109739008/991406757354147911/category.png"> Screenshot </a></td>
  </tr>
  <tr>
    <td>✔</td>
    <td>5</td>
    <td>Site-User</td>
    <td>Edit post</td>
    <td><a href = "https://cdn.discordapp.com/attachments/919077234109739008/991407909110030436/edit.png"> Screenshot </a></td>
  </tr>
  <tr>
    <td>✔</td>
    <td>6</td>
    <td>Site-User</td>
    <td>Delete post</td>
    <td><a href = "https://cdn.discordapp.com/attachments/919077234109739008/991408486426615899/333.png"> Screenshot </a></td>
  </tr>
   <tr>
    <td>✔</td>
    <td>7</td>
    <td>Site-User</td>
    <td>Edit profile</td>
    <td><a href = "https://cdn.discordapp.com/attachments/919077234109739008/991409195104616508/edit_profile.png"> Screenshot </a></td>
  </tr>
  <tr>
    <td>✔</td>
    <td>8</td>
    <td>Site-User</td>
    <td>Like post</td>
    <td><a href = "https://cdn.discordapp.com/attachments/919077234109739008/991409964625166446/like.png"> Screenshot </a></td>
  </tr>
</table>

## 

<table>
  <tr>
    <th>DONE</th>
    <th>STORY ID</th>
    <th>As A/An</th>
    <th>I Want To Be Able To</th>
    <th></th>
  </tr>
  <tr>
    <td>✔</td>
    <td>9</td>
    <td>Admin-User</td>
    <td>Create/Delete Category</td>
  </tr>
  <tr>
    <td>✔</td>
    <td>10</td>
    <td>Admin-User</td>
    <td>Create/Delete Blogs</td>
  </tr>
  <tr>
    <td>✔</td>
    <td>11</td>
    <td>Admin-User</td>
    <td>Delete/Add Users</td>
  </tr>
  <tr>
    <td>✔</td>
    <td>12</td>
    <td>Admin-User</td>
    <td>Edit All Profiles</td>
  </tr>
  
</table>

## Deployment
I first installed the **Heroku CLI** and then signed into Heroku through the CLI. When everything was set up, I transferred all of the code to the CLI and executed the migrations.

During this procedure, I had to adjust the method I deployed my project since, at the last minute, I realised my code didn't want to execute at all, which stressed me out. I inquired about Slack for alternatives to the code path that coding institute provided you. Everything was run using the CLI.

## Validation
I tested all of the validations and they all passed; before to deployment, I saw about 19 problems in the HTML but resolved them within a hour or so.

## Testing
This has to be the most difficult project I've worked on since I've counted and rectified so many problems. Let's just say Django isn't one of my strong suits, but I have a functioning page that functions to say the least.

My greatest challenge was the actual deployment process since everything just chose to break at the time, so I was searching all over the web for answers until Anim, a student from Slack, jumped in and was my savior; I couldn't have done it without him!

My primary difficulty was that I moved everything in the wrong sequence, which didn't go well, but I now know that practice makes perfect for the next time!

## Credits

Huge thanks to bootstrap, who has been my hero throughout this trip because Python and Django aren't my strong suits and took up most of my time, therefore bootstrap has saved me a lot of time.

**Acknowledgements** 
All of the Slack aid with suggestions and help, especially for anim working through the issue with the categories difficulty I had, as well as the entire deployment process, which was already a hassle.

Once again, many thanks to the Code Institute for all of the films they give; huge ups to them!

And of course my family for supporting me through this whole course <3
