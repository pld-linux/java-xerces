Summary:	XML parser for Java
Summary(pl):	Parser XML napisany w Javie
Name:		xerces-j
%define	major	1
%define	minor	1
%define	micro	3
Version:	%{major}.%{minor}.%{micro}
%define ver	%{major}_%{minor}_%{micro}
Release:	1
Group:		Development/Libraries
License:	Apache Software License
URL:		http://xml.apache.org/xerces-j
Source0:	http://xml.apache.org/xerces-j/dist/Xerces-J-src.%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	/usr/bin/jar
BuildRequires:	jikes
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javaclassdir	%{_datadir}/java/classes
%define		jredir		%{_libdir}/jre

%description
N/A

%description -l pl
N/A

%prep
%setup -q -n xerces-%{ver}

%build
export CLASSPATH=%{jredir}/lib/rt.jar
%{__make} JAVAC=jikes jars

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javaclassdir}
install bin/xerces.jar $RPM_BUILD_ROOT%{_javaclassdir}
gzip -9nf README Readme.html LICENSE STATUS

%files
%defattr(644,root,root,755)
%doc {README,Readme.html,LICENSE,STATUS}.gz docs/* docs/dtd
%{_javaclassdir}/xerces.jar


%clean
rm -rf $RPM_BUILD_ROOT
