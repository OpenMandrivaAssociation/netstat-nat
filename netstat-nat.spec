%define name   netstat-nat 
%define version 1.4.10
%define release %mkrel 2
%define lib_major 1
%define lib_name %{mklibname} %{name} %{lib_major}

Name:           %{name}
Summary: 	Displays NAT connections, managed by netfilter/iptables 
Group:		Networking/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Version:        %{version}
Release:        %{release}
License: 	GPL
URL:		http://tweegy.nl/projects/netstat-nat/
#Requires: 	
Provides:	netstat-nat
Prefix:         %{_prefix}
Source:         %{name}-%{version}.tar.bz2
#Source1:
#Patch0:

%description
Netstat-nat is a small program written in C. It displays NAT connections, 
managed by netfilter/iptables which comes with the > 2.4.x linux kernels. 
The program reads its information from '/proc/net/ip_conntrack', which is 
the temporary conntrack-storage of netfilter. (http://netfilter.samba.org/)
Netstat-nat takes several arguments (but not needed).

%prep
rm -rf ${RPM_BUILD_ROOT}
%setup -q -n %{name}-%{version}

%build
%configure
%make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m755 $RPM_BUILD_DIR/%{name}-%{version}/netstat-nat %{buildroot}%{_bindir}/netstat-nat
#bzip2 $RPM_BUILD_DIR/%{name}-%{version}/netstat-nat.1
install -m644 $RPM_BUILD_DIR/%{name}-%{version}/netstat-nat.1 %{buildroot}%{_mandir}/man1/netstat-nat.1

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL README
%attr(644,root,root) %{_mandir}/man1/netstat-nat.*
%attr(755,root,root) %{_bindir}/netstat-nat




%changelog
* Wed Apr 27 2011 Antoine Ginies <aginies@mandriva.com> 1.4.10-1mdv2011.0
+ Revision: 659637
- version 1.4.10

* Wed Feb 16 2011 Antoine Ginies <aginies@mandriva.com> 1.4.9-6
+ Revision: 638052
- just for testing purpose

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.9-5mdv2011.0
+ Revision: 613035
- the mass rebuild of 2010.1 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.4.9-4mdv2010.0
+ Revision: 440326
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.4.9-3mdv2009.0
+ Revision: 253854
- rebuild
- fix no-buildroot-tag

* Tue Feb 12 2008 Antoine Ginies <aginies@mandriva.com> 1.4.9-1mdv2008.1
+ Revision: 165759
- new release 1.4.9

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Antoine Ginies <aginies@mandriva.com> 1.4.8-1mdv2008.0
+ Revision: 76929
- update to release 1.4.8

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages

* Mon May 21 2007 Antoine Ginies <aginies@mandriva.com> 1.4.7-1mdv2008.0
+ Revision: 29310
- release 1.4.7


* Thu Mar 01 2007 Antoine Ginies <aginies@mandriva.com> 1.4.6-1mdv2007.0
+ Revision: 130588
- Import netstat-nat

* Tue Aug 08 2006 Antoine Ginies <aginies@mandriva.com> 1.4.6-1mdv2007.0
- use mkrel
- release 1.4.6

* Fri Mar 18 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 1.4.5-1mdk
- release 1.4.5

* Tue May 18 2004 Antoine Ginies <aginies@n2.mandrakesoft.com> 1.4.3-1mdk
- release 1.4.3

