Summary:	GNU autoconf - source configuration tools
Summary(pl):	GNU autoconf - narz�dzie do automatycznego konfigurowania �r�de�
Name:		autounit
Version:	0.05
Release:	1
License:	GPL
Group:		Development/Building
Group(pl):	Programowanie/Budowanie
Source0:	http://www.recursism.com/projects/autounit/%{name}-%{version}.tar.gz
URL:		http://www.recursism.com/projects/autounit/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%define		_libdir		%{_datadir}

%description
GNU Autounit's goal is to provide a common unit testing framework for                               application developers who use GNU Autoconf already in their projects but                           do not currently use a unit testing framework.

%description -l pl
Celem programu GNU Autounit jest dostarczenie popularnego systemu test�w
dla developer�w aplikacji ju� u�ywaj�cych programu GNU Autoconf w ich
projektach ale aktualnie nie u�ywaj�cych program�w testuj�cych.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
FIXME
