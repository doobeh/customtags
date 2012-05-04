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
on port 5000 and listens on 0.0.0.0 (so unless you're running a firewall, it
will be accessible from remote computers).

Improvements/Todo
-----------------
* Label configuration should read from a configuration file, currently it's
hard-coded.

* Form validation, at present the upc gets cropped to 12 digits, even if the
user enters more, and the description has no length checks.  This can cause
at best formatting errors, at worst a failure to generate any tags.