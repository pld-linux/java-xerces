Summary:	XML parser for Java
Summary(pl):	Analizator sk³adniowy XML-a napisany w Javie
Name:		xerces-j
Version:	2.6.2
Release:	1
License:	Apache
Group:		Applications/Publishing/XML/Java
Source0:	http://www.apache.org/dist/xml/xerces-j/Xerces-J-src.%{version}.tar.gz
# Source0-md5:	cfd536b8d72f8ebe3465ae35f5e3775d
# Get Xercej-J-tools to avoid Requires: xerces-j
Source1:	http://www.apache.org/dist/xml/xerces-j/Xerces-J-tools.%{version}.tar.gz
# Source1-md5:	55ba4b71ae95acf7d50c4bc0d796ee76
URL:		http://xml.apache.org/xerces-j/
BuildRequires:	jdk >= 1.1
BuildRequires:	jakarta-ant >= 1.5
BuildRequires:	xml-commons
Requires:	jre >= 1.1
Requires:	xml-commons
Provides:	jaxp_parser_impl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
XML parser for Java.

%description -l pl
Analizator sk³adniowy XML-a napisany w Javie.

%package doc
Summary:	Documentation for Xerces-J - XML parser for Java
Summary(pl):	Dokumentacja do Xercesa-J - analizatora sk³adniowego XML-a w Javie
Group:		Documentation

%description doc
Documentation for Xerces-J - XML parser for Java.

%description doc -l pl
Dokumentacja do Xercesa-J - analizatora sk³adniowego XML-a w Javie.

%prep
%setup -q -n xerces-%(echo %{version} | tr . _) -a1

%build
JAVA_HOME=/usr/lib/java
CLASSPATH=./tools/xercesImpl.jar
CLASSPATH=./tools/bin/xjavac.jar:$CLASSPATH
CLASSPATH=%{_javalibdir}/xml-commons-apis.jar:$CLASSPATH
export JAVA_HOME CLASSPATH
ant clean jars javadocs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}

install build/xerces*.jar $RPM_BUILD_ROOT%{_javalibdir}
ln -sf xercesImpl.jar $RPM_BUILD_ROOT%{_javalibdir}/jaxp_parser_impl.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Readme.html LICENSE STATUS
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc build/docs/javadocs/*
