Summary:	XML parser for Java
Summary(pl):	Parser XML napisany w Javie
Name:		xerces-j
Version:	1.4.4
Release:	4
License:	Apache
Group:		Applications/Publishing/XML/Java
Source0:	http://xml.apache.org/xerces-j/dist/Xerces-J-src.%{version}.tar.gz
URL:		http://xml.apache.org/xerces-j/
BuildRequires:	jdk >= 1.1
Requires:	jre >= 1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javaclassdir	/usr/share/java

%description
XML parser for Java.

%description -l pl
Parser XML napisany w Javie.

%prep
%setup -q -n xerces-%(echo %{version} | tr . _)

%build
%{__make} JAVAC="javac -O" jars

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javaclassdir}

install bin/xerces.jar $RPM_BUILD_ROOT%{_javaclassdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Readme.html LICENSE STATUS docs/*
%{_javaclassdir}/xerces.jar
