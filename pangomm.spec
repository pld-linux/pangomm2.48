#
%define		apiver	1.4
#
Summary:	A C++ interface for pango library
Summary(pl.UTF-8):	Interfejs C++ dla biblioteki pango
Name:		pangomm
Version:	2.27.1
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pangomm/2.27/%{name}-%{version}.tar.bz2
# Source0-md5:	71936f2d2c5b2d37ca950dba188cab00
URL:		http://www.gtkmm.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	cairomm-devel >= 1.6.3
BuildRequires:	glibmm-devel >= 2.22.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	mm-common >= 0.7.1
BuildRequires:	pango-devel >= 1:1.24.0
BuildRequires:	perl-base >= 1:5.6.0
BuildRequires:	pkgconfig
Requires:	cairomm >= 1.6.3
Requires:	glibmm >= 2.16.0
Requires:	pango >= 1:1.24.0
Provides:	gtkmm-pango
Obsoletes:	gtkmm-pango
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A C++ interface for pango library.

%description -l pl.UTF-8
Interfejs C++ dla biblioteki pango.

%package devel
Summary:	Header files for pangomm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki pangomm
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairomm-devel >= 1.6.3
Requires:	glibmm-devel >= 2.16.0
Requires:	pango-devel >= 1:1.24.0
Provides:	gtkmm-pango-devel
Obsoletes:	gtkmm-pango-devel

%description devel
Header files for pangomm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki pangomm.

%package static
Summary:	Static pangomm library
Summary(pl.UTF-8):	Statyczna biblioteka pangomm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	gtkmm-pango-static
Obsoletes:	gtkmm-pango-static

%description static
Static pangomm library.

%description static -l pl.UTF-8
Statyczna biblioteka pangomm.

%package apidocs
Summary:	pangomm library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki pangomm
Group:		Documentation
Requires:	devhelp

%description apidocs
pangomm library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki pangomm.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libpangomm-%{apiver}.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpangomm-%{apiver}.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpangomm-%{apiver}.so
%{_includedir}/pangomm-%{apiver}
%{_libdir}/pangomm-%{apiver}
%{_pkgconfigdir}/pangomm-%{apiver}.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libpangomm-%{apiver}.a

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/pangomm-%{apiver}
%{_datadir}/devhelp/books/pangomm-%{apiver}
