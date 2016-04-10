Summary:	Character Map application for GNOME
Summary(pl.UTF-8):	Mapa znaków dla GNOME
Name:		gnome-characters
Version:	3.20.1
Release:	1
License:	GPL v2+ with BSD parts
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-characters/3.20/%{name}-%{version}.tar.xz
# Source0-md5:	5e1ce3cd54bede98aa0ee9cb9dd7934c
URL:		https://wiki.gnome.org/Design/Apps/CharacterMap
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.12
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gettext-tools
BuildRequires:	gjs-devel >= 1.43.3
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gobject-introspection-devel >= 1.36.0
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	intltool >= 0.50.1
BuildRequires:	libtool >= 2:2
BuildRequires:	libunistring-devel >= 0.9.6
BuildRequires:	pango-devel
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	gjs >= 1.43.3
Requires:	glib2 >= 1:2.26.0
Requires:	gnome-icon-theme-symbolic
Requires:	hicolor-icon-theme
Requires:	libunistring >= 0.9.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Characters is a simple utility application to find and insert
unusual characters.

%description -l pl.UTF-8
GNOME Characters to prosta aplikacja narzędziowa pozwalająca znajdować
i wstawiać rzadko używane znaki.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4 -I glm4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/org.gnome.Characters/*.la

%find_lang org.gnome.Characters
%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache gnome
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache gnome
%update_icon_cache hicolor

%files -f org.gnome.Characters.lang
%defattr(644,root,root,755)
%doc COPYING NEWS README
%attr(755,root,root) %{_bindir}/gnome-characters
%dir %{_libdir}/org.gnome.Characters
%attr(755,root,root) %{_libdir}/org.gnome.Characters/libgc.so
%dir %{_libdir}/org.gnome.Characters/girepository-1.0
%{_libdir}/org.gnome.Characters/girepository-1.0/Gc-1.0.typelib
%{_datadir}/appdata/org.gnome.Characters.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Characters.service
%{_datadir}/dbus-1/services/org.gnome.Characters.BackgroundService.service
%{_datadir}/glib-2.0/schemas/org.gnome.Characters.gschema.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Characters.search-provider.ini
%dir %{_datadir}/org.gnome.Characters
%attr(755,root,root) %{_datadir}/org.gnome.Characters/org.gnome.Characters
%attr(755,root,root) %{_datadir}/org.gnome.Characters/org.gnome.Characters.BackgroundService
%{_datadir}/org.gnome.Characters/org.gnome.Characters.*.gresource
%dir %{_datadir}/org.gnome.Characters/gir-1.0
%{_datadir}/org.gnome.Characters/gir-1.0/Gc-1.0.gir
%{_desktopdir}/org.gnome.Characters.desktop
%{_iconsdir}/hicolor/*x*/apps/gnome-characters.png
%{_iconsdir}/hicolor/scalable/categories/characters-*-symbolic.svg
%{_iconsdir}/hicolor/symbolic/apps/gnome-characters-symbolic.svg
