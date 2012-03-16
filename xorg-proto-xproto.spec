Summary:	X protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu X i pomocnicze
Name:		xorg-proto-xproto
Version:	7.0.23
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/xproto-%{version}.tar.bz2
# Source0-md5:	d4d241a4849167e4e694fe73371c328c
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd43-xml
BuildRequires:	xmlto >= 0.0.22
BuildRequires:	xorg-sgml-doctools >= 1.8
BuildRequires:	xorg-util-util-macros >= 1.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X protocol and ancillary headers.

%description -l pl.UTF-8
Nagłówki protokołu X i pomocnicze.

%package devel
Summary:	X protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu X i pomocnicze
Group:		X11/Development/Libraries
Requires:	filesystem >= 3.0-32
Obsoletes:	xproto

%description devel
X protocol and ancillary headers.

%description devel -l pl.UTF-8
Nagłówki protokołu X i pomocnicze.

%prep
%setup -q -n xproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/X11/extensions

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README specs/*.html specs/SIAddresses/{IPv6,hostname,localuser}.txt
%{_includedir}/X11/*.h
%dir %{_includedir}/X11/extensions
%{_pkgconfigdir}/xproto.pc
