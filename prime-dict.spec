%define version	1.0.0
%define release	%mkrel 11.%{date}.1
%define date	20090507

Name:		prime-dict
Summary:	Dictionaries for PRIME
Version:	%{version}
Release:	%{release}
URL:		http://sourceforge.jp/projects/prime/
License:	GPL
Group:		System/Internationalization
Source0:	%{name}-%{version}-%{date}ut.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby

%description
Dictionaries for PRIME.

%prep
%setup -q -n %{name}-%{version}-%{date}ut

%build
%configure2_5x --with-rubydir=%{ruby_sitelibdir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog COPYING 
%{ruby_sitelibdir}/*
%{_datadir}/prime/*
