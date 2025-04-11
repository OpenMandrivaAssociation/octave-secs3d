%define octpkg secs3d

Summary:	A Drift-Diffusion simulator for 2d semiconductor devices with Octave
Name:		octave-%{octpkg}
Version:	0.0.1
Release:	2
Url:		https://packages.octave.org/%{octpkg}/
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
BuildArch:	noarch

BuildRequires:	octave-devel >= 3.2.4
BuildRequires:	octave-bim
BuildRequires:	octave-fpl

Requires:	octave(api) = %{octave_api}
Requires:	octave-bim
Requires:	octave-fpl

Requires(post): octave
Requires(postun): octave

%description
A Drift-Diffusion simulator for 3d semiconductor devices with Octave.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

