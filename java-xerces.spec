
%define	major	1
%define	minor	4
%define	micro	4

Summary:	XML parser for Java
Summary(pl):	Parser XML napisany w Javie
Name:		xerces-j
Version:	%{major}.%{minor}.%{micro}
Release:	3
License:	Apache Software License
Group:		Applications/Publishing/XML/Java
URL:		http://xml.apache.org/xerces-j
Source0:	http://xml.apache.org/xerces-j/dist/Xerces-J-src.%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	jdk
Requires:	jre
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ver				%{major}_%{minor}_%{micro}
%define		_javaclassdir		/usr/share/java/
%define		jredir			%{_libdir}/java/jre/lib

%description
XML parser for Java.

%description -l pl
Parser XML napisany w Javie.

%prep
%setup -q -n xerces-%{ver}

%build
%{__make} JAVAC="javac -O" jars

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javaclassdir}

install bin/xerces.jar $RPM_BUILD_ROOT%{_javaclassdir}

gzip -9nf README Readme.html LICENSE STATUS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,Readme.html,LICENSE,STATUS}.gz docs/* docs/dtd
%{_javaclassdir}/xerces.jar
