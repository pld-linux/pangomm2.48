%define		apiver	2.48

%define	cairomm_ver	1.15.1
%define	glibmm_ver	2.68.0
%define	pango_ver	1:1.54.0
Summary:	A C++ interface for pango library
Summary(pl.UTF-8):	Interfejs C++ dla biblioteki pango
Name:		pangomm2.48
Version:	2.54.0
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	https://download.gnome.org/sources/pangomm/2.54/pangomm-%{version}.tar.xz
# Source0-md5:	19e0266fdd4b47d5fadd9f16ee5f728d
URL:		https://www.gtkmm.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.11
BuildRequires:	doxygen >= 1:1.8.9
BuildRequires:	cairomm1.16-devel >= %{cairomm_ver}
BuildRequires:	glibmm2.68-devel >= %{glibmm_ver}
BuildRequires:	graphviz
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	libtool >= 2:2.0
BuildRequires:	mm-common >= 0.9.12
BuildRequires:	pango-devel >= %{pango_ver}
BuildRequires:	perl-base >= 1:5.6.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	cairomm1.16 >= %{cairomm_ver}
Requires:	glibmm2.68 >= %{glibmm_ver}
Requires:	pango >= %{pango_ver}
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
Requires:	cairomm1.16-devel >= %{cairomm_ver}
Requires:	glibmm2.68-devel >= %{glibmm_ver}
Requires:	libstdc++-devel >= 6:7
Requires:	pango-devel >= %{pango_ver}

%description devel
Header files for pangomm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki pangomm.

%package static
Summary:	Static pangomm library
Summary(pl.UTF-8):	Statyczna biblioteka pangomm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static pangomm library.

%description static -l pl.UTF-8
Statyczna biblioteka pangomm.

%package apidocs
Summary:	pangomm library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki pangomm
Group:		Documentation
Requires:	devhelp
BuildArch:	noarch

%description apidocs
pangomm library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki pangomm.

%prep
%setup -q -n pangomm-%{version}

%build
mm-common-prepare --copy --force
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-maintainer-mode \
	--disable-silent-rules \
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
%doc ChangeLog NEWS README.md
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
