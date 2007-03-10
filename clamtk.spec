Summary:	Easy to use front-end for ClamAV
Summary(pl.UTF-8):	Prosty w użyciu interfejs do ClamAVa
Name:		clamtk
Version:	2.30
Release:	1
License:	Artistic
Group:		Applications
Source0:	http://dl.sourceforge.net/clamtk/%{name}-%{version}.tar.gz
# Source0-md5:	8d0bad3800547477ede2e7d5bd3297e3
URL:		http://clamtk.sourceforge.net/
BuildRequires:	sed >= 4.0
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

%description -l pl.UTF-8
ClamTk jest małą i prostą w użyciu nakładką graficzną na program
antyvirusowy ClamAV.

%prep
%setup -q
sed -i -e 's#Categories=Application;Utility;#Categories=GTK;Utility;#' clamtk.desktop
echo '# vi: encoding=utf-8' >> clamtk.desktop

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_mandir}/man1,%{_desktopdir},%{_datadir}/mime/packages}
install -d $RPM_BUILD_ROOT%{_datadir}/locale/{da,de,fr,it,pt_BR,ru,zh_CN}/LC_MESSAGES

install clamtk $RPM_BUILD_ROOT%{_bindir}
gzip -dc clamtk.1.gz >$RPM_BUILD_ROOT%{_mandir}/man1/clamtk.1
install clamtk.png $RPM_BUILD_ROOT%{_pixmapsdir}
install clamtk.desktop $RPM_BUILD_ROOT%{_desktopdir}

for n in po/*.mo ; do
    install -D $n $RPM_BUILD_ROOT%{_datadir}/locale/`basename $n .mo`/LC_MESSAGES/clamtk.mo
done
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGES DISCLAIMER README clamtk LICENSE
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/clamtk.desktop
%{_pixmapsdir}/clamtk.png
%{_mandir}/man1/%{name}.1*
