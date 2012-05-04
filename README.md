customtags
==========

CustomTags is a single purpose web application.  It generates pages of labels based on the user input.

The barcodes on the generated labels are in EAN13 format, so everything should be able to read them.  The check
digit is automatically calculated.

To run:
* Clone, or download the source
* run `pip install -r requirements.txt` from the customTags directory, this
will install the required packages.  The reportlab library seems to have
problems with venv on windows.  So if you're using windows, download the
reportlab binaries from their site.