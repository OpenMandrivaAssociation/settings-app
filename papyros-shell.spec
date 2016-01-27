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
BuildRequires:	cmake(papyros)

%description
The system settings app for Papyros.

%prep
%setup -q

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/papyros-settings
%{_datadir}/papyros-settings/app/
%{_datadir}/papyros-settings/modules/
