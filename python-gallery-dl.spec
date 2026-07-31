%define module gallery-dl
%define oname gallery_dl

Name:		python-gallery-dl
Version:	1.32.8
Release:	1
Summary:	A program to download image galleries from several image hosting sites
License:	GPL-2.0-or-later
Group:		Development/Python
# old repo still exists but moved developement to different forge:
# https://github.com/mikf/gallery-dl/issues/9374
# https://github.com/mikf/gallery-dl
URL:		https://codeberg.org/mikf/gallery-dl
Source0:	https://codeberg.org/mikf/gallery-dl/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

# rename to be consistent with upstream name, pypi name and its executable
%rename python-gallery_dl

%description
%{name} is a command-line program to download image galleries
and collections from several image hosting sites.

%prep -a
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%build -p
# These make options need to be ran prior to building the module in
# order that the build collects them for the install stage.
# make shell completions for bash/fish/zsh.
make completion
# make man pages.
make man

%files
%doc README.rst docs/options.md
%doc docs/configuration.rst
%doc docs/%{module}.conf docs/%{module}-example.conf
%license LICENSE
%{_bindir}/%{module}
%{_datadir}/bash-completion/completions/%{module}
%{_datadir}/fish/vendor_completions.d/%{module}.fish
%{_datadir}/zsh/site-functions/_%{module}
%{_mandir}/man*/%{module}*
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
