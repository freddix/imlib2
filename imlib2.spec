Summary:	Powerful image loading and rendering library
Name:		imlib2
Version:	1.4.5
Release:	4
License:	BSD-like
Group:		X11/Libraries
Source0:	http://downloads.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
# Source0-md5:	8406786d3852b1b1322c2e4bee3c9e5c
Patch0:		%{name}-giflib.patch
URL:		http://enlightenment.org/p.php?p=about/libs/imlib2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	freetype-devel
BuildRequires:	giflib-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	xorg-libXext-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Imlib2 is an advanced replacement library for libraries like libXpm
that provides many more features with much greater flexibility and
speed than standard libraries, including font rasterization, rotation,
RGBA space rendering and blending, dynamic binary filters, scripting,
and more.

%package devel
Summary:	Imlib2 header files and development documentation
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	freetype-devel
Requires:	xorg-libXext-devel
Requires:	zlib-devel

%description devel
Header files and development documentation for Imlib2.

%package static
Summary:	Imlib2 static libraries
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Imlib2 static libraries.

%prep
%setup -q
%patch0 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%ifarch i686
	--enable-mmx	\
	%endif
	--enable-visibility-hiding
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/imlib2/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING-PLAIN README
%attr(755,root,root) %{_bindir}/imlib2_*
%attr(755,root,root) %{_libdir}/imlib2/filters/*.so
%attr(755,root,root) %{_libdir}/imlib2/loaders/*.so

%attr(755,root,root) %ghost %{_libdir}/libImlib2.so.?
%attr(755,root,root) %{_libdir}/libImlib2.so.*.*.*

%dir %{_libdir}/imlib2
%dir %{_libdir}/imlib2/filters
%dir %{_libdir}/imlib2/loaders
%{_datadir}/imlib2

%files devel
%defattr(644,root,root,755)
%doc doc/{*.gif,*.html}
%attr(755,root,root) %{_bindir}/imlib2-config
%attr(755,root,root) %{_libdir}/libImlib2.so
%{_includedir}/Imlib2.h
%{_pkgconfigdir}/imlib2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libImlib2.a

