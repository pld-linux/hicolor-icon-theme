Summary:	Directory hierarchy for default icon theme
Summary(pl.UTF-8):	Struktura katalogów dla domyślnego motywu ikon
Name:		hicolor-icon-theme
Version:	0.12
Release:	2
License:	LGPL
Group:		Base
Source0:	http://icon-theme.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	55cafbcef8bcf7107f6d502149eb4d87
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

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# added in Revision 1.11
install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/stock/emoticons
install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/8x8/devices
install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/42x42/devices

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_iconsdir}/hicolor
