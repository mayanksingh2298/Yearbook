# Yearbook

This webapp is used to generate the yearbook every year for the final year students. 



### Database struncture
* Student:
  * id
  * one-one link with django inbuilt user(for auth purposes)
  * name
  * department
  * DP (display picture)
  * genPic1 (first out of the 2 pictures the user would like to contribute to the yearbook)
  * genPic2 (second out of the 2 pictures the user would like to contribute to the yearbook)
  * phone
  * email
  * oneliner (something that describes them)
  * AnswersAboutMyself (json of some answers they write about themselves)
  ```
  {
   "id of question":"answer"
  }
  example
  {
   "1":".",
   "3":"sample answer",
   "2":"another sample answer"
  }
  ```
  * VotesIHaveGiven (json of votes that this user has given)
  ```
  {
   "id of poll":"entry number of a user"
  }
  example
  {
    "283":"2014ee10444",
    "202":"2014ee10655",
    "265":"2014ee30544",
    "157":"2014ee30152",
    "211":"2014ee30531",
    "301":"2014ee10871",
    "310":"2014ee30527"
  }
  ```
  * CommentsIWrite (array of json of comments that this user has given)
  ```
  [
   {
    "comment":string of comment,
    "forWhom": "entry number of user"
   },...
  ]
  example
  [
   {
     "comment":"hello how are you.",
     "forWhom":"2014ch70049"
   },
   {
     "comment":"all the best for your future!",
     "forWhom":"2014ee30766"
   },
  ]
  ```
  * CommentsIGet (array of json of comments that this user gets)
  ```
  [
   {
    "comment":string of comment,
    "fromWhom": "entry number of user",
    "displayInPdf":"True or False"(based on whether the user wants this displayed in the pdf)
   },...
  ]
  example
  [
   {
     "comment":"I got this comment",
     "fromWhom":"2014ee30539",
     "displayInPdf":"True"
   },
   {
     "comment":"I got another comment ",
     "fromWhom":"2014ee10134",
     "displayInPdf":"True"
   },
   {
     "comment":"Ye lo ek aur",
     "fromWhom":"2014ee10496",
     "displayInPdf":"True"
   },
  ]
  ```
* GenQuestion (this consists of some general questions that admins have to publish before the portal is set up):
  * id
  * question 
* Poll (this consists of some poll questions)
  * id
  * poll (the poll title)
  * department
  * votes (json field which stores data about the votes given)
  ```
  {
   "entry number of some user":votes he/she gets,
   ...
  }
  example
  {
  "2014bb10048":4,
  "2014bb10021":3,
  "2014bb10028":6
  }
  ```

### How is this supposed to work?
### Prior work to be done by admins
1. @Atishya add here, how can we get started with the yearbook.
2. @Atishya Do mention about the changes to do for each year, and remember the Config files are not present on the github, so add information about that too.
3. @Atishya, add about the scripts using which we create accounts for people
4. @Atishya, add details about setting up genQuestions
5. @Atishya, add details about setting up the polls
6. Comment this line in urls.py: url(r'^yearbook/$', views.yearbook, name='yearbook'),


### How does the general public use this?
1. On opening the website, you would be greeted with the welcome page, where you'd have to sign in with your Kerberos ID
2. The first thing which someone would want to do is to edit their profile page - add details about themselves.
3. Next, they would want to answer questions about themselves.
4. They can write comments about their friends(inter-department commenting is allowed)
5. They can vote in polls(If a poll is department specific, only students from that departments can vote for students in their department. If a poll has department - 'all', anyone one can vote for anyone)
6. If they don't want a comment written by someone for them, to be displayed in the yearbook, they can set displayInPdf for that comment to be False.

### Post work to be done by admins
1. Uncomment this line in urls.py: url(r'^yearbook/$', views.yearbook, name='yearbook'),
2. Now if a user browses to .../yearbook, they can see the yearbook of their department.
3. If the admin is logged in via the .../admin site, they can browse to .../yearbook?department=<dept_code>, to open the yearbook of any department.
```
dept_code - department name

chemical - chemical
civil - civil
cse - computer science
ee - electrical
maths - mathematics
mech - mechanical
physics - engineering physics
textile - textile engineering
dbeb - biotechnology
```
4. At this point of time, there are no pictures in yearbooks.
5. Admin must download all the yearbooks, by hitting Ctrl + P once they have opened the yearbooks. Use the following settings to download the yearbooks in a chrome browser:
 * Set the zoom to 125% (yeah, that changes the print of the yearbook)
 * Enable background graphics
 * Set margins to none, if that doesn't look good, let it be default
6. Now we need to optimize the size of the yearbooks using ps2pdf command. To do that run this for each book:
  * ps2pdf <file_input> <file_output>

  Alternatively,
  * Create a new folder and put all the downloaded yearbooks inside it. 
  * Create a new folder inside this folder with the name "optimized".
  * Create a new file with the name "optimize.sh" and copy-paste the following inside it,
    ```
    for VAR in $(ls)
    do
            echo $VAR
            ps2pdf $VAR optimized/$VAR
    done
    ```
  * Run this script
7. @Udit/@Aman, add about the collage stuff

## Authors

* [**Mayank Singh Chauhan**](https://github.com/mayanksingh2298)
* [**Atishya Jain**](https://github.com/atishya-jain)


Also see the list of Devclub's [members](https://github.com/orgs/devclub-iitd/people).

## Acknowledgments

* [**Aman Aggarwal**](https://github.com/aman71197) for your guidance
* [**Udit Jain**](https://github.com/udit01) for helping with the collage

