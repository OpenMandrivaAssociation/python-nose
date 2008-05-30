%define module	nose
%define name   	python-%{module}
%define version 0.10.2
%define release %mkrel 1

Summary: Unittest-based testing framework for Python
Name: 	 %{name}
Version: %{version}
Release: %{release}
Source0: %{module}-%{version}.tar.lzma
License: LGPLv2+
Group: 	 Development/Python
Url: 	 http://code.google.com/p/python-nose/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel
BuildArch: noarch

%description
nose is a Python test discovery and execution infrastructure
alternative to unittest that mimics the behavior of py.test as much as
is reasonably possible without resorting to too much magic.

%prep
%setup -q -n %{module}-%{version}

%build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} 
%__mkdir -p %{buildroot}%{_mandir}/man1/
%__mv %{buildroot}/usr/man/man1/nosetests.1 %{buildroot}%{_mandir}/man1/
%__lzma -z %{buildroot}%{_mandir}/man1/nosetests.1

%clean
%__rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc AUTHORS CHANGELOG NEWS README.txt examples/ doc/
%{_bindir}/*
%{py_sitedir}/*.egg-info
%{py_sitedir}/%{module}*/*
%{_mandir}/man1/nosetests.*

