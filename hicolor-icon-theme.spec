Summary:	Directory hierarchy for default icon theme
Summary(pl):	Struktura katalogów dla domy¶lnego motywu ikon
Name:		hicolor-icon-theme
Version:	0.9
Release:	1
License:	LGPL
Group:		Base
Source0:	http://icon-theme.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	1d0821cb80d394eac30bd8cec5b0b60c
URL:		http://icon-theme.freedesktop.org/wiki/HicolorTheme
# Conflicts:	gnome-icon-theme < 1.0.9
Conflicts:	kdelibs < 9:3.2.0-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Directory hierarchy for default icon theme.

%description -l pl
Struktura katalogów dla domy¶lnego motywu ikon.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# added in Revision 1.11
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/stock/emoticons

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_iconsdir}/hicolor
