Summary:	XML parser for Java
Summary(pl):	Parser XML napisany w Javie
Name:		xerces-j
%define	major	1
%define	minor	4
%define	micro	3
Version:	%{major}.%{minor}.%{micro}
%define ver	%{major}_%{minor}_%{micro}
Release:	1
License:	??
Group:		Applications/Publishing/XML/Java
Group(de):	Applikationen/Publizieren/XML/Java
Group(pl):	Aplikacje/Publikowanie/XML/Java
URL:		http://xml.apache.org/xerces-j
Source0:	http://xml.apache.org/xerces-j/dist/Xerces-J-src.%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	jar
BuildRequires:	jikes
Requires:	jre
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javaclassdir	%{_datadir}/java/classes
%define		jredir		/usr/lib/java-sdk/jre/lib

%description
XML parser for Java.

%description -l pl
Parser XML napisany w Javie.

%prep
%setup -q -n xerces-%{ver}

%build
export CLASSPATH=%{jredir}/rt.jar
%{__make} JAVAC=jikes jars

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
