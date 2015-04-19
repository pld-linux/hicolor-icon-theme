Summary:	Directory hierarchy for default icon theme
Summary(pl.UTF-8):	Struktura katalogów dla domyślnego motywu ikon
Name:		hicolor-icon-theme
Version:	0.15
Release:	1
License:	GPL v2
Group:		Base
Source0:	http://icon-theme.freedesktop.org/releases/%{name}-%{version}.tar.xz
# Source0-md5:	6aa2b3993a883d85017c7cc0cfc0fb73
Patch0:		%{name}-more-dirs.patch
URL:		http://icon-theme.freedesktop.org/wiki/HicolorTheme
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# gtk+2 cache
touch $RPM_BUILD_ROOT%{_iconsdir}/hicolor/icon-theme.cache

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{_iconsdir}/hicolor
%{_iconsdir}/hicolor/*x*
%{_iconsdir}/hicolor/scalable
%{_iconsdir}/hicolor/symbolic
%ghost %{_iconsdir}/hicolor/icon-theme.cache
