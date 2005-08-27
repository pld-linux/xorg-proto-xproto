Summary:	X protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u X i pomocnicze
Name:		xorg-proto-xproto
Version:	7.0
Release:	0.02
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/proto/xproto-%{version}.tar.bz2
# Source0-md5:	360b01ad138326e674641ae931db871f
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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
