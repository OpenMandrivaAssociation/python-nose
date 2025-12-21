%bcond_without bootstrap
%define module	nose

Summary:	Unittest-based testing framework for Python

Name:		python-%{module}
Version:	1.3.8
Release:	1
License:	LGPLv2+
Group:		Development/Python
Url:		https://github.com/nose-devs/nose
Source0:	https://files.pythonhosted.org/packages/source/n/nose3/nose3-%{version}.tar.gz
# Make compatible with coverage 4.1
# https://github.com/nose-devs/nose/pull/1004
#Patch0:		python-nose-coverage4.patch


BuildArch:	noarch
BuildSystem:	python
BuildRequires:	make
BuildRequires:	python%{pyver}dist(setuptools)
%if ! %{with bootstrap}
BuildRequires:	python-sphinx >= 0.6.0
%endif
%rename		python3-%{module}
# Make sure we can fulfill the 'python%{pyver}dist(nose)' dep used
# everywhere, despite the fact that we're now using the nose3 fork
Provides:	python%{pyver}dist(nose) = %{version}

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

%install -a
# We need python3-sphinx first
%if ! %{with bootstrap}
%make -C doc/ html
%endif

mkdir -p %{buildroot}%{_mandir}/man1/
mv %{buildroot}/usr/man/man1/nosetests.1 %{buildroot}%{_mandir}/man1/
ln -sf nosetests %{buildroot}%{_bindir}/nosetests-3

# Make sure we can fulfill the 'python%{pyver}dist(nose)' dep used
# everywhere, despite the fact that we're now using the nose3 fork
cd %{buildroot}%{py_puresitedir}
for i in nose3*; do
	ln -s $i ${i/nose3/nose}
done

%files
%doc AUTHORS CHANGELOG NEWS README.txt lgpl.txt examples
%if ! %{with bootstrap}
%doc doc/.build/html
%endif
%{_bindir}/nosetests
%{_bindir}/nosetests-3*
%{_mandir}/man1/nosetests.*
%{py_puresitedir}/*
