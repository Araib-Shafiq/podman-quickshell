Name:           %{upstream_project}-git
Version:        %{upstream_version}
Release:        1%{?dist}
Summary:        Flexible toolkit for making desktop shells with QtQuick

License:        LGPL-3.0-only
URL:            https://github.com/quickshell-mirror/quickshell

Source0:        repo.tar.gz

# Build tools
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

# Qt
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtdeclarative-private-devel
BuildRequires:  qt6-qtshadertools-devel
BuildRequires:  qt6-qtwayland-devel

# CLI11
BuildRequires:  cli11-devel

# Crash handling
BuildRequires:  cpptrace-devel
BuildRequires:  libunwind-devel
BuildRequires:  libdwarf-devel
BuildRequires:  libzstd-devel

# Memory allocator
BuildRequires:  jemalloc-devel

# Wayland
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel

# X11
BuildRequires:  libxcb-devel

# Graphics
BuildRequires:  libdrm-devel
BuildRequires:  mesa-libgbm-devel

# PipeWire
BuildRequires:  pipewire-devel

# PAM
BuildRequires:  pam-devel

# Polkit
BuildRequires:  polkit-devel

# D-Bus
BuildRequires:  dbus-devel

%description
Quickshell is a flexible toolkit for making desktop shells with QtQuick,
supporting both Wayland and X11.

%prep
%setup -q -n %{upstream_project}-%{version}

%build
cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DDISTRIBUTOR="Fedora" \
    -S . \
    -B build \
    -G Ninja

cmake --build build \
    -j%{?_smp_build_ncpus}%{!?_smp_build_ncpus:1}

%install
rm -rf %{buildroot}

DESTDIR=%{buildroot} cmake --install build

%files
%license LICENSE
%doc README.md

%{_bindir}/quickshell
%{_bindir}/qs

%{_datadir}/applications/org.quickshell.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.quickshell.svg

%changelog
* Mon Aug 31 2026 Package Maintainer - %{version}-1
- Initial package