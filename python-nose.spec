%define bootstrap 1
%define module	nose

Summary:	Unittest-based testing framework for Python

Name:		python-%{module}
Version:	1.3.7
Release:	2
License:	LGPLv2+
Group:		Development/Python
Url:		https://github.com/nose-devs/nose
Source0:	https://github.com/nose-devs/nose/archive/release_%{version}.tar.gz
BuildArch:	noarch
%if !%{bootstrap}
BuildRequires:	python-sphinx >= 0.6.0
%endif
BuildRequires:	python2-distribute
BuildRequires:	python-distribute
BuildRequires:	pkgconfig(python)
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

%package -n python2-%{module}
Summary:	Unittest-based testing framework for Python2

Requires:	python2

%description -n python2-%{module}
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
%setup -q -c
mv %{module}-release_%{version} python2
cp -r python2 python3

%install
# python2 goes first so python3 can overwrite common files
pushd python2
%if !%{bootstrap}
%make -C doc/ html
%endif

python2 setup.py install --root=%{buildroot} 
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}/usr/man/man1/nosetests.1 %{buildroot}%{_mandir}/man1/python2-nosetests.1
mv %{buildroot}/%{_bindir}/nosetests %{buildroot}/%{_bindir}/python2-nosetests
popd

pushd python3
# We need python3-sphinx first
# %if !%{bootstrap}
# %make -C doc/ html
# %endif

mkdir -p %{buildroot}%{_mandir}/man1/
python3 setup.py install --root=%{buildroot}
mv %{buildroot}/usr/man/man1/nosetests.1 %{buildroot}%{_mandir}/man1/
popd


%files 
%doc python3/AUTHORS python3/CHANGELOG python3/NEWS python3/README.txt python3/lgpl.txt python3/examples
%if !%{bootstrap}
%doc python3/doc/.build/html
%endif
%{_bindir}/nosetests
%{_bindir}/nosetests-3*
%{_mandir}/man1/nosetests.*
%{py_puresitedir}/*

%files -n python2-%{module}
%doc python2/AUTHORS python2/CHANGELOG python2/NEWS python2/README.txt python2/lgpl.txt python2/examples
# %if !%{bootstrap}
# %doc python3/doc/.build/html
# %endif
%{_bindir}/nosetests-2*
%{_bindir}/python2-nosetests
%{_mandir}/man1/python2-nosetests.*
%{py2_puresitedir}/*
