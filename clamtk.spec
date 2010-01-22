Summary:	Easy to use front-end for ClamAV
Summary(pl.UTF-8):	Prosty w użyciu interfejs do ClamAVa
Name:		clamtk
Version:	4.23
Release:	1
License:	Artistic
Group:		Applications
Source0:	http://downloads.sourceforge.net/clamtk/%{name}-%{version}.tar.gz
# Source0-md5:	171da131291891218d75adc849c818af
URL:		http://clamtk.sourceforge.net/
BuildRequires:	perl-base
BuildRequires:	sed >= 4.0
Requires:	clamav >= 0.87
Requires:	clamav-database
Requires:	clamav-libs
Requires:	perl-Config-Tiny
Requires:	perl-Date-Calc
Requires:	perl-File-Find-Rule
Requires:	perl-Gtk2
Requires:	perl-Locale-gettext
Requires:	perl-Net-DNS
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
#mv po/cs{_CZ,}.mo
gzip -d clamtk.1.gz

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_mandir}/man1,%{_desktopdir},%{_datadir}/mime/packages,%{perl_vendorlib}/ClamTk}

install -p clamtk $RPM_BUILD_ROOT%{_bindir}
cp -a clamtk.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -a clamtk.png $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a clamtk.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -a lib/*.pm $RPM_BUILD_ROOT%{perl_vendorlib}/ClamTk

for n in po/*.mo; do
	l=$(basename $n .mo)
	install -Dp $n $RPM_BUILD_ROOT%{_datadir}/locale/$l/LC_MESSAGES/clamtk.mo
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
%{perl_vendorlib}/ClamTk
