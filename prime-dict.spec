%define date	20090507
%define debug_package %{nil}

Name:		prime-dict
Summary:	Dictionaries for PRIME
Version:	1.0.0
Release:	11.%{date}.2
URL:		http://sourceforge.jp/projects/prime/
License:	GPL
Group:		System/Internationalization
Source0:	%{name}-%{version}-%{date}ut.tar.bz2
BuildRequires:	ruby

%description
Dictionaries for PRIME.

%prep
%setup -q -n %{name}-%{version}-%{date}ut

%build
%configure2_5x --with-rubydir=%{ruby_sitelibdir}
%make

%install
%makeinstall_std

%files
%doc ChangeLog COPYING 
%{ruby_sitelibdir}/*
%{_datadir}/prime/*
