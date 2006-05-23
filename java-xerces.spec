%include	/usr/lib/rpm/macros.java
Summary:	XML parser for Java
Summary(pl):	Analizator sk³adniowy XML-a napisany w Javie
Name:		xerces-j
Version:	2.8.0
Release:	1
# appears that portions of the code are on other licenses.
# can it all be called "apache 2.0"?
License:	Apache v2.0
Group:		Applications/Publishing/XML/Java
Source0:	http://www.apache.org/dist/xml/xerces-j/Xerces-J-src.%{version}.tar.gz
# Source0-md5:	162d481e901a302eb82eb40ebeb8653e
# Get Xercej-J-tools to avoid Requires: xerces-j
Source1:	http://www.apache.org/dist/xml/xerces-j/Xerces-J-tools.%{version}.tar.gz
# Source1-md5:	4206f318b43654552f16a9040bdfa6b4
URL:		http://xml.apache.org/xerces-j/
BuildRequires:	jdk >= 1.1
BuildRequires:	ant >= 1.5
BuildRequires:	xml-commons
Requires:	jre >= 1.1
Requires:	xml-commons
Provides:	jaxp_parser_impl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
CLASSPATH="./tools/xercesImpl.jar:./tools/bin/xjavac.jar"
required_jars='xml-commons-apis'
export CLASSPATH="$CLASSPATH:`/usr/bin/build-classpath $required_jars`"
export JAVA_HOME=%{java_home}
export JAVAC=%{javac}
export JAVA=%{java}

%{ant} clean jars javadocs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install build/xerces*.jar $RPM_BUILD_ROOT%{_javadir}
ln -sf  xercesImpl.jar    $RPM_BUILD_ROOT%{_javadir}/jaxp_parser_impl.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ISSUES NOTICE README Readme.html STATUS TODO
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc build/docs/javadocs/*
