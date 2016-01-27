%define snap %nil
%define debug_package %nil
%define debugcflags %nil

Summary:	Papyros desktop shell
Name:		settings-app
Version:	0.1.0
Release:	1
License:	GPLv2
Group:		Graphical desktop/Other
URL:		https://github.com/papyros/settings-app
# git clone https://github.com/papyros/settings-app.git
# git archive --format=tar --prefix settings-app-0.1.0-$(date +%Y%m%d)/ HEAD | xz -vf > settings-app-0.1.0-$(date +%Y%m%d).tar.xz

Source0:	%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Papyros)

%description
The system settings app for Papyros.

%prep
%setup -q

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build

%files
%dir %{_datadir}/papyros-settings/modules
%{_bindir}/papyros-settings
%{_datadir}/appdata/io.papyros.Settings.appdata.xml
%{_datadir}/applications/io.papyros.Settings.desktop
%{_datadir}/papyros-settings/modules/*
