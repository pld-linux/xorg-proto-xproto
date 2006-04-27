Summary:	X protocol and ancillary headers
Summary(pl):	Nag��wki protoko�u X i pomocnicze
Name:		xorg-proto-xproto
Version:	7.0.5
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/xproto-%{version}.tar.bz2
# Source0-md5:	7ebf5b845817a867f2e4bdcabc33a257
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X protocol and ancillary headers.

%description -l pl
Nag��wki protoko�u X i pomocnicze.

%package devel
Summary:	X protocol and ancillary headers
Summary(pl):	Nag��wki protoko�u X i pomocnicze
Group:		X11/Development/Libraries
Obsoletes:	xproto

%description devel
X protocol and ancillary headers.

%description devel -l pl
Nag��wki protoko�u X i pomocnicze.

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
%doc AUTHORS COPYING ChangeLog
%dir %{_includedir}/X11
%{_includedir}/X11/*.h
%dir %{_includedir}/X11/extensions
%{_pkgconfigdir}/xproto.pc
