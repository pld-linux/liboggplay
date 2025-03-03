#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	A library to decode from multiple ogg streams synchronously
Summary(pl.UTF-8):	Biblioteka do synchronicznego dekodowania wielu strumieni ogg
Name:		liboggplay
Version:	0.3.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://downloads.xiph.org/releases/liboggplay/%{name}-%{version}.tar.gz
# Source0-md5:	1e5813a38570c26511aba39b7d2a8f31
URL:		https://www.xiph.org/ogg/
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	doxygen
BuildRequires:	imlib2-devel
BuildRequires:	libfishsound-devel >= 0.9.1
BuildRequires:	libkate-devel
BuildRequires:	liboggz-devel >= 0.9.8
BuildRequires:	libskeleton-devel
BuildRequires:	libtheora-devel
BuildRequires:	libtiger-devel >= 0.3.1
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
Requires:	libfishsound >= 0.9.1
Requires:	liboggz >= 0.9.8
Requires:	libtiger >= 0.3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library to decode from multiple ogg streams synchronously.

%description -l pl.UTF-8
Biblioteka do synchronicznego dekodowania wielu strumieni ogg.

%package devel
Summary:	Header files for liboggplay library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki liboggplay
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libfishsound-devel >= 0.9.1
Requires:	libkate-devel
Requires:	liboggz-devel >= 0.9.8
Requires:	libskeleton-devel
Requires:	libtheora-devel
Requires:	libtiger-devel >= 0.3.1

%description devel
Header files for liboggplay library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki liboggplay.

%package static
Summary:	Static liboggplay library
Summary(pl.UTF-8):	Statyczna biblioteka liboggplay
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static liboggplay library.

%description static -l pl.UTF-8
Statyczna biblioteka liboggplay.

%package apidocs
Summary:	API documentation for liboggplay library
Summary(pl.UTF-8):	Dokumentacja API biblioteki liboggplay
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for liboggplay library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki liboggplay.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# should not be installed
%{__rm} $RPM_BUILD_ROOT%{_pkgconfigdir}/oggplay-uninstalled.pc
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/liboggplay.la

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/liboggplay

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/oggplay-dump-first-frame
%attr(755,root,root) %{_bindir}/oggplay-info
%attr(755,root,root) %{_libdir}/liboggplay.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboggplay.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboggplay.so
%{_includedir}/oggplay
%{_pkgconfigdir}/oggplay.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/liboggplay.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc doc/liboggplay/html/*
