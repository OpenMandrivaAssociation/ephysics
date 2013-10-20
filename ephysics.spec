%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

%define svnrev 77544

Summary:	A wrapper between Ecore, Evas and Bullet Physics
Name:		ephysics
Version:	0.1.99.%{svnrev}
Release:	2
License:	BSD
Group:		Graphical desktop/Enlightenment
Url:		http://trac.enlightenment.org/e/browser/trunk/ephysics
Source0:	%{name}-%{version}.tar.bz2
Patch0:		ephysics-0.1.99.77544-linkage.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig(bullet)
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(ecore-evas)
BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(evas)

%description
EPhysics is a library that manages Ecore, Evas and Bullet Physics into
an easy to use way. It's a kind of wrapper, a glue, between these libraries.
It's not intended to be a physics library (we already have many out there).

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Ephysics Dynamic Library
Group:		System/Libraries

%description -n %{libname}
Ephysics is a wrapper library between Ecore, Evas and Bullet Physics.

%files -n %{libname}
%{_libdir}/libephysics.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Ephysics headers, static libraries, documentation and test programs
Group:		Development/Other
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Headers, static libraries, test programs and documentation for ephysics.

%files -n %{devname}
%{_includedir}/ephysics-0/
%{_libdir}/pkgconfig/ephysics.pc
%{_libdir}/libephysics.so

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
NOCONFIGURE=yes ./autogen.sh
%configure --disable-static
%make

%install
%makeinstall_std

