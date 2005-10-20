Summary:	X protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u X i pomocnicze
Name:		xorg-proto-xproto
Version:	7.0.1
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/proto/xproto-%{version}.tar.bz2
# Source0-md5:	5fcb850e1779a93d85ae7c59a3852b86
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u X i pomocnicze.

%package devel
Summary:	X protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u X i pomocnicze
Group:		X11/Development/Libraries
Obsoletes:	xproto

%description devel
X protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u X i pomocnicze.

%prep
%setup -q -n xproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc AUTHORS
%{_includedir}/X11/*.h
%{_pkgconfigdir}/xproto.pc
