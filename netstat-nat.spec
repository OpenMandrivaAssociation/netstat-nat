%define name   netstat-nat 
%define version 1.4.7
%define release %mkrel 1
%define lib_major 1
%define lib_name %{mklibname} %{name} %{lib_major}

Name:           %{name}
Summary: 	Displays NAT connections, managed by netfilter/iptables 
Group:		Networking/Other
Version:        %{version}
Release:        %{release}
License: 	GPL
URL:		http://tweegy.demon.nl/projects/netstat-nat/index.html
#Requires: 	
Provides:	netstat-nat
BuildRoot:      %{_tmppath}/%{name}-%{version}
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


