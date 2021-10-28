#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : arrow
Version  : 1.2.1
Release  : 9
URL      : https://files.pythonhosted.org/packages/25/e2/85d4a709a3ea58f8e36b4db9eb7927560a2fa4b6f8f362fb6475962fec51/arrow-1.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/25/e2/85d4a709a3ea58f8e36b4db9eb7927560a2fa4b6f8f362fb6475962fec51/arrow-1.2.1.tar.gz
Summary  : Better dates & times for Python
Group    : Development/Tools
License  : Apache-2.0
Requires: arrow-license = %{version}-%{release}
Requires: arrow-python = %{version}-%{release}
Requires: arrow-python3 = %{version}-%{release}
Requires: python-dateutil
Requires: typing_extensions
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dateutil
BuildRequires : tox
BuildRequires : typing_extensions
BuildRequires : virtualenv

%description
Arrow: Better dates & times for Python
======================================
.. start-inclusion-marker-do-not-remove

%package license
Summary: license components for the arrow package.
Group: Default

%description license
license components for the arrow package.


%package python
Summary: python components for the arrow package.
Group: Default
Requires: arrow-python3 = %{version}-%{release}

%description python
python components for the arrow package.


%package python3
Summary: python3 components for the arrow package.
Group: Default
Requires: python3-core
Provides: pypi(arrow)
Requires: pypi(python_dateutil)

%description python3
python3 components for the arrow package.


%prep
%setup -q -n arrow-1.2.1
cd %{_builddir}/arrow-1.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635173287
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
mkdir -p %{buildroot}/usr/share/package-licenses/arrow
cp %{_builddir}/arrow-1.2.1/LICENSE %{buildroot}/usr/share/package-licenses/arrow/1a3af28b6e1b31db5b0d5e4bcd7c1fe4dabe7f7e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/arrow/1a3af28b6e1b31db5b0d5e4bcd7c1fe4dabe7f7e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
