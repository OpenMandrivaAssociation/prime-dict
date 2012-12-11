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


%changelog
* Sat May 30 2009 Funda Wang <fundawang@mandriva.org> 1.0.0-11.20090507.1mdv2010.0
+ Revision: 381403
- BR ruby
- New ut patches

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.0-7mdv2009.0
+ Revision: 259293
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.0-6mdv2009.0
+ Revision: 247218
- rebuild

* Fri Mar 14 2008 Funda Wang <fundawang@mandriva.org> 1.0.0-4mdv2008.1
+ Revision: 187762
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-3mdv2008.0
+ Revision: 90173
- rebuild

* Thu Aug 23 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0.0-2mdv2008.0
+ Revision: 70396
- use %%mkrel


* Fri Apr 15 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.0-1mdk
- fix rpmlint warnings
- new release (UTUMI Hirosi <utuhiro78@yahoo.co.jp>)

* Fri Feb 18 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.8.7-1mdk
- new release
- change URL
- spec cleanup

* Mon Aug 30 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.8.4-1mdk
- initial spec for mdk

