# Wikipedia
It's a wikipedia like web-based app.

<br>
<a href="https://youtu.be/lqzdZqQcnf8">See it in action</a>.

## Installation
- You need to have **Django** installed on your local machine.
- Download this zip code.
- Go into this project's directory and run `python(or python3) manage.py runserver`.
- You'll be able to run the application.
- To install django on your machine, [click here](https://docs.djangoproject.com/en/3.2/topics/install/).
- All the database files will be stored on your machine.

## Usage
- Upon running the application, you'll be presented with an index page that lists all the topics stored in the **entries** folder.
- You have the option of creating a new page, editing the existing page and choosing a random page from all the entries.
- To create a new page, click on **Create New Page** wherein you can type title and content for your page.
- To edit a page, select any entry from the **Home** page and click on **Edit** button to edit the page.
- You can search your page in the **Search Encyclopedia** by typing in the entrie's name. You'll be presented with the list of all entries whose substring matches the searched entry.
- Clicking on **Random Page** will take you to a random page from the existing pages.
- Everything you write in pages will be written in **markdown**. 
- To see basic formatting and syntax of markdown, [click here](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

## Structure/Design of program
This is a wiki project that has a app called encyclopedia. It is mainly written in Django. HTML and CSS are used for layout and styling.
<br>
Main files:
<br>
* *manage.py* - It contains all the required files to run your webapp.
* *encyclopeida/static* - It include the required styling css page to help user to have a good experience of the webapp.
* *encyclopedia/templates* - These include all the html pages of the webapp from a basic layout file to each and every html page of the webapp.
* *auctions/views.py* - It contains all the logic behind rendering the required pages upon request and acting as a mediator between databse and user.
* *auctions/urls.py* - It has all the urls that a user can request to visit the pages of the webapp.

There are other supporting files as well.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
