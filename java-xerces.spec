Summary:	XML parser for Java
Summary(pl):	Parser XML napisany w Javie
Name:		xerces-j
Version:	2.4.0
Release:	1
License:	Apache
Group:		Applications/Publishing/XML/Java
Source0:	http://xml.apache.org/dist/xerces-j/Xerces-J-src.%{version}.tar.gz
# Source0-md5:	7b4ceb6cf1d66037be7221901d9c4143
# Get Xercej-J-tools to avoid Requires: xerces-j
Source1:	http://xml.apache.org/dist/xerces-j/Xerces-J-tools.%{version}.tar.gz
# Source1-md5:	09e18250116de58e0539d110c3fd6cc7
Patch0:		%{name}-jdk14.patch
Patch1:		%{name}-manifest.patch
Patch2:		%{name}-jdk1.4.2.patch
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
Parser XML napisany w Javie.

%package doc
Summary:	Documentation for Xerces-J - XML parser for Java
Summary(pl):	Dokumentacja do Xercesa-J - parsera XML w Javie
Group:		Documentation

%description doc
Documentation for Xerces-J - XML parser for Java.

%description doc -l pl
Dokumentacja do Xercesa-J - parsera XML w Javie.

%prep
%setup -q -n xerces-%(echo %{version} | tr . _)
%patch0 -p1
%patch1 -p1
%patch2	-p1
gzip -dc %{SOURCE1} | tar -x

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
