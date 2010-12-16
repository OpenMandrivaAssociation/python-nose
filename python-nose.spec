%define module	nose
%define name	python-%{module}
%define version	1.0.0
%define release	%mkrel 1

Summary:	Unittest-based testing framework for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.gz
License:	LGPLv2+
Group:		Development/Python
Url:		http://python-nose.googlecode.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-sphinx >= 0.6.0
%py_requires -d

%description
nose extends the test loading and running features of unittest, making it easier
to write, find and run tests.

By default, nose will run tests in files or directories under the current
working directory whose names include "test" or "Test" at a word boundary (like
"test_this" or "functional_test" or "TestClass" but not "libtest"). Test output
is similar to that of unittest, but also includes captured stdout output from
failing tests, for easy print-style debugging.

These features, and many more, are customizable through the use of plugins.
Plugins included with nose provide support for doctest, code coverage and
profiling, flexible attribute-based test selection, output capture and more.

%prep
%setup -q -n %{module}-%{version}

%install
%__make -C doc/ html

%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} 
%__mkdir -p %{buildroot}%{_mandir}/man1/
%__mv %{buildroot}/usr/man/man1/nosetests.1 %{buildroot}%{_mandir}/man1/
%__lzma -z %{buildroot}%{_mandir}/man1/nosetests.1

%clean
%__rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc AUTHORS CHANGELOG NEWS README.txt lgpl.txt examples/ doc/.build/html
%{_bindir}/*
%{py_sitedir}/*.egg-info
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}*/*
%{_mandir}/man1/nosetests.*
