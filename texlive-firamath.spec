%global tl_name firamath
%global tl_revision 56672

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3.4
Release:	%{tl_revision}.1
Summary:	Fira sans serif font with Unicode math support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/firamath
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/firamath.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/firamath.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Fira Math is a sans-serif font with Unicode math support. The design of
this font is based on Fira Sans and FiraGO. Fira Math is distributed in
OpenType format and can be used with the unicode-math package under
XeLaTeX or LuaLaTeX. More support is offered by the firamath-otf
package.

