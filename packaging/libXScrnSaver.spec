Name:           libXScrnSaver
%define lname	libXss
Version:        1.2.2
Release:        0
License:        MIT
Summary:        X11 Screen Saver extension client library
Url:            http://xorg.freedesktop.org/
Group:          Development/Libraries/C and C++

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXScrnSaver
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXScrnSaver/
Source:         %{name}-%{version}.tar.bz2
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(scrnsaverproto) >= 1.2
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%description
The X Window System provides support for changing the image on a
display screen after a user-settable period of inactivity to avoid
burning the cathode ray tube phosphors. This extension allows an
external "screen saver" client to detect when the alternate image is
to be displayed and to provide the graphics.

%package -n %lname
Summary:        X11 Screen Saver extension client library
Group:          System/Libraries

%description -n %lname
The X Window System provides support for changing the image on a
display screen after a user-settable period of inactivity to avoid
burning the cathode ray tube phosphors. This extension allows an
external "screen saver" client to detect when the alternate image is
to be displayed and to provide the graphics.

%package devel
Summary:        Development files for the X11 Screen Saver extension library
Group:          Development/Libraries/C and C++
Requires:       %lname = %{version}

%description devel
The X Window System provides support for changing the image on a
display screen after a user-settable period of inactivity to avoid
burning the cathode ray tube phosphors. This extension allows an
external "screen saver" client to detect when the alternate image is
to be displayed and to provide the graphics.

This package contains the development headers for the library found
in %lname.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
%fdupes %{buildroot}

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%{_libdir}/libXss.so.1*

%files devel
%defattr(-,root,root)
%{_includedir}/X11/*
%{_libdir}/libXss.so
%{_libdir}/pkgconfig/xscrnsaver.pc
%{_mandir}/man3/*

%changelog
