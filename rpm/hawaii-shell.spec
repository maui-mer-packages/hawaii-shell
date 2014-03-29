# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       hawaii-shell

# >> macros
# << macros

Summary:    Hawaii user interface for desktop and mobile
Version:    0.2.0.1.20140329.599ec8b
Release:    1
Group:      Applications/System
License:    LGPLv2.1+ and GPLv2+
URL:        https://github.com/mauios/hawaii-shell.git
Source0:    hawaii-shell-%{version}.tar.xz
Source100:  hawaii-shell.yaml
Requires:   qt5-qtdeclarative-import-window2
Requires:   qt5-qtsvg-plugin-imageformat-svg
Requires:   qt5-qttools-qdbus
Requires:   qt5-qtquickcontrols
Requires:   hawaii-icon-theme
Requires:   hawaii-wallpapers
Requires:   fluid
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Compositor)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(weston)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  qtaccountsservice-devel
BuildRequires:  qtconfiguration-devel
BuildRequires:  cmake
BuildRequires:  qt5-default
BuildRequires:  bzip2-devel
BuildRequires:  greenisland-devel

%description
Provides Hawaii desktop environment shell.

%package devel
Summary:    Development files for Hawaii
Group:      Development/System
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the files necessary to develop applications |
that interact with Hawaii Shelll.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
find upstream/src/server/ -type f -name "*.cpp" | xargs perl -p -i -e 's, override,,g'
find upstream/src/server/ -type f -name "*.h" | xargs perl -p -i -e 's, override,,g'
# << setup

%build
# >> build pre
# << build pre

%cmake .  \
    -DCMAKE_INSTALL_SYSCONFDIR="%{_sysconfdir}" \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DQTWAYLAND_SCANNER_EXECUTABLE="%{_libdir}/qt5/bin/qtwaylandscanner"

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING.LIB README.md
%{_sysconfdir}/systemd/user/
%{_bindir}/hawaii
%{_bindir}/hawaii-shell
%{_bindir}/hawaii-polkit-agent
%{_bindir}/hawaii-notifications-daemon
%{_libdir}/hawaii/plugins/platformthemes/hawaii.so
%{_libdir}/hawaii/qml/Hawaii/Shell/
%{_libdir}/weston/hawaii-desktop.so
%{_libdir}/libHF1HawaiiShell.so.*
%{_libexecdir}/starthawaii
%{_libexecdir}/hawaii-shell-client
%{_libexecdir}/hawaii-screensaver
%{_datadir}/hawaii/
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_includedir}/HF1/HawaiiShell/
%{_libdir}/cmake/HF1HawaiiShell/*.cmake
%{_libdir}/libHF1HawaiiShell.so
# >> files devel
# << files devel
