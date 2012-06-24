Summary:	GNU autoconf - source configuration tools
Summary(pl):	GNU autoconf - narz�dzie do automatycznego konfigurowania �r�de�
Name:		autounit
Version:	0.10
Release:	1
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
Source0:	http://www.recursism.com/projects/autounit/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
URL:		http://www.recursism.com/projects/autounit/
BuildRequires:	glib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Autounit's goal is to provide a common unit testing framework for
application developers who use GNU Autoconf already in their projects
but do not currently use a unit testing framework.

%description -l pl
Celem programu GNU Autounit jest dostarczenie popularnego systemu
test�w dla developer�w aplikacji ju� u�ywaj�cych programu GNU Autoconf
w ich projektach ale aktualnie nie u�ywaj�cych program�w testuj�cych.

%prep
%setup -q
%patch -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%post
%fix_info_dir

%postun
%fix_info_dir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_libdir}/libau-c-unit.a
%{_includedir}/c-unit
%{_infodir}/*info*
