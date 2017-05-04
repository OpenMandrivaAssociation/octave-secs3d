%define octpkg secs3d

Summary:	A Drift-Diffusion simulator for 2d semiconductor devices with Octave
Name:		octave-%{octpkg}
Version:	0.0.1
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 3.2.4

Requires:	octave(api) = %{octave_api}
Requires:	octave-bim
Requires:	octave-fpl

Requires(post): octave
Requires(postun): octave

%description
A Drift-Diffusion simulator for 3d semiconductor devices with Octave.

This package is part of external Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkgdir}
%{octpkgdir}/*
#%doc %{octpkg}-%{version}/NEWS
%doc %{octpkg}-%{version}/COPYING

