%define		_realname	xpenguins-applet

Summary:	Cute little penguins that walk along the tops of your windows
Summary(pl):	Ma�e pingwiny chodz�ce po okienkach
Name:		gnome-applet-xpenguins
Version:	2.1.1
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	http://xpenguins.seul.org/%{_realname}-%{version}.tar.gz
# Source0-md5:	0f54433233ae4904e5fd64e260c5d8ce
URL:		http://xpenguins.seul.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gnome-panel-devel >= 2.2.0
BuildRequires:	xpenguins-themes >= 1.0
Requires(post):	GConf2
Requires(post):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
This program is a GNOME 2 panel applet that animates a friendly family
of penguins in your root window. They drop in from the top of the
screen, walk along the tops of your windows, up the side of your
windows, up the side of the screen, and sometimes even levitate with
their genetically-modified go-go-gadget 'copter ability.

%description -l pl
To jest aplet GNOME 2 animuj�ce przyjazn� rodzin� pingwin�w w g��wnym
okienku. Spadaj� z g�ry ekranu, chodz� po g�rnych kraw�dziach okienek,
czasem nawet lewituj� korzystaj�c z wszczepionego koptera.

%prep
%setup -q -n %{_realname}-%{version}

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{_realname} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun	-p /usr/bin/scrollkeeper-update

%files -f %{_realname}.lang
%defattr(644,root,root,755)
%doc README
%{_sysconfdir}/gconf/schemas/xpenguins-applet.schemas
%attr(755,root,root) %{_libdir}/xpenguins-applet
%{_libdir}/bonobo/servers/*
%{_datadir}/gnome-2.0/ui/*
%{_pixmapsdir}/*.png
%{_omf_dest_dir}/%{_realname}