Summary:	Directory hierarchy for default icon theme
Summary(pl):	Struktura katalogów dla domy¶lnego motywu ikon
Name:		hicolor-icon-theme
Version:	0.5
Release:	2
License:	LGPL
Group:		Base
Source0:	http://freedesktop.org/Software/icon-theme/releases/%{name}-%{version}.tar.gz
# Source0-md5:	947c7f6eb68fd95c7b86e87f853ceaa0
URL:		http://freedesktop.org/Software/icon-theme
# Conflicts:	gnome-icon-theme < 1.0.9
Conflicts:	kdelibs < 9:3.2.0-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Directory hierarchy for default icon theme.

%description -l pl
Struktura katalogów dla domy¶lnego motywu ikon.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

# make install is outdated, make all by hand
#%{__make} install \
#	DESTDIR=$RPM_BUILD_ROOT \
#	PREFIX=%{_prefix}

install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/24x24/apps
install index.theme $RPM_BUILD_ROOT%{_iconsdir}/hicolor
for dir in `grep Directories= index.theme|sed -e 's/Directories=//;s/,/ /g'` ; do
	install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/$dir
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_iconsdir}/hicolor
