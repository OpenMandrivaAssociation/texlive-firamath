Name:		texlive-firamath
Version:	56672
Release:	1
Summary:	Fira sans serif font with Unicode math support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/firamath
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/firamath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/firamath.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Fira Math is a sans-serif font with Unicode math support. The
design of this font is based on Fira Sans and FiraGO. Fira Math
is distributed in OpenType format and can be used with the
unicode-math package under XeLaTeX or LuaLaTeX. More support is
offered by the firamath-otf package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/opentype/public/firamath
%doc %{_texmfdistdir}/doc/fonts/firamath

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
