Summary:	SASL Tcl extension
Summary(pl):	Rozszerzenie SASL dla Tcl
Name:		tclsasl
Version:	1.0
Release:	1
License:	distributable
Group:		Development/Languages/Tcl
Source0:	http://beepcore-tcl.sourceforge.net/%{name}-%{version}.tgz
# Source0-md5:	6d8cc2bd31d9d41a999a72817308d165
Patch0:		%{name}-CFLAGS.patch
Patch1:		%{name}-automake.patch
Patch2:		%{name}-DESTDIR.patch
URL:		http://beepcore-tcl.sourceforge.net/%{name}.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cyrus-sasl-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	tcl-devel >= 8.3.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tcl SASL provides a Tcl interface to the Cyrus SASLv2 library.

%description -l pl
Tcl SASL udostêpnia interfejs Tcl-a do biblioteki Cyrus SASLv2.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f config/missing
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__automake}
%configure

%{__make} LIB_TCL="-ltcl" LIB_SASL="-lsasl -R /usr/lib/sasl2 -L/usr/lib/sasl2 -lsasldb"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

rm $RPM_BUILD_ROOT%{_libdir}/sasl-*/*.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS doc/tclsasl.html
%{_libdir}/*
