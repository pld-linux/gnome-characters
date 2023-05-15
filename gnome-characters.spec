# TODO: use gtk4-update-icon-cache
Summary:	Character Map application for GNOME
Summary(pl.UTF-8):	Mapa znaków dla GNOME
Name:		gnome-characters
Version:	43.1
Release:	1
License:	GPL v2+ with BSD parts
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-characters/43/%{name}-%{version}.tar.xz
# Source0-md5:	626b6607ed5a7d6d1177702721930647
URL:		https://wiki.gnome.org/Design/Apps/CharacterMap
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	gjs-devel >= 1.50
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gobject-introspection-devel >= 1.36.0
BuildRequires:	gtk4-devel >= 4.6
BuildRequires:	libadwaita-devel >= 1.2
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	gjs >= 1.50
Requires:	glib2 >= 1:2.26.0
Requires:	gtk4 >= 4.6
Requires:	hicolor-icon-theme
Requires:	libadwaita >= 1.2
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
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang org.gnome.Characters

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f org.gnome.Characters.lang
%defattr(644,root,root,755)
%doc COPYING NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-characters
%dir %{_libdir}/org.gnome.Characters
%attr(755,root,root) %{_libdir}/org.gnome.Characters/libgc.so
%dir %{_libdir}/org.gnome.Characters/girepository-1.0
%{_libdir}/org.gnome.Characters/girepository-1.0/Gc-1.0.typelib
%{_datadir}/dbus-1/services/org.gnome.Characters.service
%{_datadir}/glib-2.0/schemas/org.gnome.Characters.gschema.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Characters.search-provider.ini
%{_datadir}/metainfo/org.gnome.Characters.appdata.xml
%dir %{_datadir}/org.gnome.Characters
%attr(755,root,root) %{_datadir}/org.gnome.Characters/org.gnome.Characters
%{_datadir}/org.gnome.Characters/org.gnome.Characters.*.gresource
%dir %{_datadir}/org.gnome.Characters/gir-1.0
%{_datadir}/org.gnome.Characters/gir-1.0/Gc-1.0.gir
%{_desktopdir}/org.gnome.Characters.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Characters.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Characters-symbolic.svg
