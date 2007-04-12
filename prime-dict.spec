%define version	1.0.0
%define release	1mdk

Name:		prime-dict
Summary:	Dictionaries for PRIME
Version:		%{version}
Release:		%{release}
URL:			http://sourceforge.jp/projects/prime/
License:		GPL
Group:		System/Internationalization
Source0:		%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Dictionaries for PRIME.


%prep
%setup -q

%build
# fix build:
%define __libtoolize /bin/true

%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc ChangeLog COPYING 
%{_libdir}/site_ruby*
%{_datadir}/prime/*


