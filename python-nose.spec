%bcond_without bootstrap
%define module	nose

Summary:	Unittest-based testing framework for Python

Name:		python-%{module}
Version:	1.3.7
Release:	9
License:	LGPLv2+
Group:		Development/Python
Url:		https://github.com/nose-devs/nose
Source0:	https://github.com/nose-devs/nose/archive/release_%{version}.tar.gz
# Make compatible with coverage 4.1
# https://github.com/nose-devs/nose/pull/1004
Patch0:		python-nose-coverage4.patch
# Fix python 3.5 compat
# https://github.com/nose-devs/nose/pull/983
Patch1:		python-nose-py35.patch
# Fix UnicodeDecodeError with captured output
# https://github.com/nose-devs/nose/pull/988
Patch2:		python-nose-unicode.patch
# Allow docutils to read utf-8 source
Patch3:		python-nose-readunicode.patch
# Fix Python 3.6 compatibility
# Python now returns ModuleNotFoundError instead of the previous ImportError
# https://github.com/nose-devs/nose/pull/1029
Patch4:		python-nose-py36.patch
# Remove a SyntaxWarning (other projects may treat it as error)
Patch5:		python-nose-py38.patch
Patch6:		https://src.fedoraproject.org/rpms/python-nose/raw/rawhide/f/python-nose-py311.patch
Patch7:		https://src.fedoraproject.org/rpms/python-nose/raw/rawhide/f/python-nose-py311-doctest.patch


BuildArch:	noarch
%if ! %{with bootstrap}
BuildRequires:	python-sphinx >= 0.6.0
%endif
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
%rename		python3-%{module}

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
%autosetup -p1 -n %{module}-release_%{version}

%install
2to3 --write --nobackups --no-diffs .
2to3 --write --nobackups --no-diffs -d $(find -name '*.rst')

# We need python3-sphinx first
%if ! %{with bootstrap}
%make -C doc/ html
%endif

mkdir -p %{buildroot}%{_mandir}/man1/
python setup.py install --root=%{buildroot}
mv %{buildroot}/usr/man/man1/nosetests.1 %{buildroot}%{_mandir}/man1/
ln -sf nosetests %{buildroot}%{_bindir}/nosetests-3
cd ..

%files
%doc AUTHORS CHANGELOG NEWS README.txt lgpl.txt examples
%if ! %{with bootstrap}
%doc doc/.build/html
%endif
%{_bindir}/nosetests
%{_bindir}/nosetests-3*
%{_mandir}/man1/nosetests.*
%{py_puresitedir}/*
