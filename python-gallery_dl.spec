Name:		python-gallery_dl
Version:	1.29.2
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/g/gallery_dl/gallery_dl-%{version}.tar.gz
Summary:	Command-line program to download image galleries and collections from several image hosting sites
URL:		https://pypi.org/project/gallery_dl/
License:	GPLv2
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Command-line program to download image galleries and collections from several image hosting sites

%files
%{py_sitedir}/gallery_dl
%{py_sitedir}/gallery_dl-*.*-info
%{_bindir}/gallery-dl
%{_datadir}/*
