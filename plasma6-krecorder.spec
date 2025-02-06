%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name:		plasma6-krecorder
Version:	24.12.0
Release:	%{?git:0.%{git}.}1
Summary:	Audio recorder for Plasma Mobile
%if %{defined git}
Source0:	https://invent.kde.org/utilities/krecorder/-/archive/%{gitbranch}/krecorder-%{gitbranchd}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/krecorder-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6KirigamiAddons)

%description
Audio recorder for Plasma Mobile

%prep
%autosetup -p1 -n krecorder-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang krecorder

%files -f krecorder.lang
%{_bindir}/krecorder
%{_datadir}/applications/org.kde.krecorder.desktop
%{_datadir}/metainfo/org.kde.krecorder.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/org.kde.krecorder.svg
