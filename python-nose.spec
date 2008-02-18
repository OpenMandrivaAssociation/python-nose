%define module	nose
%define name   	python-%{module}
%define version 0.10.1 
%define release %mkrel 2

Summary: Unittest-based testing framework for Python
Name: 	 %{name}
Version: %{version}
Release: %{release}
Source0: %{module}-%{version}.tar.lzma
License: LGPL
Group: 	 Development/Python
Url: 	 http://code.google.com/p/python-nose/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: python-devel

%description
nose provides an alternate test discovery and running process for
unittest that mimics the behavior of py.test as much as is reasonably
possible without resorting to too much magic.

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
%{py_sitedir}/%{module}*/*
%{_mandir}/man1/nosetests.*

