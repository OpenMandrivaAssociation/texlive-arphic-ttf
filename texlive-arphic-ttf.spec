Name:		texlive-arphic-ttf
Version:	42675
Release:	2
Summary:	TrueType version of Chinese Arphic fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/arphic-ttf
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arphic-ttf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arphic-ttf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides TrueType versions of the Chinese Arphic
fonts for use with XeLaTeX and LuaLaTeX. Type1 versions of
these fonts, for use with pdfLaTeX and the cjk package, are
provided by the arphic package. Arphic is actually the name of
the company which created these fonts.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/truetype/public/arphic-ttf
%doc %{_texmfdistdir}/doc/fonts/arphic-ttf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
