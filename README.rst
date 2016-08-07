===================
google-drive-public
===================

Download without login from public Google Drive folders in Pure Python (works on Windows/Linux/Mac)


Install
=======
::

    python setup.py develop

Usage
=====
Copy the URL of the publicly-shared Google Drive folder from which you want to download files::

    python public.py <paste folder URL>

-o   output directory
-c   clobber (overwrite already downloaded files)
-v   verbose


=============    ===========================
file             description
=============    ===========================
public.py        Download publicly-shared Google Drive files without login
pydrv.py         use PyDrive (use public.py instead)
=============    ===========================


Reference
=========
Normal users don't care about these notes below.

PyDrive notes
-------------
Even though the files may be shared publicly, with PyDrive you still need an API key ``client_secrets.json``
This may be acquired via `Google API console <https://console.developers.google.com/apis/library>`_
API Manager > Credentials > Create Project (if not already created) -- any name is fine >
Create Credentials > OAuth client ID > Web Application (any name is fine)
Then in the Credentials list, at the far right of the key row, there is a download icon. Save it into your code directory as client_secrets.json
Note, this gives the Python application a view into your entire Google Drive, so perhaps for best security create a throwaway account used just for this.

Currently, the code underlying PyDrive (google-api-python-client) has a memory leak,
so the code automatically stops after it's used too much RAM. Keep an eye on it so your computer doesn't crash.

ChromeDriver
------------
Used by Selenium to invoke a Chrome browser.

Linux::

 sudo apt-get install chromium-chromedriver

Windows: http://chromedriver.storage.googleapis.com/index.html
