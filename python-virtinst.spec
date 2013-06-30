# NOTE: currently maintained as part of virt-manager
%define	appname	virtinst
Summary:	Python modules and utilities for installing virtual machines
Summary(pl.UTF-8):	Moduły Pythona i narzędzia do instalowania maszyn wirtualnych
Name:		python-%{appname}
Version:	0.600.4
Release:	1.1
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://virt-manager.org/download/sources/virtinst/%{appname}-%{version}.tar.gz
# Source0-md5:	0be36b08bb8b61eb9d75f0885eacc173
URL:		http://virt-manager.org/
BuildRequires:	gettext-devel
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Requires:	python-libvirt >= 0.4.5
Requires:	python-libxml2
Requires:	python-urlgrabber
Suggests:	python-selinux
Suggests:	virt-viewer >= 0.0.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
virtinst is a module that helps build and install libvirt based
virtual machines. Currently supports KVM, QEmu and Xen virtual
machines. Package includes several command line utilities, including
virt-install (build and install new VMs) and virt-clone (clone an
existing virtual machine).

%description -l pl.UTF-8
virtinst to moduł pomagający przy tworzeniu i instalowaniu maszyn
wirtualnych opartych na libvirt. Obecnie obsługiwane są maszyny KVM,
QEmu i Xen. Pakiet zawiera kilka działających z linii poleceń
skryptów, w tym virt-install (tworzący i instalujący nowe VM-y) oraz
virt-clone (klonujący istniejącą maszynę wirtualną).

%prep
%setup -q -n %{appname}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%find_lang %{appname}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{appname}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/image.rng doc/example1.xml
%attr(755,root,root) %{_bindir}/virt-clone
%attr(755,root,root) %{_bindir}/virt-convert
%attr(755,root,root) %{_bindir}/virt-image
%attr(755,root,root) %{_bindir}/virt-install
%dir %{py_sitescriptdir}/virtconv
%{py_sitescriptdir}/virtconv/*.py[co]
%dir %{py_sitescriptdir}/virtconv/parsers
%{py_sitescriptdir}/virtconv/parsers/*.py[co]
%dir %{py_sitescriptdir}/virtinst
%{py_sitescriptdir}/virtinst/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{appname}-%{version}-py*.egg-info
%endif
%{_mandir}/man1/virt-clone.1*
%{_mandir}/man1/virt-convert.1*
%{_mandir}/man1/virt-image.1*
%{_mandir}/man1/virt-install.1*
%{_mandir}/man5/virt-image.5*
