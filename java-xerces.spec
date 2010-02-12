#
%bcond_without	javadoc		# don't build javadoc
%if "%{pld_release}" == "ti"
%bcond_without	java_sun	# build with gcj
%else
%bcond_with	java_sun	# build with java-sun
%endif

%define	srcname	xerces

%include	/usr/lib/rpm/macros.java
Summary:	XML parser for Java
Summary(pl.UTF-8):	Analizator składniowy XML-a napisany w Javie
Name:		java-xerces
Version:	2.9.1
Release:	1
# appears that portions of the code are on other licenses.
# can it all be called "Apache 2.0"?
License:	Apache v2.0
Group:		Libraries/Java
Source0:	http://www.apache.org/dist/xerces/j/Xerces-J-src.%{version}.tar.gz
# Source0-md5:	e340cba4a2abf4f0f833488380821153
# Get Xerces-J-tools to avoid BuildRequires: xerces-j
Source1:	http://www.apache.org/dist/xerces/j/Xerces-J-tools.%{version}.tar.gz
# Source1-md5:	6b50c65f2c31d66bb258aa5be79b0e21
Patch0:		xerces-j-target.patch
URL:		http://xerces.apache.org/xerces-j/
BuildRequires:	ant >= 1.7.1-4
%{!?with_java_sun:BuildRequires:	java-gcj-compat-devel}
%{?with_java_sun:BuildRequires:	java-sun}
BuildRequires:	jpackage-utils
BuildRequires:	rpm >= 4.4.9-56
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

%ant jars %{?with_javadoc:javadocs}

%install
rm -rf $RPM_BUILD_ROOT
# jars
install -d $RPM_BUILD_ROOT%{_javadir}
cp -a build/xercesImpl.jar $RPM_BUILD_ROOT%{_javadir}/xerces-j2-%{version}.jar
ln -sf xerces-j2-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/xerces-j2.jar
ln -sf xerces-j2-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jaxp_parser_impl.jar
ln -sf xerces-j2-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/xercesImpl.jar

%if %{with javadoc}
# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a build/docs/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%doc LICENSE* NOTICE* README Readme.html
%{_javadir}/*.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
