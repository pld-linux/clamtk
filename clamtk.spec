Summary:	Easy to use front-end for ClamAV
Summary(pl):	Prosty w u¿yciu interface dla ClamAV
Name:		clamtk
Version:	2.15
Release:	1
License:	Artistic
Group:		Applications
Source0:	http://dl.sourceforge.net/clamtk/%{name}-%{version}.tar.gz
# Source0-md5:	543f6914c3b7a37b758b05728bb0a0c0
URL:		http://clamtk.sourceforge.net/
Requires:	clamav >= 0.87
Requires:	clamav-database 
Requires:	clamav-libs 
Requires:	perl-Date-Calc
Requires:	perl-File-Find-Rule 
Requires:	perl-Gtk2 
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ClamTk is a frontend for ClamAV antivirus. It is meant to be
lightweight and easy to use.

%description -l pl
ClamTk jest ma³± i prost± w u¿yciu nak³adk± graficzn± na program
antyvirusowy ClamAV.

%prep
%setup -q
sed -i -e 's#Categories=Application;Utility;#Categories=GTK;Application;Utility;#' clamtk.desktop
echo 'Comment[pl]=Skaner antyvirusowy' >> clamtk.desktop
echo '# vi: encoding=utf-8' >> clamtk.desktop

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_mandir}/man1,%{_desktopdir},%{_datadir}/mime/packages}

cp clamtk $RPM_BUILD_ROOT%{_bindir}
install clamtk.xml $RPM_BUILD_ROOT%{_datadir}/mime/packages
install clamtk.1.gz $RPM_BUILD_ROOT%{_mandir}/man1
install clam.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install clamtk.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%doc CHANGES DISCLAIMER README clamtk.pl clamtk LICENSE
%{_desktopdir}/clamtk.desktop
%{_pixmapsdir}/clam.xpm
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/%{name}.1*
