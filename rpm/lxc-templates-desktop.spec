Name:           lxc-templates-desktop
Version:        1.2
Release:        1
Summary:        LXC templates adapted to sailfishOS
Packager:       sailfish containers
Group:          Application/Other
License:        GPL
URL:            https://github.com/sailfish-containers
Source0:        %{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(Qt5Core)
BuildArch:      noarch
Requires:       lxc, lxc-templates

%description
LXC templates adapted to SailfishOS

%prep
%setup -q -n %{name}-%{version}

%build
%qmake5

%install
# clean build root
rm -rf $RPM_BUILD_ROOT
%qmake5_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir /usr/share/lxc/templates
%attr(4755, root, root) /usr/share/lxc/templates/lxc-sfos-download
%doc

%changelog
* Fri Apr 3 2020 sailfish containers
- moved guest scripts from lxc-templates-desktop to harbour-containers
- removed default guest mountpoint

* Mon Feb 24 2020 sailfish containers
- multiarch support
- QT scaling fix
- improved setup_desktop.sh
- moved lxc cache to /home/.lxc

* Fri Feb 21 2020 sailfish containers
- fixed missing dependency thanks to mosen and kabouik
- first public pre-release build available

* Tue Feb 18 2020 sailfish containers
- containers rootfs moved to /home/.lxc
- rewrote config part
- various bugfixes

* Fri Feb 14 2020 sailfish containers
- fixed wget check, thanks to Craig
- fixed download steps

* Tue Feb 11 2020 sailfish containers
- release 1.0 - initial release
