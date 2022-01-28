#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-arrow
Version  : 1.2.2
Release  : 16
URL      : https://files.pythonhosted.org/packages/48/28/30a5748af715b0ab9c2b81cf08bd9e261e47a6261e247553afb7f6421b24/arrow-1.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/48/28/30a5748af715b0ab9c2b81cf08bd9e261e47a6261e247553afb7f6421b24/arrow-1.2.2.tar.gz
Summary  : Better dates & times for Python
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-arrow-license = %{version}-%{release}
Requires: pypi-arrow-python = %{version}-%{release}
Requires: pypi-arrow-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(python_dateutil)
BuildRequires : pypi(typing_extensions)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
Arrow: Better dates & times for Python
======================================
.. start-inclusion-marker-do-not-remove

%package license
Summary: license components for the pypi-arrow package.
Group: Default

%description license
license components for the pypi-arrow package.


%package python
Summary: python components for the pypi-arrow package.
Group: Default
Requires: pypi-arrow-python3 = %{version}-%{release}

%description python
python components for the pypi-arrow package.


%package python3
Summary: python3 components for the pypi-arrow package.
Group: Default
Requires: python3-core
Provides: pypi(arrow)
Requires: pypi(python_dateutil)
Requires: pypi(typing_extensions)

%description python3
python3 components for the pypi-arrow package.


%prep
%setup -q -n arrow-1.2.2
cd %{_builddir}/arrow-1.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1643386275
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-arrow
cp %{_builddir}/arrow-1.2.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-arrow/1a3af28b6e1b31db5b0d5e4bcd7c1fe4dabe7f7e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-arrow/1a3af28b6e1b31db5b0d5e4bcd7c1fe4dabe7f7e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
