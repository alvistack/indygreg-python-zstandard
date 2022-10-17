# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-zstandard
Epoch: 100
Version: 0.17.0
Release: 1%{?dist}
Summary: Zstandard bindings for Python
License: BSD-3-Clause
URL: https://github.com/indygreg/python-zstandard/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-cffi
BuildRequires: python3-cython
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Python bindings to zstandard compression library.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-zstandard
Summary: Zstandard bindings for Python
Requires: python3
Provides: python3-zstandard = %{epoch}:%{version}-%{release}
Provides: python3dist(zstandard) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-zstandard = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(zstandard) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-zstandard = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(zstandard) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-zstandard
Python bindings to zstandard compression library.

%files -n python%{python3_version_nodots}-zstandard
%license LICENSE
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-zstandard
Summary: Zstandard bindings for Python
Requires: python3
Provides: python3-zstandard = %{epoch}:%{version}-%{release}
Provides: python3dist(zstandard) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-zstandard = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(zstandard) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-zstandard = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(zstandard) = %{epoch}:%{version}-%{release}

%description -n python3-zstandard
Python bindings to zstandard compression library.

%files -n python3-zstandard
%license LICENSE
%{python3_sitearch}/*
%endif

%changelog
