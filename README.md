## Flask-with-Datatables (Server-Side Rendering)

With the goal of Datatables library (https://datatables.net/) being to enhance HTML tables, providing built-in features supporting pagination, searching, multi-column ordering, easily theme-able etc, it
provides support for two modes of processing data.

1. Client-Side processing - the full data set is loaded up-front and data processing is done in the browser.
2. Server-Side processing - an Ajax request is made for every table redraw, with only the data required for each display returned. The data processing is performed on the server.

Both has its advantages and disadvantages, however in dealing with very large records, forexample, 100,000 rows of records, it is advisable to use server-side processing, so the server does the heavy lifting 
of serving data as it is requested from the frontend, as the browser cannot support large records or quantity of data at once because it has a limited amount of memory in loading records to the Browser Window.

## Server-side Rendering with Flask and SQL-Alchemy
Flask as a lightweight WSGI web application, provides the minimal tools such as WSGI toolkit, CLICK CLI toolkit and Jinja template, for writing our backend applications as well as being able to render HTML with
its in-built Jinja template.

**Flask-SQLAlchemy** as an **ORM** provides and abstract interface to interact  with several **database engines**, and in this example, **SQLITE** is used, but can be replaced by other database engines in the .**env file settings**.

In performing Server-Side Rendering, Datatables makes **ajax requests** to request table data from the server in the background without the browser re-loading and updates the table records with the newly fetched data. This
makes it ideal for processing and displaying large quantities in the frontend of our application.

## Process-Flow
1. **render_template** from the  Flask class,  renders an html template, thus when the application starts,  the **homepage endpoint** renders our **index.html** file
2. Custom ajax datatables javascript file found in **static/js folder**, upon **index.html being rendered** makes a **POST-request** to the appropriate endpoint **(user_records endpoint)** found in **blueprint_routes folder**
3. If **user records are available in our database**, the **ORM queries** are executed which fetches and returns the relevant data as **JSON payload** to the frontend, else if no records are
   available, default **JSON Payload** is also returned as well. 
5. With the available data, datatables renders the records in its table
6. Pagination buttons automatically provided with datatables, can be interacted with, depending on how the data is paginated, and on each paginated button click, datatables makes  post request to retrieve new data from the
   backend-server and redraws the records in the datatables
7. Users can also search for new records, by typing in their query in the search bar of datatables, which in turn sends the request to the backend, processes the search query and returns the relevant result.

[NOTE]
The database is already pre-populated with (5000 records)  in the **app.py** file with dummy data found in **dummy_data.py**

After cloning the application, create an (.env) file in the root of the application containg the following fields to properly setup your application
     
     FLASK_DEBUG=true
     SECRET_KEY=<generated your secret key here>
     SQLALCHEMY_DATABASE_URI=sqlite:///userinfoDB.db
     SQLALCHEMY_TRACK_MODIFICATIONS=False
     

     Generating secret: https://docs.python.org/3/library/secrets.html#module-secrets
     TLDR: python >>> import secrets
                  >>> print(secrets.token_urlsafe())
     Copy generated secret to SECRET_KEY field

Libraries Used:
1.   pip install Flask
     https://flask.palletsprojects.com/en/stable/installation/
     
2.   pip install environs
     URL: https://github.com/sloria/environs
     
3.   pip install -U Flask-SQLAlchemy
     URL: https://flask-sqlalchemy.readthedocs.io/en/stable/quickstart/#installation

## Sample Screenshot of Running application
Retrieve paginated records
![datatables-rendering example](https://github.com/user-attachments/assets/949dc1e9-dafa-49fc-8705-a61c86fe0d6d)

Retrieve paginated records
![datatables-rendering-2](https://github.com/user-attachments/assets/3dd51c80-6153-46e3-b126-17337472de91)

Performing Search
![datatables-search](https://github.com/user-attachments/assets/4196845f-61f9-4652-b5d0-c0328fad1751)

