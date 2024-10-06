Summary:	Directory hierarchy for default icon theme
Summary(pl.UTF-8):	Struktura katalogów dla domyślnego motywu ikon
Name:		hicolor-icon-theme
Version:	0.18
Release:	1
License:	GPL v2+
Group:		Base
Source0:	https://icon-theme.freedesktop.org/releases/%{name}-%{version}.tar.xz
# Source0-md5:	ef14f3af03bcde9ed134aad626bdbaad
Patch0:		%{name}-more-dirs.patch
URL:		https://freedesktop.org/wiki/Software/icon-theme/
BuildRequires:	meson >= 0.60
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
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
# additional sizes:
# 8x8/apps  genius grass postgis-gui spatialite_gui
# 8x8/emblems  ka5-kmail
# 20x20/apps  VirtualBox-gui kmymoney parcellite
# 20x20/mimetypes  VirtualBox-gui djvulibre
# 40x40/apps  parcellite
# 42x42/apps  grass postgis-gui spatialite_gui
# 80x80/apps  grass spatialite_gui ka5-kanagram-data
# 160x160/apps  wcm wf-shell
# 1024x1024/apps  kmymoney scribus ka5-kdevelop-data ka5-krita-data gingerblue gnome-internet-radio-locator gtk-internet-radio-locator octave-gui supertuxkart vcmi
# 1024x1024/mimetypes  kmymoney ka5-krita-data
%patch0 -p1

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

mkdir -p $RPM_BUILD_ROOT%{_iconsdir}/hicolor/symbolic/actions

# gtk+2 cache
touch $RPM_BUILD_ROOT%{_iconsdir}/hicolor/icon-theme.cache

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.md
%dir %{_iconsdir}/hicolor
%{_iconsdir}/hicolor/*x*
%{_iconsdir}/hicolor/scalable
%{_iconsdir}/hicolor/symbolic
%ghost %{_iconsdir}/hicolor/icon-theme.cache
%{_npkgconfigdir}/default-icon-theme.pc
