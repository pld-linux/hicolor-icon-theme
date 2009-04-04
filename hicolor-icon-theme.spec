Summary:	Directory hierarchy for default icon theme
Summary(pl.UTF-8):	Struktura katalogów dla domyślnego motywu ikon
Name:		hicolor-icon-theme
Version:	0.10
Release:	3
License:	LGPL
Group:		Base
Source0:	http://icon-theme.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	3534f7b8e59785c7d5bfa923e85510a7
Patch0:		%{name}-256-size.patch
URL:		http://icon-theme.freedesktop.org/wiki/HicolorTheme
# Conflicts:	gnome-icon-theme < 1.0.9
Conflicts:	kdelibs < 9:3.2.0-4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Directory hierarchy for default icon theme.

%description -l pl.UTF-8
Struktura katalogów dla domyślnego motywu ikon.

%prep
%setup -q
%patch0 -p1

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
