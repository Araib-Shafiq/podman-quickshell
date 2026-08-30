Name:           %{upstream_project}-git
Version:        %{upstream_version}
Release:        1%{?dist}
Summary:        Simple, powerful, and fast stack trace library for C++

License:        MIT
URL:            https://github.com/jeremy-rifkin/cpptrace

Source0:        repo.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  libunwind-devel
BuildRequires:  libdwarf-devel
BuildRequires:  libzstd-devel

Provides:       cpptrace-devel = %{version}

%description
Simple, powerful, and fast stack trace library for C++.

%prep
%setup -q -n %{upstream_project}-%{version}

%build
cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCPPTRACE_UNWIND_WITH_LIBUNWIND=ON \
    -DCPPTRACE_USE_EXTERNAL_LIBDWARF=ON \
    -DCPPTRACE_USE_EXTERNAL_ZSTD=ON \
    -DCPPTRACE_FIND_LIBDWARF_WITH_PKGCONFIG=ON \
    -S . \
    -B build \
    -G Ninja

cmake --build build -j%{?_smp_build_ncpus}%{!?_smp_build_ncpus:1}

%install
rm -rf %{buildroot}

DESTDIR=%{buildroot} cmake --install build

echo "===== INSTALLED FILES ====="
find %{buildroot} \( -type f -o -type l \) -print | sort
echo "===== END INSTALLED FILES ====="


%files
/usr/include/cpptrace/
/usr/include/ctrace/
/usr/lib64/cmake/cpptrace/
/usr/lib64/libcpptrace.a

%changelog
* Mon Aug 31 2026 Package Maintainer - 1.0.4-1
- Initial package
