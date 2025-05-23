# fix bogs requires
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^typelib\\(GtkosxApplication

Name:		zim
Version:	0.76.3
Release:	1
Summary:	A desktop wiki and outliner
Source:		https://www.zim-wiki.org/downloads/%{name}-%{version}.tar.gz
License:	GPLv2
Group:		Editors
Url:		https://www.zim-wiki.org/
BuildRequires:	pkgconfig(python)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:	python%{pyver}dist(pygobject)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	typelib(GObject)
BuildRequires:	typelib(Gtk)
BuildRequires:	typelib(Gdk)
BuildRequires:	typelib(GdkPixbuf)
BuildRequires:	typelib(Gio)
BuildRequires:	typelib(GLib)
BuildRequires:	typelib(GObject)
BuildRequires:	typelib(Pango)
Requires:	python
Requires:	python-gobject3
Requires:	python%{pyver}dist(pygobject)
Requires:	typelib(Gtk)
Requires:	typelib(Gdk)
Requires:	typelib(GdkPixbuf)
Requires:	typelib(Gio)
Requires:	typelib(GLib)
Requires:	typelib(GObject)
Requires:	typelib(Pango)
Recommends:	typelib(GtkSource)
Recommends:	typelib(GtkSpell)
Suggests:	pyxdg
Suggests:	xdg-utils
BuildArch:	noarch

%description
Zim is a WYSIWYG text editor written in Gtk2-Perl which aims to bring
the concept of a wiki to your desktop. Every page is saved as a text
file with wiki markup. Pages can contain links to other pages, and are
saved automatically. Creating a new page is as easy as linking to a
non-existing page. Pages are ordered in a hierarchical structure that
gives it the look and feel of an outliner. This tool is intended to
keep track of TODO lists or to serve as a personal scratch book.

%prep
%autosetup -p1  -n %{name}-%{version}
# remove tarball egg-info
rm -rf %{name}.egg-info

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}
sed -i 's|^#!python$|#!/usr/bin/python|' %{buildroot}/usr/bin/zim

#install icons
%__install -D -m 0644 data/zim.png %{buildroot}%{_iconsdir}/zim.png
%__install -D -m 0644 data/zim.png %{buildroot}%{_iconsdir}/hicolor/64x64/mimetypes/application-x-zim-notebook.png
%__install -D -m 0644 data/zim.png %{buildroot}%{_iconsdir}/hicolor/64x64/mimetypes/gnome-mime-application-x-zim-notebook.png

%find_lang %{name}

%clean

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/org.zim_wiki.Zim.desktop
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}-py%{python_version}.*info
%{_mandir}/man1/%{name}*
#{_datadir}/pixmaps/%%{name}.png
%{_datadir}/mime/*
%{_datadir}/metainfo/org.zim_wiki.Zim.appdata.xml
%{_iconsdir}/%{name}.png
%{_iconsdir}/hicolor/*/*/*
%{_iconsdir}/ubuntu*/*/*/*
%doc README.md
%license LICENSE
