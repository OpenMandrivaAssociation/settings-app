%define snap 20150709
%define debug_package %nil
%define debugcflags %nil

Summary:	Papyros desktop shell
Name:		settings-app
Version:	0.0.5
Release:	1.%{snap}.2
License:	GPLv2
Group:		Graphical desktop/Other
URL:		https://github.com/papyros/settings-app
# git clone https://github.com/papyros/settings-app.git
# git archive --format=tar --prefix settings-app-0.0.5-$(date +%Y%m%d)/ HEAD | xz -vf > settings-app-0.0.5-$(date +%Y%m%d).tar.xz

Source0:	%{name}-%{version}-%{snap}.tar.xz
BuildRequires:	qt5-devel

%description
The system settings app for Papyros.

%prep
%setup -qn %{name}-%{version}-%{snap}

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/papyros-settings
%{_datadir}/papyros-settings/app/
%{_datadir}/papyros-settings/modules/
