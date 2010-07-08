
%define 	module	dirstore

Summary:	dirstore - Python module for acces files from directories and/or archives
Summary(pl.UTF-8):	dirstore - moduł Pythona umożliwiający dostęp do plików umieszczonych w katalogach i/lub archiwach
Name:		python-%{module}
Version:	0.1.0
Release:	3
License:	GPL v2
Group:		Libraries/Python
Source0:	http://kai.vm.bytemark.co.uk/~piman/software/%{module}-%{version}.tar.gz
# Source0-md5:	559b3e350534110d9acf94e69df3679e
URL:		http://kai.vm.bytemark.co.uk/~piman/software.shtml#dirstore
BuildRequires:	python-modules >= 2.2
BuildRequires:	rpm-perlprov
Requires:	python >= 2.2
Requires:	unrar
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Python module provides a generic object (DirStore) to access
files stored in a directory, tar, rar, or zip archive. You can read
data from the archive as a string or a file-like object without
worrying about the underlying archive format.


%description -l pl.UTF-8
Moduł ten udostępnia ogólny obiekt (DirStore) umożliwiający uzyskanie
dostępu do plików przechowywanych w katalogu lub archiwum tar, rar lub
zip. Moduł ten umożliwia odczyt danych z archiwum w postaci łańcucha
znaków albo obiektu podobnego do file() bez martwienia się formatem
przeglądanego archiwum.

%prep
%setup -q -n %{module}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/dirstore.py[oc]
%doc README
