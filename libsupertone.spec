%define	major 0
%define libname %mklibname supertone %{major}
%define develname %mklibname supertone -d

Summary:	A library for supervisory tone detection and generation
Name:		libsupertone
Version:	0.0.2
Release:	%mkrel 7
License:	GPL
Group:		System/Libraries
URL:		http://www.soft-switch.org/libsupertone
Source0:	http://www.soft-switch.org/libsupertone/libsupertone-0.0.2.tar.bz2
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
BuildRequires:	libtool
BuildRequires:	tiff-devel >= 3.6.1-3mdk
BuildRequires:	libxml2-devel
BuildRequires:	jpeg-devel
BuildRequires:	file
BuildRequires:  spandsp-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
libsupertone is a library for the detection and generation of supervisory tones
on telephony interfaces.

%package -n	%{libname}
Summary:	Steve's SpanDSP library for telephony spans
Group:          System/Libraries

%description -n	%{libname}
libsupertone is a library for the detection and generation of supervisory tones
on telephony interfaces.

%package -n	%{develname}
Summary:	Header files and libraries needed for development with libsupertone
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname supertone 0 -d}

%description -n	%{develname}
This package includes the header files and libraries needed for
developing programs using libsupertone.

%prep

%setup -q

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

%build
autoreconf -fi
%configure2_5x

make CFLAGS="%{optflags} -fPIC"

%install
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-, root, root)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
