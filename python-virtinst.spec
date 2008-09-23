
%define	appname	virtinst

Summary:	Python modules and utilities for installing virtual machines
Name:		python-%{appname}
Version:	0.400.0
Release:	0.1
License:	GPL v2
Group:		Development/Languages/Python
Source0:	http://virt-manager.org/download/sources/%{appname}/%{appname}-%{version}.tar.gz
# Source0-md5:	484792dfe05abc75082d44fc51b811f3
URL:		http://virt-manager.org
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	gettext
BuildRequires:	python-libvirt >= 0.4.5
BuildRequires:	python-libxml2
BuildRequires:	python-urlgrabber
BuildRequires:	rpmbuild(macros) >= 1.219
#%pyrequires_eq	python-libs
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
virtinst is a module that helps build and install libvirt based
virtual machines. Currently supports KVM, QEmu and Xen virtual
machines. Package includes several command line utilities, including
virt-install (build and install new VMs) and virt-clone (clone an
existing virtual machine).

%prep
%setup -q -n %{appname}-%{version}

%build
export CFLAGS="%{rpmcflags}"
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
%doc README COPYING AUTHORS ChangeLog NEWS doc/image.rng doc/example1.xml
%attr(755,root,root) %{_bindir}/virt-install
%attr(755,root,root) %{_bindir}/virt-clone
%attr(755,root,root) %{_bindir}/virt-image
%attr(755,root,root) %{_bindir}/virt-pack
%attr(755,root,root) %{_bindir}/virt-convert
%dir %{py_sitescriptdir}/virtconv
%{py_sitescriptdir}/virtconv/*.py[co]
%dir %{py_sitescriptdir}/virtconv/parsers
%{py_sitescriptdir}/virtconv/parsers/*.py[co]
%dir %{py_sitescriptdir}/virtinst
%{py_sitescriptdir}/virtinst/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{appname}-*.egg-info
%endif
%{_mandir}/man1/*
%{_mandir}/man5/*
