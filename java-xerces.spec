
%define jredir %{_libdir}/jre
%define javadir %{_libdir}/java

Summary:	XML parser for Java
Summary(pl):	Parser metajêzyka XML dla jêzyka Java
Name:		xerces-j
Version:	1.1.3
Release:	1
Group:		Development/Libraries
Source0:	Xerces-J-src.%{version}.tar.gz
Copyright:	GPL
BuildRequires:	/usr/bin/jar
BuildRequires:	jikes
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
N/A

%description -l pl
N/A

%prep
%setup -q -n xerces-1_1_3

%build
export CLASSPATH=%{jredir}/lib/rt.jar
%{__make} JAVAC=jikes jars

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{javadir}
install bin/xerces.jar $RPM_BUILD_ROOT%{javadir}
gzip -9nf README Readme.html LICENSE STATUS

%files
%defattr(644,root,root,755)
%doc {README,Readme.html,LICENSE,STATUS}.gz docs/* docs/dtd
%{javadir}/xerces.jar


%clean
rm -rf $RPM_BUILD_ROOT
