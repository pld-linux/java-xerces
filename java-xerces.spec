#
%define	srcname	xerces
#
%include	/usr/lib/rpm/macros.java
Summary:	XML parser for Java
Summary(pl.UTF-8):	Analizator składniowy XML-a napisany w Javie
Name:		java-xerces
Version:	2.9.0
Release:	4
# appears that portions of the code are on other licenses.
# can it all be called "Apache 2.0"?
License:	Apache v2.0
Group:		Applications/Publishing/XML/Java
Source0:	http://www.apache.org/dist/xml/xerces-j/Xerces-J-src.%{version}.tar.gz
# Source0-md5:	bd43e57ec7105acc9f13072e0208d445
# Get Xerces-J-tools to avoid BuildRequires: xerces-j
Source1:	http://www.apache.org/dist/xml/xerces-j/Xerces-J-tools.%{version}.tar.gz
# Source1-md5:	79d48733b0ab41af190f1af7ca89ab3f
Patch0:		xerces-j-target.patch
URL:		http://xml.apache.org/xerces-j/
BuildRequires:	ant >= 1.7.1-4
BuildRequires:	java-gcj-compat-devel
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	java-xml-commons
Requires:	java-xml-commons
Provides:	xerces-j
Provides:	jaxp_parser_impl
Obsoletes:	xerces-j
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML parser for Java.

%description -l pl.UTF-8
Analizator składniowy XML-a napisany w Javie.

%package javadoc
Summary:	Documentation for Xerces - XML parser for Java
Summary(pl.UTF-8):	Dokumentacja do Xercesa - analizatora składniowego XML-a w Javie
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	xerces-j-doc
Obsoletes:	xerces-j-javadoc

%description javadoc
Documentation for Xerces - XML parser for Java.

%description javadoc -l pl.UTF-8
Dokumentacja do Xercesa - analizatora składniowego XML-a w Javie.

%description javadoc -l fr.UTF-8
Javadoc pour Xerces.

%prep
%setup -q -n xerces-%(echo %{version} | tr . _) -a1
%patch0 -p1

%build
required_jars='xml-commons-apis'
CLASSPATH=$(build-classpath $required_jars):./tools/xercesImpl.jar:./tools/bin/xjavac.jar
export CLASSPATH

%ant -Dbuild.compiler=gcj jars javadocs

%install
rm -rf $RPM_BUILD_ROOT
# jars
install -d $RPM_BUILD_ROOT%{_javadir}
cp -a build/xercesImpl.jar $RPM_BUILD_ROOT%{_javadir}/xerces-j2-%{version}.jar
ln -sf xerces-j2-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/xerces-j2.jar
ln -sf xerces-j2-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jaxp_parser_impl.jar
ln -sf xerces-j2-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/xercesImpl.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a build/docs/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%doc LICENSE* NOTICE* README Readme.html
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
