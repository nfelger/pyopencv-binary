This contains the binary extension from the OpenCV project as installed by
Ubuntu's python-opencv package.

OpenCV is hard to install inside an isolated virtualenv (i.e. one without the
`--system-site-packages` flag). A common recommendation is to install the
system package with apt-get and to subsequently copy the exension into the
virtualenv directory manually.

This package allows us to install those files with pip instead. This package is
very platform-specific and unlikely to work with other versions of Ubuntu than
14.04.
