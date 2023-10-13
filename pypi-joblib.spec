#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-joblib
Version  : 1.3.2
Release  : 46
URL      : https://files.pythonhosted.org/packages/15/0f/d3b33b9f106dddef461f6df1872b7881321b247f3d255b87f61a7636f7fe/joblib-1.3.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/15/0f/d3b33b9f106dddef461f6df1872b7881321b247f3d255b87f61a7636f7fe/joblib-1.3.2.tar.gz
Summary  : Lightweight pipelining with Python functions
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-joblib-license = %{version}-%{release}
Requires: pypi-joblib-python = %{version}-%{release}
Requires: pypi-joblib-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
|PyPi| |Azure| |ReadTheDocs| |Codecov|
.. |PyPi| image:: https://badge.fury.io/py/joblib.svg
:target: https://badge.fury.io/py/joblib
:alt: Joblib version

%package license
Summary: license components for the pypi-joblib package.
Group: Default

%description license
license components for the pypi-joblib package.


%package python
Summary: python components for the pypi-joblib package.
Group: Default
Requires: pypi-joblib-python3 = %{version}-%{release}

%description python
python components for the pypi-joblib package.


%package python3
Summary: python3 components for the pypi-joblib package.
Group: Default
Requires: python3-core
Provides: pypi(joblib)

%description python3
python3 components for the pypi-joblib package.


%prep
%setup -q -n joblib-1.3.2
cd %{_builddir}/joblib-1.3.2
pushd ..
cp -a joblib-1.3.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1691593191
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-joblib
cp %{_builddir}/joblib-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-joblib/3d53c0cb4680058290f41280e73c3a1236fca1fe || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-joblib/3d53c0cb4680058290f41280e73c3a1236fca1fe

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
