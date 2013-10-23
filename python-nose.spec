%define bootstrap 0

%define module	nose

Summary:	Unittest-based testing framework for Python
Name:		python-%{module}
Version:	1.3.0
Release:	1
Source0:	https://pypi.python.org/packages/source/n/nose/nose-%{version}.tar.gz
License:	LGPLv2+
Group:		Development/Python
Url:		http://python-nose.googlecode.com/
BuildArch:	noarch
%if !%{bootstrap}
BuildRequires:	python-sphinx >= 0.6.0
%endif
BuildRequires:	python-distribute
%py_requires -d

%description
nose extends the test loading and running features of unittest,
making it easier to write, find and run tests.

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
%if !%{bootstrap}
%__make -C doc/ html
%endif

%__python setup.py install --root=%{buildroot} 
%__mkdir -p %{buildroot}%{_mandir}/man1/
%__mv %{buildroot}/usr/man/man1/nosetests.1 %{buildroot}%{_mandir}/man1/
%__lzma -z %{buildroot}%{_mandir}/man1/nosetests.1

%files 
%doc AUTHORS CHANGELOG NEWS README.txt lgpl.txt examples
%if !%{bootstrap}
%doc doc/.build/html
%endif
%{_bindir}/*
%{_mandir}/man1/nosetests.*
%{py_puresitedir}/*

%changelog
* Fri Feb  8 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.2.1-4
- Rebuild after rebootstrap of python-sphinx.

* Fri Feb  8 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.2.1-3
- Add python-distribute to build requires.

