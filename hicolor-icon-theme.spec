
Summary:	TODO
Summary(pl):	TODO
Name:		hicolor-icon-theme
Version:	0.3
Release:	1
License:	LGPL
Group:		Base
Source0:	http://freedesktop.org/Software/icon-theme/releases/%{name}-%{version}.tar.gz
# Source0-md5:	4257206ba86dc37e6b6cf57c9e2f927e
URL:		http://freedesktop.org/Software/icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TODO

%description -l pl
TODO

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_iconsdir}/hicolor
