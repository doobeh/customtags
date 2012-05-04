customtags
==========

CustomTags is a single purpose web application.  It generates pages
of labels based on the user input of description and upc.

The barcodes on the generated labels are in EAN13 format, so everything
worth it's salt should be able to read them.  The check digit is
automatically calculated.

The UI uses Bootstrap Twitter, and the backend uses Flask and Reportlab
for the heavy lifting.

To run:
-------
* Clone, or download the source
* Create a python virtualenv and activate it.
* run `pip install -r requirements.txt` from the customTags directory, this
will install the required packages to your virtual environment.  The
reportlab library seems to have problems with virtualenv on windows.
So if you're using windows, download the reportlab binaries from their site.
* Then simply run `python runserver.py`.  The webserver will by default run
on port 5000 and listens on 127.0.0.1