#$Id$
Summary: emacspeak -- The Complete Audio Desktop
Name: emacspeak
Version: 14.60025
Release: 1
Copyright: GPL
Group: Applications/Editors
Source: http://cs.cornell.edu/home/raman/emacspeak/emacspeak.tar.gz
URL: http://cs.cornell.edu/home/raman/emacspeak/emacspeak.html
Vendor: Emacspeak Inc 
Packager: T. V. Raman <raman@cs.cornell.edu>
%description 
Emacspeak is a speech interface that allows visually impaired users to
interact independently and efficiently with the computer. Available free of
cost on the Internet, Emacspeak has dramatically changed how the author and
hundreds of blind and visually impaired users around the world interact with
the personal computer and the Internet. A rich suite of task-oriented
speech-enabled tools provides efficient speech-enabled access to the evolving
semantic WWW. When combined with Linux running on low-cost PC hardware,
Emacspeak/Linux provides a reliable, stable speech-friendly solution that
opens up the Internet to visually impaired users around the world. With
support for the freely downloadable IBM ViaVoice Outloud speech synthesis
engine, Emacspeak now turns Linux into the first zero-cost Internet access
solution for blind and visually impaired users.

%prep
%setup

%build
make  config SRC=`pwd`
make

%install
make install

%post 
cd /usr/share/emacs/site-lisp/emacspeak
find . -type d -print |xargs chmod 755
echo "Emacspeak is now installed on your system.
Note that this has installed the sources for Emacspeak speech server for
ViaVoice Outloud  --a software speech synthesis engine.
However, you need to obtain and install the ViaVoice Outloud
RPMs and then compile the 
this speech server for ViaVoice Outloud.
1) Download and install the ViaVoice Outloud  RPMs from
http://www-4.ibm.com/software/speech/dev/index.html

2) cd to
/usr/share/emacs/site-lisp/emacspeak/servers/linux-outloud 
and type 

make

3) The Outloud speech server uses midi for producing auditory
icons.  You need to obtain and install package stdiosynth
from http://www.leb.net/pub/blinux/emacspeak/blinux/stdiom.tar.gz
"

%files 
 /usr/share/emacs/site-lisp/emacspeak/
%doc servers/linux-outloud/NOTES
%doc etc/NEWS
%doc etc/NEWS-14.0
%doc etc/NEWS-13.0
%doc etc/NEWS-12.0
%doc etc/NEWS-11.0
%doc etc/NEWS-10.0
%doc etc/NEWS-9.0
%doc etc/NEWS-8.0
%doc etc/FAQ
%doc etc/HELP
%doc etc/COPYRIGHT
%doc etc/tips.html
%doc etc/applications.html
%doc info/acknowledge.texi
%doc info/announce.texi
%doc info/audio-desktop.texi
%doc info/copyright.texi
%doc info/documents.texi
%doc info/emacspeak.texi
%doc info/eterm.texi
%doc info/install.texi
%doc info/introduction.texi
%doc info/online-help.texi
%doc info/packages.texi
%doc info/preamble.texi
%doc info/structure.texi
%doc info/tts.texi
%doc info/using.texi
%doc info/commands.texi
%doc user-guide/acknowledgments.html
%doc user-guide/before-you-begin.html
%doc user-guide/entertainment.html
%doc user-guide/index.html
%doc user-guide/introduction.html
%doc user-guide/productivity.html
%doc user-guide/system-administration.html
%doc user-guide/working-online.html
%doc user-guide/working-with-files.html
%doc user-guide/espk-article.sgml
/usr/bin/emacspeak
/usr/info/emacspeak.info
/usr/info/emacspeak.info-1
/usr/info/emacspeak.info-2
/usr/info/emacspeak.info-3
/usr/info/emacspeak.info-4
/usr/info/emacspeak.info-5
