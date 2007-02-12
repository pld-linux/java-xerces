Summary:	XML parser for Java
Summary(pl.UTF-8):   Analizator składniowy XML-a napisany w Javie
Name:		xerces-j
Version:	2.9.0
Release:	1
# appears that portions of the code are on other licenses.
# can it all be called "apache 2.0"?
License:	Apache v2.0
Group:		Applications/Publishing/XML/Java
Source0:	http://www.apache.org/dist/xml/xerces-j/Xerces-J-src.%{version}.tar.gz
# Source0-md5:	bd43e57ec7105acc9f13072e0208d445
# Get Xerces-J-tools to avoid BuildRequires: xerces-j
Source1:	http://www.apache.org/dist/xml/xerces-j/Xerces-J-tools.%{version}.tar.gz
# Source1-md5:	79d48733b0ab41af190f1af7ca89ab3f
URL:		http://xml.apache.org/xerces-j/
BuildRequires:	ant >= 1.5
BuildRequires:	jdk >= 1.1
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	xml-commons
Requires:	jre >= 1.1
Requires:	xml-commons
Provides:	jaxp_parser_impl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML parser for Java.

%description -l pl.UTF-8
Analizator składniowy XML-a napisany w Javie.

%package doc
Summary:	Documentation for Xerces-J - XML parser for Java
Summary(pl.UTF-8):   Dokumentacja do Xercesa-J - analizatora składniowego XML-a w Javie
Group:		Documentation

%description doc
Documentation for Xerces-J - XML parser for Java.

%description doc -l pl.UTF-8
Dokumentacja do Xercesa-J - analizatora składniowego XML-a w Javie.

%prep
%setup -q -n xerces-%(echo %{version} | tr . _) -a1

%build
CLASSPATH="./tools/xercesImpl.jar:./tools/bin/xjavac.jar"
required_jars='xml-commons-apis'
export CLASSPATH="$CLASSPATH:`/usr/bin/build-classpath $required_jars`"
export JAVA_HOME=%{java_home}
export JAVAC=%{javac}
export JAVA=%{java}

%ant clean jars javadocs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install build/xercesImpl.jar $RPM_BUILD_ROOT%{_javadir}
ln -sf xercesImpl.jar $RPM_BUILD_ROOT%{_javadir}/jaxp_parser_impl.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE* NOTICE* README Readme.html
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc build/docs/javadocs/*
