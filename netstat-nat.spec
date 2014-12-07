%define major 1
%define libname %{mklibname} %{name} %{major}

Summary:	Displays NAT connections, managed by netfilter/iptables 
Name:		netstat-nat
Group:		Networking/Other
Version:	1.4.10
Release:	9
License:	GPLv2
Provides:	netstat-nat
Url:		http://tweegy.nl/projects/netstat-nat/
Source0:	%{name}-%{version}.tar.bz2

%description
Netstat-nat is a small program written in C. It displays NAT connections, 
managed by netfilter/iptables which comes with the > 2.4.x linux kernels. 
The program reads its information from '/proc/net/ip_conntrack', which is 
the temporary conntrack-storage of netfilter. (http://netfilter.samba.org/)
Netstat-nat takes several arguments (but not needed).

%prep
%setup -q

%build
%configure2_5x
%make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m755 netstat-nat %{buildroot}%{_bindir}/netstat-nat
install -m644 netstat-nat.1 %{buildroot}%{_mandir}/man1/netstat-nat.1

%files
%doc AUTHORS COPYING INSTALL README
%{_bindir}/netstat-nat
%{_mandir}/man1/netstat-nat.*

