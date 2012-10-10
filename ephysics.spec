%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

%define svnrev 77544

Name:		ephysics
Version:	0.1.99.%{svnrev}
Release:	1
Summary:	A wrapper between Ecore, Evas and Bullet Physics
License:	LGPL
Group:		Graphical desktop/Enlightenment
Url:		http://trac.enlightenment.org/e/browser/trunk/ephysics
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(ecore-evas)
BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(bullet)

%description
EPhysics is a library that manages Ecore, Evas and Bullet Physics into
an easy to use way. It's a kind of wrapper, a glue, between these libraries.
It's not intended to be a physics library (we already have many out there).

%package -n %{libname}
Summary:	Ephysics Dynamic Libraries
Group:		System/Libraries

%description -n %{libname}
Ephysics is core EFL (Enlightenment Foundation Libraries) library to handle various data types.

%package -n %{devname}
Summary:	Ephysics headers, static libraries, documentation and test programs
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Headers, static libraries, test programs and documentation for ephysics.

%prep
%setup -q

%build
%configure --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libephysics.so.%{major}*

%files -n %{devname}
%{_includedir}/ephysics-0/
%{_libdir}/pkgconfig/ephysics.pc
%{_libdir}/libephysics.so

