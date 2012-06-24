%include	/usr/lib/rpm/macros.java
Summary:	XML parser for Java
Summary(pl.UTF-8):	Analizator składniowy XML-a napisany w Javie
Name:		xerces-j
Version:	2.9.0
Release:	3
# appears that portions of the code are on other licenses.
# can it all be called "Apache 2.0"?
License:	Apache v2.0
Group:		Applications/Publishing/XML/Java
Source0:	http://www.apache.org/dist/xml/xerces-j/Xerces-J-src.%{version}.tar.gz
# Source0-md5:	bd43e57ec7105acc9f13072e0208d445
# Get Xerces-J-tools to avoid BuildRequires: xerces-j
Source1:	http://www.apache.org/dist/xml/xerces-j/Xerces-J-tools.%{version}.tar.gz
# Source1-md5:	79d48733b0ab41af190f1af7ca89ab3f
Patch0:		%{name}-target.patch
URL:		http://xml.apache.org/xerces-j/
BuildRequires:	ant >= 1.5
BuildRequires:	jdk >= 1.3
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	xml-commons
Requires:	xml-commons
Provides:	jaxp_parser_impl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML parser for Java.

%description -l pl.UTF-8
Analizator składniowy XML-a napisany w Javie.

%package javadoc
Summary:	Documentation for Xerces-J - XML parser for Java
Summary(pl.UTF-8):	Dokumentacja do Xercesa-J - analizatora składniowego XML-a w Javie
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	xerces-j-doc

%description javadoc
Documentation for Xerces-J - XML parser for Java.

%description javadoc -l pl.UTF-8
Dokumentacja do Xercesa-J - analizatora składniowego XML-a w Javie.

%description javadoc -l fr.UTF-8
Javadoc pour %{name}.

%prep
%setup -q -n xerces-%(echo %{version} | tr . _) -a1
%patch0 -p1

%build
required_jars='xml-commons-apis'
export CLASSPATH=$(build-classpath $required_jars):./tools/xercesImpl.jar:./tools/bin/xjavac.jar

%ant jars javadocs

%install
rm -rf $RPM_BUILD_ROOT
# jars
install -d $RPM_BUILD_ROOT%{_javadir}
cp -a build/xercesImpl.jar $RPM_BUILD_ROOT%{_javadir}/xerces-j2-%{version}.jar
ln -sf xerces-j2-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/xerces-j2.jar
ln -sf xerces-j2-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jaxp_parser_impl.jar
ln -sf xerces-j2-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/xercesImpl.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a build/docs/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc LICENSE* NOTICE* README Readme.html
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
